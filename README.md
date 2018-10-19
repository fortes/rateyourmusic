# RateYourMusic

[![build status](https://travis-ci.org/fortes/rateyourmusic.svg?branch=master)](https://travis-ci.org/fortes/rateyourmusic) [![PyPI version](https://badge.fury.io/py/rateyourmusic.svg)](https://badge.fury.io/py/rateyourmusic)

Metadata scraper [RateYourMusic](https://rateyourmusic.com) reviews.

## Installation

```sh
pip install rateyourmusic
```

Alternatively, clone directly from `master` to run with the freshest bugs:

```sh
pip install git+git://github.com/fortes/rateyourmusic.git@master
```

## Usage

```
>>> import rateyourmusic
>>> review = rateyourmusic.getAlbumReviewForRateYourMusicUrl('https://rateyourmusic.com/release/album/edan/beauty_and_the_beat/')
>>> print(review.rating)
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
* RateYourMusic will hopefully add an API some day and this will all be wasted effort

## License

MIT

## Contributions

Please do
