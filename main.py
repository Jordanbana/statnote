import os

#path = 'myNotesFolder/oldTestFiles/'
path = 'myNotesFolder/'
numbrOfStudents = 0.0
def getText():
    global numbrOfStudents
    for i in os.listdir(path):
        fileName = path + i
        if fileName[-3:] == 'txt':
            numbrOfStudents = numbrOfStudents + 1
            file = open(fileName,"r")
            #lines = file.readlines()[0]
            for lines in file.readlines():
                textFiles.append(lines.lower().strip().split())
            file.close()

textFiles = []
filteredWordsFromEachFile = []


commonWordsFilename = "CommonWords.txt"
commonFile = open(commonWordsFilename,"r")
commonWords = []
line = commonFile.readline()
while line:
    commonWords.append(line.strip())
    line = commonFile.readline()


def get_words(words):
    wordsFound = []
    counts = []
    for x in words:
        if not x in wordsFound and not x in commonWords:
            counts.append([words.count(x), x])
            """we are taking all of the filtered words from all files
            and adding them to one list"""
            filteredWordsFromEachFile.append([words.count(x),x])
            wordsFound.append(x)
            counts.sort()
    return counts

getText()
for words in textFiles:
    counts = get_words(words)
    counts.sort()
    counts = list(reversed(counts))
    """print counts"""

"""
print ""
print ""
print filteredWordsFromEachFile
print ""
print ""
"""

#starting to cross refernce all notes and see what words are the same
i = 0
m = 1

for x in range(len(filteredWordsFromEachFile)):
    for y in range(x + 1, len(filteredWordsFromEachFile)):
        if filteredWordsFromEachFile[x][1] == filteredWordsFromEachFile[y][1]:
            filteredWordsFromEachFile[x][0] += filteredWordsFromEachFile[y][0]

finalWordCounts = []

def wordIsInFinal(word):
    for x in finalWordCounts:
        if x[1] == word:
            return True
    return False

for x in filteredWordsFromEachFile:
    if not wordIsInFinal(x[1]):
        finalWordCounts.append(x)

finalWordCounts.sort()
"""
print list(reversed(finalWordCounts))
print ""
print ""
"""


#lets get the averages of every word!
for x in range(len(filteredWordsFromEachFile)):
    filteredWordsFromEachFile[x][0] = (filteredWordsFromEachFile[x][0])/numbrOfStudents

finalWordCounts.sort()
print "Number of students:", numbrOfStudents
print list(reversed(finalWordCounts))[:15]

topTenWords=[]
topTenWords=list(reversed(finalWordCounts))[:15]

##PLOTTING SHITTTTTTT
import plotly.plotly as py
from plotly.graph_objs import *
# Fill in with your personal username and API key
# or, use this public demo account
py.sign_in('sbrill', '0gvkq9193t')

names = []
values = []
for z in topTenWords:
    names.append(z[1])
    values.append(z[0])

data = Data([
    Bar(
        x=names,
        y=values
    )
])
plot_url = py.plot(data, filename='basic-bar')
#print textFiles


menuInput = raw_input("Would you like to search for a specific keyword? (yes or no): ")
if menuInput.lower() == "yes":
    keywordSearch = raw_input("What keyword or phrase do you want to search for?: ")
    for i in finalWordCounts:
        if keywordSearch == i[1]:
            keywordSearchResults = i[0]
            print keywordSearchResults
elif menuInput.lower() == "no":
    print "FINE!"
elif menuInput != "no" or menuInput != "yes":
    print "Not a valid search"
