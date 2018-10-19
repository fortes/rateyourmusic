# RateYourMusic

[![build status](https://travis-ci.org/fortes/rateyourmusic.svg?branch=master)](https://travis-ci.org/fortes/rateyourmusic) [![PyPI version](https://badge.fury.io/py/rateyourmusic.svg)](https://badge.fury.io/py/rateyourmusic)

An unofficial scraper [RateYourMusic](https://rateyourmusic.com) reviews.

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
>>> print(review.album)
'Beauty and the Beat'
>>> print(review.rating)
3.72
```

## Tests

There is one test, you can try it:

```bash
python -m unittest
```

## License

MIT

## Contributions

Please do
