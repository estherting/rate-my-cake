from django.shortcuts import render, redirect
import random

def index(request):
    if not('gold' in request.session) and not('activity' in request.session):
        request.session['gold'] = 0
        request.session['activity'] = ""
    return render(request, 'game/index.html')

def process_gold(request, location):
    if request.method == "POST":
        # print("*"*150, "I'm at ", location)
        if location == "farm":
            gold = random.randrange(10, 21)
            request.session['gold'] += gold
            request.session['activity'] += "Earned " + str(gold) + " golds from the farm!<br>"
        if location == "cave":
            gold = random.randrange(5, 11)
            request.session['gold'] += gold
            request.session['activity'] += "Earned " + str(gold) + " golds from the cave!<br>"
        if location == "house":
            gold = random.randrange(2, 6)
            request.session['gold'] += gold
            request.session['activity'] += "Earned " + str(gold) + " golds from the house!<br>"
        if location == "casino":
            gold = random.randrange(-50, 51)
            if gold < 0:
                request.session['text-color'] = "red"
            else:
                request.session['text-color'] = "black"
            # text-color = session['text-color']
            request.session['gold'] += gold
            request.session['activity'] += "<p class='"+ request.session['text-color'] +"'>Earned " + str(gold) + " golds from the casino!</p><br>"

    return redirect('/')
