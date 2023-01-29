[![ci-cd](https://github.com/UBC-MDS/twitter-persona/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/twitter-persona/actions/workflows/ci-cd.yml) [![Documentation Status](https://readthedocs.org/projects/twitterpersona/badge/?version=latest)](https://twitterpersona.readthedocs.io/en/latest/?badge=latest) ![PyPI](https://img.shields.io/pypi/v/twitterpersona) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
# twitterpersona

Twitter is a popular social media app with over 1 billion user accounts. While a diversity of users is a strength, some individuals have concerns with the prevalence of "troll" accounts and individuals who exhibit unconstructive tone and diction whom they deem not worth engaging with.
The package twitterpersona is intended to provide insight into a twitter user based on their tweet history in effort to determine if an account is worth engaging with. The package provides an easy to use interface for determining the general sentiment expressed by a user.

## Contributors and Maintainers
- [Renzo Wijngaarden](https://github.com/Hawknum)
- [Roan Raina](https://github.com/roanraina)
- [Andy Wang](https://github.com/tiger12055)
- [Yurui Feng](https://github.com/Yurui-Feng)


## Quick Start

To get started with `twitterpersona`, install it using `pip`:

```bash
$ pip install twitterpersona
```
Please visit the [documentation](https://twitterpersona.readthedocs.io/en/latest/?badge=latest) for more information and examples.

## Classes and Functions
1. `load_twitter_msg`: returns a user's recent tweets (as a dataframe) given their `user id` using the Twitter API.
   1. `user_info()`: get user credentials details
   2. `load_twitter_by_user()`: load specific user's tweets
   3. `load_twitter_by_keywords()`: load specific keyword's tweets
2. `sentiment_analysis`: determines the general (average) sentiment of recent tweets
   1. `sentiment_labler()`: returns all tweets with the corresponding labels
3. `preprocessing`: a spotter that identifies credit card numbers
   1. `generalPreprocessing`: returns the processed tweet dataframe
4. `generate_word_cloud`: a spotter that identifies credit card numbers
   1. `create_wordcloud`: returns a matplotlib plot of the wordcloud

Below is a simple quick start example:

```python
from twitterpersona import load_twitter_msg, sentiment_analysis, preprocessing, generate_word_cloud

# Create a cleanser, and don't add the default spotters
user = user_info('consumer key', 'consumer secret', 'access_token', 'token_secret')
twitter_df = load_twitter_by_user('someuser', 30, user)
sentiment_df = sentiment_labler(twitter_df, 'text')
cleaned_df = generalPreprocessing(sentiment_df)
plt = generate_word_cloud(cleaned_df)
```
In order to run test, you need to first install the vader_lexicon package

```bash
$ python -m nltk.downloader vader_lexicon
```
## Scope and Fit

There are existing packages that preform tweet analysis (including [twitter-sentiment-analysis](https://github.com/abdulfatir/twitter-sentiment-analysis), [tweetlytics](https://github.com/UBC-MDS/tweetlytics), and [pytweet](https://github.com/UBC-MDS/pytweet)). However, none of these packages focus of providing metrics in the context of determining if the twitter user is worth engaging with.

## Contributing

Interested in contributing? Check out the contributing guidelines in CONTRIBUTING.md. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`twitterpersona` was created by Andy Wang, Renzo Wijngaarden, Roan Raina, Yurui Feng. It is licensed under the terms of the MIT license.

## Credits

`twitterpersona` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
