from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"first.html")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    #Check which checkbox is on
    punctuations = '''!()-[]{;:'"\,<>./}?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
   
