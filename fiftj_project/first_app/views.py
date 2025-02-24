from django.shortcuts import render
from .forms import ContactForm,StudentData

# Create your views here.
def Home(request):
    return render(request,'home.html')
def About(request):
    if request.method=="GET":
        print(request.GET)
        name = request.GET.get("UserName")
        email = request.GET.get("UserEmail")
        select = request.GET.get("select")
        return render(request,'about.html',{'name':name,'email':email,'select':select})
    return render(request,'about.html')

def submit_form(request):
    # if request.method=="POST":
    #     name = request.POST.get("UserName")
    #     email = request.POST.get("UserEmail")
    #     return render(request,'forms.html',{'name':name,'email':email})
    return render(request,'forms.html')


def DjangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
        #   file = form.get["File"]
        #   with open("./first_app/upload/" + file.name,"wb+") as dastination:
        #       for chunk in file.chunks():
        #           dastination.write(chunk)

          print(form.cleaned_data)
          return render(request,'django_form.html', {'form':form})
    else:
        form = ContactForm()
    return render(request,'django_form.html', {'form':form})



def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():

          print(form.cleaned_data)
          return render(request,'django_form.html', {'form':form})
    else:
        form =StudentData()
    return render(request,'django_form.html', {'form':form})
        
        