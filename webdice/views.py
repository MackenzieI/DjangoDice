from django.shortcuts import render
import random

#from .forms import DiceForm

# Create your views here.
def roll(request, sides=6):
    Droll = random.randint(1, sides)

    return render(request, 'dice.html', {'roll': Droll})
