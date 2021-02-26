# wiki_celeb_gen
Some python scripts that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, then use that data to train an AI!
# Usage
Note: This has only been tested on Windows 10.
Uses Python 3.9.2

Install textgenrnn using pip:
`pip3 install textgenrnn`
Run `generate.py` to use the weights already in the repo.
If the weights are not in the textgenrnn folder of the repo as you read this, install `selenium` and `wikipedia` from pip and run `wikipedia-scrape.py` then run `train.py`.
