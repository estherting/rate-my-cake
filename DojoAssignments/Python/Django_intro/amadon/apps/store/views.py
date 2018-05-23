from django.shortcuts import render, redirect

def index(request):
    return redirect('/amadon')


def amadon(request):
    return render(request, 'store/index.html')


def process(request):
    if request.method == "POST":
        if request.POST['itemId'] == "1":
            price = 19.99
        elif request.POST['itemId'] == "2":
            price = 29.99
        elif request.POST['itemId'] == "3":
            price = 4.99
        elif request.POST['itemId'] == "4":
            price = 49.99

        request.session['total_price'] = price * int(request.POST['quantity'])
        request.session['quantity'] = request.POST['quantity']

    return redirect('/amadon/checkout')


def checkout(request):
    return render(request, 'store/checkout.html')
