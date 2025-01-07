from django import forms

class DiceForm(forms.Form):
    NUMBER_OF_SIDES = [
        ('S_six', '6'),
        ('S_Three', '3'),
        ('S_seven', '7')
    ]

    sides = forms.ChoiceField(sides=NUMBER_OF_SIDES)
"""
    NUMBER_OF_DICE = [
        ('D_one', '1'),
        ('D_two', '2')
    ]
"""