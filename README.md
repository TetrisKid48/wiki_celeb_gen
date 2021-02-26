# wiki_celeb_gen
Some python scripts that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, then use that data to train an AI!
# Usage
Note: This has only been tested on Windows 10, and some files may be missing from this repo as it is still a work in progress.  
This repo uses Python 3.9.2

First, download and extract the zip file of this repo. Install textgenrnn using pip:    
`pip3 install textgenrnn`  
Run `generate.py` to use the weights (.hdf5 file) already in the repo.  

If the weights are not in this repo as you read this, run `train.py`.  
If you want to gather the input.txt yourself, install `selenium` and `wikipedia` using pip, then run `wikipedia-scrape.py`.  

# Some Information
`wikipedia-scrape.py` gathers the training data from Wikipedia and puts it into an `input.txt` file. It requires the libraries `wikipedia` and `selenium` to work.
I've only tested using selenium with the Chrome drivers.  
`train.py` and `generate.py` require the library `textgenrnn` to work. More info here:  
https://github.com/minimaxir/textgenrnn  
  
Other sources I used:  
https://pypi.org/project/wikipedia/    
https://pypi.org/project/selenium/  
https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918
