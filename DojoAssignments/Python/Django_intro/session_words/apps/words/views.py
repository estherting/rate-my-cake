from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'words/index.html')


def process(request):
    if not('input' in request.session):
        request.session['input'] = []

    if request.method == "POST":
        print("*"*150 + "word is: ", request.POST['big'])
        user_input ={}
        user_input['word'] = request.POST['word']
        user_input['color'] = request.POST['color']
        if request.POST['big']:
            user_input['big'] = request.POST['big']
        else:
            user_input['big'] = false

        input = request.session['input']
        input.append(user_input)
        request.session['input'] = input

    return redirect('/result')


def result(request):
    context = {
        'time': strftime("%H:%M %p %Y-%m-%d", gmtime())
    }
    return render(request, 'words/result.html', context)


def reset(request):
    request.session.clear()
    return redirect('/')
