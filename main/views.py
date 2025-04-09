from django.http import HttpResponse

def home(request):
    return HttpResponse("Привіт! Це перша сторінка.")