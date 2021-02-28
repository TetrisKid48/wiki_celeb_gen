# wiki_celeb_gen
A Python script that will scrape Wikipedia for the first sentence of a bunch of pages in the "Living people" category, and train an RNN on that data!
This is just a project I started for fun, and I just recently learned how to use Python. I hope you enjoy the outcome!

# Example Output
Robert Ross de Michael Courhs Jackson, is a British writer and politician.   
  
Andreas Tran (born 23 June 1967) is a Norwegian artist, born in Longon, Mexico) is a retired Indian politician of the Catholic Church of the County Assembly of Jensers of Commond FC surgery.  
  
Luis Alband (born 2 April 1988) is a Spanish footballer who plays for Collinghaine from 1983 to 1993.  
  
Christopher Bonta  is an international basketball player who plays as a Midfielder for Plademporia.  
  
James Daversock (born 7 December 1966) is an English rugby league footballer, manager in the American Football League (VFL).
  
Alexander Scillin (born 1972) is a Canadian politician and a member of the National Assembly of the University of San Durging and the American Second since the 1992 Summer Olympics.  
  
José Antonio "Cherry" Ross (born 1959) is a British businessman and politician.  
  
Radney Aflail (pronounced \[ˈvɨddele) bɑlağlle (born 6 February 1971) is a Nigerian footballer who is thi currently the 1stwary player from Verhota.
  
Dan Hlojon is an American professional who has worked as the extroander, thrower of the spots for the world.

# Usage
Choose one of the two options below to generate sentences like the examples above.

## Option 1: Google Collab
Go to the link [here](https://colab.research.google.com/drive/1B4QnWmTSI1FrlDvvBWcVyV4vsJ180R4Y#scrollTo=RTa6zf3e_9gV).  
(Credit to [minimaxir](https://github.com/minimaxir) for the original code and Google Collab template.)  
Run the cell to get a text file of generated output (a wiki_celeb_gen_gentext file.) This may take a while.

## Option 2: generate.py
### Warning: This method is currently a work in progress, and may not work. These scripts have only been tested on Windows 10 with Python 3.9.2.
First, download and extract the zip file of this repo. Install textgenrnn using pip:    
`pip3 install textgenrnn`  
Also install the version of tensorflow or tf-nightly from PyPi that is compatible with your version of Python.  
Run `generate.py` to generate a `textgenrnn_text.txt` file with AI output sentences.
  
If you want to gather the input.txt yourself (which I don't recommend doing), install `wikipedia` and `selenium` using pip, install the Chrome drivers for your version of Chrome from [the selenium PyPi page](https://pypi.org/project/selenium/), then run `wikipedia-scrape.py`.  

# Some Information
`generate.py` requires the library `textgenrnn` to work. More info [here](https://github.com/minimaxir/textgenrnn).
It also requires tensorflow, and as of right now only the nightly version is compatible with Python 3.9.   
  
Important links and sources:  
https://pypi.org/project/wikipedia/  
https://pypi.org/project/selenium/  
https://github.com/minimaxir/textgenrnn  
https://pypi.org/project/tf-nightly/
