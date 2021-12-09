from community.forms import PersonForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Person
from django.views.decorators.http import require_http_methods,require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    persons = Person.objects.order_by('-pk')
    context={
        'persons':persons
    }
    return render(request,'community/index.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method=="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('community:detail',person.pk)
    else:
        form = PersonForm()
    context = {
        'form':form
    }
    return render(request,'community/form.html',context)

@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    person = get_object_or_404(Person,pk=pk)
    if request.method=='POST':
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            person = form.save()
            return redirect('community:detail',person.pk)
    else:
        form = PersonForm(instance=person)
    context={
        'form':form,
        'person':person
    }
    return render(request,'community/form.html',context)

@login_required
@require_safe
def detail(request,pk):
    person = get_object_or_404(Person,pk=pk)
    context={
        'person':person
    }
    return render(request,'community/detail.html',context)

@login_required
@require_http_methods('POST')
def delete(request,pk):
    person =get_object_or_404(Person,pk=pk)
    if request.method =="POST":
        person.delete()
    return redirect('community:index')