from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html',{'hithere':'This is me'})

def count(request):
    getTextAreaCont = request.GET['fulltext']
    wordList = getTextAreaCont.split()
    contentDictionary = {}
    for word in wordList:
        if word in contentDictionary:
            #Increase value of the existing word.
            contentDictionary[word] += 1
        else:
            #Add new word to the dictionary.
            contentDictionary[word] = 1
    
    sortedWords = sorted(contentDictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html',{'content': getTextAreaCont, 'wordCount':len(wordList), 'sortedWords':sortedWords})
def about(request):
    return render(request, 'about.html')