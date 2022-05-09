from django.shortcuts import render

# Create your views here.
def stockpicker(request):
    return render(request,'mainapp/stockpicker.html')

def stocktracker(request):
    return render(request,'mainapp/stocktracker.html')