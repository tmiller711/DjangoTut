from django import forms

class CreateNewList(forms.Form):
    # label will show up before the box of the form
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)