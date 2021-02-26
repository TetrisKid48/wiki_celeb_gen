# wiki_celeb_gen
Some python scripts that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, then use that data to train an AI!
# Usage
Note: This has only been tested on Windows 10, and some files may be missing from this repo as it is still a work in progress.
Uses Python 3.9.2

First, download all of the code.
Install textgenrnn using pip:  
`pip3 install textgenrnn`  
Run `generate.py` to use the weights (.hdf5 file) already in the repo.  
If the weights are not in the textgenrnn folder of the repo as you read this, run `train.py`.  

If you want to gather the input.txt yourself, install `selenium` and `wikipedia` using pip, then run `wikipedia-scrape.py`.  
Always make sure that the path in `wikipedia-scrape.py` will save `input.txt` to the same folder as `train.py` before running it.
