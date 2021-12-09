from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request,'index.html')

def dinner(request):
    id = request.GET.get('id')

    dinners=['짜장','짬뽕','고추잡채','김치']
    food = random.choice(dinners)
    context ={
        'food': food ,
        'id': id,
        'dinners' : dinners
    }
    return render(request,'dinner.html',context)