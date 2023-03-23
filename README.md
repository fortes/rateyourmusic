# No longer maintained

This is no longer maintained, code is archived and available for forking though.

# RateYourMusic

[![build status](https://travis-ci.org/fortes/rateyourmusic.svg?branch=master)](https://travis-ci.org/fortes/rateyourmusic) [![PyPI version](https://badge.fury.io/py/rateyourmusic.svg)](https://badge.fury.io/py/rateyourmusic)

Metadata scraper [RateYourMusic](https://rateyourmusic.com) reviews.

## Installation

```sh
pip install rateyourmusic
```

Alternatively, clone directly from `master` to run with the freshest bugs:

```sh
pip install git+https://github.com/fortes/rateyourmusic.git@master
```

## Usage

```
>>> import rateyourmusic
>>> review = rateyourmusic.getAlbumReviewForRateYourMusicUrl('https://rateyourmusic.com/release/album/edan/beauty_and_the_beat/')
>>> print(review.average_rating)
3.72
```

## Tests

There is one test, you can try it:

```bash
python -m unittest
```

## Warnings

* This was a quick hack for a small project, it may or may not work for you
* Not all sites like having scrapers, use at your own risk
* RateYourMusic/Sonemic is taking forever to create an API so this is the next best thing

## License

MIT

## Contributions

Please do
