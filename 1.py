# This script require to have beautifulsoup4 and pyperclip installed
# A script to search a english word in multiple dictionaries.
import requests
import bs4
import webbrowser
import re
import sys
import pyperclip


def oneLook():
    # Fetch the search result page with the requests module.
    resOne = requests.get('https://onelook.com/?w='+word)

    resOne.raise_for_status()

    oneLookSoup = bs4.BeautifulSoup(resOne.text, 'html.parser')

    dictionaries = ['www.collinsdictionary.com/dictionary/english',
                    'www.oxforddictionaries.com/us/definition/american_english',
                    'www.vocabulary.com/definition',
                    'dictionary.cambridge.org/dictionary']

    for i in range(len(dictionaries)):
        # All a tags with this regex(dictionary url)
        allDicts = oneLookSoup.findAll("a", href=re.compile(
            dictionaries[i]))

        myurl = ''

        for web in allDicts:
            myurl = web['href']

        webbrowser.open(myurl)

    webbrowser.open('https://www.ldoceonline.com/dictionary/'+word)

    def printAllAFromOneLook():
        # Optional
        allAlinks = oneLookSoup.select('#section-dicts > ol[start="1"] li a')
        for mylink in allAlinks:
            print(mylink)


word = ''
if(len(sys.argv) < 2):
    word = pyperclip.paste()
    oneLook()

elif(len(sys.argv) > 2 or len(sys.argv) == 2 and sys.argv[1] == 'sy'):
    if(len(sys.argv) == 2):
        word = pyperclip.paste()
        webbrowser.open('https://onelook.com/thesaurus/?s='+word)
        webbrowser.open(
            'https://www.collinsdictionary.com/dictionary/english-thesaurus/'+word)
    elif(len(sys.argv) > 2):
        word = ' '.join(sys.argv[1:])
        webbrowser.open('https://onelook.com/thesaurus/?s='+word)
        webbrowser.open(
            'https://www.collinsdictionary.com/dictionary/english-thesaurus/'+word)
elif(len(sys.argv) == 2):
    word = sys.argv[1]
    oneLook()
elif(len(sys.argv) > 2):
    word += ' '.join(sys.argv[1:])
    oneLook()
