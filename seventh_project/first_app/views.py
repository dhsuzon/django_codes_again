from django.shortcuts import render
from first_app.forms import StudentForm

def Home(request):
    if request.method =="POST": 
       form = StudentForm(request.POST)
       if  form .is_valid():
           form.save(commit=True)
           print(form.cleaned_data)
           return render(request, 'home.html',{'form':form})
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form':form})