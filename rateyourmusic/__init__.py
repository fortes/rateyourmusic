import extruct
import requests
import re
import w3lib.html
import pprint

SCHEMA_AGGREGATE_RATING_URL = "http://schema.org/AggregateRating"
SCHEMA_MUSIC_ALBUM_URL = "http://schema.org/MusicAlbum"
SCHEMA_MUSIC_GROUP_URL = "http://schema.org/MusicGroup"
SCHEMA_MUSIC_RECORDING = "http://schema.org/MusicRecording"

RYM_URL_MATCHER = re.compile(
    'https?://rateyourmusic.com/release/album/[^/]+/[^/]+')


class AlbumReview:
    """
    Class representing the fetched review

    Includes the following fields:
    - artist
    - name
    - average_rating
    - num_ratings
    - genres
    - numtracks
    - tracklist
    """

    def __init__(self, microdata):
        for data in microdata:
            type = data.get('type')
            properties = data.get('properties')

            if not type or not properties:
                continue

            if type == SCHEMA_MUSIC_ALBUM_URL:
                self.url = (
                    'https://rateyourmusic.com%s' % properties.get('url'))
                self.name = properties.get('name')

                artist = properties.get('byArtist')
                if artist and artist.get('type') == SCHEMA_MUSIC_GROUP_URL:
                    artist_properties = artist.get('properties')
                    if artist_properties:
                        name = artist_properties.get('name')
                        if isinstance(name, list):
                            self.artist = name[0]
                        else:
                            self.artist = name

                rating = properties.get('aggregateRating')
                if rating and rating.get(
                        'type') == SCHEMA_AGGREGATE_RATING_URL:
                    rating_properties = rating.get('properties')
                    if rating_properties:
                        self.average_rating = float(
                            rating_properties.get('ratingValue'))
                        self.num_ratings = int(
                            rating_properties.get('ratingCount'))

                
                genre = properties.get('genre')
                if genre:
                    self.genre = genre

                numtracks = properties.get('numTracks')
                if numtracks:
                    self.numtracks = numtracks
                
                tracks = properties.get('track')
                if tracks:
                    self.tracklist = []
                    for track in tracks:
                        if track.get('type') == SCHEMA_MUSIC_RECORDING:
                            track_properties = track.get("properties")
                            self.tracklist.append(track_properties.get("name"))                   


def isValidRateYourMusicURL(url):
    return RYM_URL_MATCHER.search(url) != None


def fetchAlbumReviewHTML(url):
    if not isValidRateYourMusicURL(url):
        raise ValueError('Invalid RYM album url')

    headers = {'User-Agent': 'RYM Python Scraper'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise IndexError(
            'Non-200 status code from RateYourMusic %s' % r.status_code)

    return r.text


def getAlbumReviewForRateYourMusicUrl(url):
    """
    Get `AlbumReview` object for an RYM album URL
    """
    html = fetchAlbumReviewHTML(url)
    base_url = w3lib.html.get_base_url(html, url)
    data = extruct.extract(html, base_url=base_url)
    microdata = data.get('microdata')
    if not microdata:
        raise IndexError('No microdata found in URL: %s' % url)

    return AlbumReview(microdata)
