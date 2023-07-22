from django.http import HttpResponse

def index(request):
    return HttpResponse (f"Go to /challenges for the web features.")