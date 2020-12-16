from django.shortcuts import render
from .models import about
from .models import slider
from .models import privacy
from .models import term






def home(request):
    aboutdata = about.objects.all()
    sliderdata = slider.objects.all()
    context = {
        'about':aboutdata,
        'slider':sliderdata,
    }
    return render(request,'index.html',context)



 
def aboutus(request):

    return render(request,'about.html')



def service(request):

    return render(request,'service.html')

def privacypolice(request):
    privacydata = privacy.objects.all()
   
    context = {
        'privacy':privacydata,
        
    }

    return render(request,'privacypolice.html', context)

def termsinservice(request):
    termsinservicedata = term.objects.all()
   
    context = {
        'term':termsinservicedata,
        
    }

    return render(request,'termsinservice.html', context)


    







