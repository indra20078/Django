from django.shortcuts import render

from django.http import HttpResponse

def main(request):
    return HttpResponse("This webpage contains three pages:\n <a href=http://127.0.0.1:8000/w><button>Click here</button></a>\n <a href=http://127.0.0.1:8000/about><button>Click here</button></a>\n <a href=http://127.0.0.1:8000/h><button>Click here</button></a> ")
    
    

def index(request):
    return render(request, 'main.html')
    
def analyze(request):
    # Get the text

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinerm = request.POST.get('newlinerm', 'off')
    print(removepunc)
    print(djtext)
    # Analyze the text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'CAPITALIZED TEXT - ', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlinerm == 'on':
        analyzed = ""
        for char in djtext: 
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': ' New line removed ', 'analyzed_text': analyzed}
        djtext = analyzed

    return render(request, 'analyze.html', params)

