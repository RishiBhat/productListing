
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Portfolio
from .forms import PortfolioForm, store   


# Create your views here.


#----------------------------- Model Based Custom Form -------------------------------
def home(request):
    form = PortfolioForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
            form.save()
            return HttpResponse("<h1> Data Stored</h1>")

    return render(request,'base.html', {'form': form})


def display(request):
    ele = Portfolio.objects.all()
    return render(request, 'display.html', {'ele':ele})


def update(request,id):
    upt = Portfolio.objects.get(id=id)
    form = PortfolioForm(instance=upt, data=request.POST or None, files=request.FILES or None)
    if request.POST:
        if form.is_valid:
            form.save()
            return redirect('display')
    return render(request ,'base.html',{'form': form})    


def delete(request, id):
    upt= Portfolio.objects.get(id=id)
    upt.delete()
    return redirect('display')

#-----------------------------Form base Custom Form ----------------------------------

def input_form(request):
    form = store(request.POST or None, request.FILES or None)
    if form.is_valid():
        num = Portfolio()

        num.name = form.cleaned_data['name']
        num.email = form.cleaned_data['email']
        num.city = form.cleaned_data['city']
        num.address = form.cleaned_data['address']
        num.date_time = form.cleaned_data['date_time']
        num.maritialstatus = form.cleaned_data['maritialstatus']
        num.image = form.cleaned_data['image']
        num.biodata = form.cleaned_data['biodata']
        num.save()
        return redirect('input_display')

    return render(request, 'base.html',{'form':form})



def input_display(request):
    elem = Portfolio.objects.all()
    return render (request,'display1.html',{'elem': elem})


def input_updated(request,id):
    ris = Portfolio.objects.get(id=id)
    img = ris.name
    doc = ris.biodata
    
    if request.POST:        
        ris.name=request.POST.get('name')
        ris.email=request.POST.get('email')
        ris.city=request.POST.get('city')
        ris.address=request.POST.get('address')
        ris.contactno=request.POST.get('contactno')
        ris.maritialstatus=request.POST.get('maritialstatus')
        ris.image=request.POST.get('image')
        ris.biodata=request.POST.get('biodata')
        
        if ris.image == None and ris.biodata == None:
            ris.image = img
            ris.biodata = doc
            ris.save()


        elif ris.biodata == None:

            ris.biodata = doc
            ris.save()

        elif ris.image == None:
            ris.image = img
            ris.save()

        else:
            ris.save()

        return redirect('input_display')
    

    return render(request,'update.html', {'ris':ris})     



def input_delete(request, id):
    error= Portfolio.objects.get(id=id)
    error.delete()
    return redirect('input_display')