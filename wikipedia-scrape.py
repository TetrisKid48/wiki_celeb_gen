import wikipedia
import re
import urllib.request
from selenium import webdriver

textfile = open(r'C:\Miscellaneous\Coding\Python\WikipediaProject\textgenrnn\input.txt', 'w', encoding="utf-8")
# sentences are saved to input.txt
# change the file path to work with your setup before running

personlist = []
listlen = 0
count = 0
link = "https://en.wikipedia.org/w/index.php?title=Category:Living_people&pagefrom=Aaltonen%2C+Juhamatti"

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

for b in range(0, 4900):

    # get page's html code

    fp = urllib.request.urlopen(link)
    mybytes = fp.read()
    htmlcode = mybytes.decode("utf8")
    fp.close()

    location1 = htmlcode.index("This list may not reflect recent changes")
    location2 = htmlcode.index("<div class=\"printfooter\">") + 1
    htmlcode = htmlcode[location1:location2]

    # get names and list them  

    location1 = htmlcode.index("<li>")
    location2 = htmlcode.index("</ul>")
    crudelist = htmlcode[location1:location2]

    crudelist = crudelist.replace("<li><a href=\"/wiki/", "")
    personlist = crudelist.split("\n")
    listlen = len(personlist)

    count = 0

    for x in range(0, listlen):
        location1 = personlist[count].index("title=\"") + 7
        location2 = personlist[count].index("\">")
        personlist[count] = personlist[count][location1:location2]
        if count % 25 == 0:
            print(personlist[count])
            count = count + 1
        else:
            count = count + 1
            continue

    print("\n")
    count = 0

    for i in range(0, listlen):

        if count % 25 == 0:
            pass
        else:
            count = count + 1
            continue

        # go through list and save the sentences

        name = personlist[count]

        if "." in name:
            print("## Name did not pass filters. ## \n")
            count = count + 1
            continue

        try:
            sentence = wikipedia.page(name).content
        except:
            print("## Exception occured getting page content. ## \n")
            count = count + 1
            continue
        try:
            cutoff = sentence.index(".") + 1
        except:
            print("## Couldn't find sentence. ## \n")
            count = count + 1
            continue
        sentence = sentence[0:cutoff]
        if "==" in sentence:
            print("## Sentence is oversized. ## \n")
            count = count + 1
            continue
        elif "\n" in sentence:
            sentence = sentence.replace("\n", " ")
        else:
            t = re.findall(" [A-Z][.]", sentence)
            if t:
                print("## Sentence did not pass the middle initial filter. ## \n")
                count = count + 1
                continue
            else:
                sentence = sentence + "\n"
                textfile.write(sentence)

        print(sentence)
        count = count + 1

    # go to the next page

    driver.get(link)
    driver.find_element_by_link_text("next page").click()
    link = driver.current_url

driver.quit()
textfile.close()
print("Finished!")
