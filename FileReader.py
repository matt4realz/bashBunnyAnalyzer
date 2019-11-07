import re
from nltk.corpus import stopwords
import math

def processFile(file):
    cleanedList = []
    stop_words = set(stopwords.words('english')) #see if need to remove
    openFile = open(file, 'r')

    for eachLine in openFile:
        # Clean up text, Remove the Symbols
        eachLine = re.sub('[/<>{}()."]', ' ', eachLine)
        eachLine = re.sub("[+-=*,./\()<>?!{:;}']", ' ', eachLine)
        eachLine = re.sub(r'(\n[ \t]*)+', '\n', eachLine)

        # Change to lowercase
        eachLine = eachLine.lower()
        # Remove next lines and tabs for whitespaces
        splitLine = eachLine.strip("\n\t").split(" ")

        for i in range(len(splitLine)):
            if splitLine[i] not in stop_words:
                cleanedList.append(splitLine[i])

    return cleanedList #cleanup with stop words
