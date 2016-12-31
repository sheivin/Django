from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    given = request.GET['giventext'].lower()

    givenInList = given.split()
    translatedText = ''
    for word in givenInList:
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            # do nothing because vowel
            translatedText += word
            translatedText += 'yay '
        else:
            translatedText += word[1:] + word[0] + 'ay '

    return render(request, 'translate.html', {'given': given, 'translatedText': translatedText})

def about(request):
    return render(request, 'about.html')