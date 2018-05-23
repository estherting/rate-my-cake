from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not ('count' in request.session):
        request.session['count'] = 0
    return render(request, 'random_word/index.html')


def makeWord(request):
    # generate random word
    # if not ('count' in request.session):
    #     request.session['count'] = 0
    if request.method == "POST":
        request.session['word'] = get_random_string(length=14)
        print('*'*150)
        request.session['count'] += 1
    # print('*'*150)
    # print('*'*150, request.session['count'])
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
