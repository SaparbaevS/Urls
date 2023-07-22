from django.shortcuts import render

from urls.models import Sneakers, Tshirts, Souvenirs


def start_page(request):
    return render(request, 'index.html')

def show_sneakers(request):
    context = {'sneakers': Sneakers.objects.all()}
    return render(request, 'showSneakers.html', context=context)


def show_tshirts(request):
    context = {'tshirts': Tshirts.objects.all()}
    return render(request, 'showTshirts.html', context=context)


def show_souvenirs(request):
    context = {'souvenirs': Souvenirs.objects.all()}
    return render(request, 'showSouvenirs.html', context=context)
