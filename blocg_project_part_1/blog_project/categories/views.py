from django.shortcuts import render,redirect
from categories.forms import CategoryForm

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            return  redirect('add_category')
    else:
        form = CategoryForm()
    
    return render(request,'add_category.html', {'form': form})