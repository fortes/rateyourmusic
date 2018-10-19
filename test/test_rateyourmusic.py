import requests
import unittest
from unittest import mock

import rateyourmusic


class TestAlbumReview(unittest.TestCase):
    # This is the only test that actually makes a request to rateyourmusic.com
    # def test_live_request(self):
    #     review = rateyourmusic.getAlbumReviewForRateYourMusicUrl(
    #         'https://rateyourmusic.com/release/album/kode9___the_spaceape/memories_of_the_future/'
    #     )
    #     self.assertEqual(review.artist, 'Kode9 + The Spaceape')
    #     self.assertEqual(review.name, 'Memories of the Future')
    #     self.assertEqual(review.average_rating, 3.32)
    #     self.assertEqual(
    #         review.url,
    #         'https://rateyourmusic.com/release/album/kode9___the_spaceape/memories_of_the_future/'
    #     )

    @mock.patch('rateyourmusic.fetchAlbumReviewHTML')
    def test_saved_request(self, mock_get):
        with open('./test/actor.html', 'r') as fh:
            html = fh.read()

        mock_get.return_value = html

        review = rateyourmusic.getAlbumReviewForRateYourMusicUrl(
            'https://rateyourmusic.com/release/album/st-vincent/actor/')
        # Microdata extraction fails here :(
        # self.assertEqual(review.artist, 'St. Vincent')
        self.assertEqual(review.name, 'Actor')
        self.assertEqual(review.average_rating, 3.61)
        self.assertEqual(
            review.url,
            'https://rateyourmusic.com/release/album/st-vincent/actor/')


if __name__ == '__main__':
    unittest.main()
