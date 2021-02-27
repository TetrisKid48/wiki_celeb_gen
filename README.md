# wiki_celeb_gen
Some Python scripts that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, then use that data to train an AI!  
This is just a project I started for fun, and I just recently learned how to use Python. I hope you enjoy the outcome!

# Example Output
(No output has been generated yet, because Tensorflow for Python 3.9 is currently non-existent!)

# Usage
Note: These scripts have only been tested on Windows 10 with Python 3.9.2, and some files have not been added yet as this is still a work in progress.  

First, download and extract the zip file of this repo. Install textgenrnn using pip:    
`pip3 install textgenrnn`  
Also install the version of tensorflow for your version of Python from PyPi.    
Run `generate.py` to generate 20 AI output sentences using the weights (.hdf5 file) already in the repo.  

If you want to run extra epochs (aka train the AI more), run `train.py`.  
  
If you want to gather the input.txt yourself (which I don't recommend doing), install `wikipedia` and `selenium` using pip, install the Chrome drivers for your version of Chrome from https://pypi.org/project/selenium/, then run `wikipedia-scrape.py`.  

# Some Information
Tensorflow for Python 3.9 has not been released, and I need that to continue this project.  
`train.py` and `generate.py` require the library `textgenrnn` to work. More info here:  
https://github.com/minimaxir/textgenrnn  
  
Important links and sources:  
https://pypi.org/project/wikipedia/  
https://pypi.org/project/selenium/  
https://github.com/minimaxir/textgenrnn  
https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918
