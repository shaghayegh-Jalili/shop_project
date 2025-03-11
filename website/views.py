from django.http import HttpResponse


def myIndex(request):
    return HttpResponse('<h1>Website Index</h1>')

