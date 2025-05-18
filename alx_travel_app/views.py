from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to ALX Travel API. Visit /swagger/ for API docs.")
