from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def shop(request):
    return render(request, 'main/shop.html')


def track(request):
    return render(request, 'main/track.html')



