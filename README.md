# wiki_celeb_gen
A Python script that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, and another that will generate new ones using an RNN!
This is just a project I started for fun, and I just recently learned how to use Python. I hope you enjoy the outcome!

# Example Output
Andreas Tran (born 23 June 1967) is a Norwegian artist, born in Longon, Mexico) is a retired Indian politician of the Catholic Church of the County Assembly of Jensers of Commond FC surgery.  
  
Luis Alband (born 2 April 1988) is a Spanish footballer who plays for Collinghaine from 1983 to 1993.  
  
Christopher Bonta  is an international basketball player who plays as a Midfielder for Plademporia.  
  
James Daversock (born 7 December 1966) is an English rugby league footballer, manager in the American Football League (VFL).
  
Alexander Scillin (born 1972) is a Canadian politician and a member of the National Assembly of the University of San Durging and the American Second since the 1992 Summer Olympics.  

# Usage
Note: These scripts have only been tested on Windows 10 with Python 3.9.2, and some files have not been added yet as this is still a work in progress.  

First, download and extract the zip file of this repo. Install textgenrnn using pip:    
`pip3 install textgenrnn`  
Also install the version of tensorflow or tf-nightly from PyPi that is compatible with your version of Python.  
Run `generate.py` to generate a `textgenrnn_text.txt` file with tons of AI output sentences. 
  
If you want to gather the input.txt yourself (which I don't recommend doing), install `wikipedia` and `selenium` using pip, install the Chrome drivers for your version of Chrome from https://pypi.org/project/selenium/, then run `wikipedia-scrape.py`.  

# Some Information
`generate.py` requires the library `textgenrnn` to work. More info here:  
https://github.com/minimaxir/textgenrnn  
It also requires tensorflow, and as of right now only the nightly version is compatible with Python 3.9.  
The RNN was trained with the Google Collab linked in the repo above.  
  
Important links and sources:  
https://pypi.org/project/wikipedia/  
https://pypi.org/project/selenium/  
https://github.com/minimaxir/textgenrnn  
https://pypi.org/project/tf-nightly/  
https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918
