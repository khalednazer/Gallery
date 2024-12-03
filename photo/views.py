from django.shortcuts import redirect, render
from .form import form
from .models import Phot, Cat
from .filter import fil
# Create your views here.

def one(request):
    return render(request, 'main.html', {} )

def create(request):
    forms = form()
    if request.method == "POST":
        forms = form(request.POST, request.FILES)
        newone = request.POST['create']
        if newone :
            forms.catg = newone
        
        if forms.is_valid(): 
            forms.save()             
            return redirect('homee')

        
    return render(request, 'create.html', {'form':forms})

def pht(request):
    data = Phot.objects.all()
    allCat =Cat.objects.all()
    fill = fil(request.GET , queryset = data)
    data = fill.qs

# new filter not used
    # repons=request.GET.get("catg")
    # if repons == None:
    #     newff = Phot.objects.all()
    # else:
    #     newff = Phot.objects.filter(catg__name = repons)


    if request.method == 'POST' :
        requests = request.POST.keys()
        try_to_get = Cat.objects.get(name__in = requests)
        alfooo = Cat.objects.get(name = try_to_get)
        alfo = alfooo.oks.all()
        return render(request, 'phots.html', {'data':alfo, 'filter':fill, 'catt':allCat} )
    
    return render(request, 'phots.html', {'data':data, 'filter':fill , 'catt':allCat, 'filtt':'newff'} )


def photslug(request, slug):
    data = Phot.objects.get(slug = slug)
    
    return render(request, 'phot.html', {'one':data} )
