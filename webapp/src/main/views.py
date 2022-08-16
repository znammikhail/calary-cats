from django.http import HttpResponse


def home(request):
    # start s task
    return HttpResponse('<h1>Гружу кота!<h1>')



