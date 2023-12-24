# This file made by Aayush kapil

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request ,'index.html')

def analyze(request):
    djtext = request.POST.get('text' ,'default')
    
    removepunc = request.POST.get('removepunc' , 'off')
    capital = request.POST.get('capital' , 'off')
    new = request.POST.get('new' , 'off')
    length = request.POST.get('length' , 'off')
    

    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                
        params ={'purpose':'Remove punctuation' , 'analyzed_text':
            analyzed}
        djtext = analyzed
              
                
    if capital == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params ={'purpose':'capitalize the text ' , 'analyzed_text':
             analyzed}
        djtext = analyzed
        
    
    if new == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
               

        params ={'purpose':'remove new line' , 'analyzed_text':
             analyzed}
        djtext = analyzed
        
    if length == "on":
        count = 0
        for char in djtext:
            count = count +1

        params ={'purpose1': " count the length of text ", 'analyzed_text':
            count}
        
        return render(request , 'analyze.html' , params)
   
    return render(request , 'analyze.html' , params)





