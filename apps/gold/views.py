from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'logs' not in request.session:
        request.session['logs'] = []
    return render(request, 'gold/index.html')

def process_money(request, action):
    entry = ''
    gold = 0
    if action == "casino":
        gold += get_gold(0, 50)
        sub = True if random.randint(0,1) == 1 else False
        if sub:
            request.session['gold'] -= gold
            entry += 'Entered a Casino and lost {} golds... ouch..'.format(gold)
        else:
            request.session['gold'] += gold
            entry += 'Entered a Casino and earned {} golds... booyah'.format(gold)
        add_log(request, "minus" if sub else "plus", entry)
    else:
        entry += 'Earned {} from {}!'
        if action == "house":
            gold += get_gold(2, 5)
        elif action == "cave":
            gold += get_gold(5, 10)
        else:
            gold += get_gold(10, 20)
        request.session['gold'] += gold 
        add_log(request, 'plus',entry.format(gold, action.capitalize()))
        
    return redirect('/gold')


def add_log(request, cls, entry):
    request.session['logs'].append([cls, "{:%Y-%m-%d %H:%m}".format(datetime.datetime.now()), entry])
    request.session.modified = True
 
 
def get_gold(lbound, ubound):
   return random.randint(lbound, ubound +1)

