from django.shortcuts import render
from.import forms


def form_name_view(request):
    form = forms.FormName()
    if request.method=="POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Form validation successful! see console:")
            print("Name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("message: " + form.cleaned_data['text'])
    return render(request, 'home.html',{'form':form})        
    
