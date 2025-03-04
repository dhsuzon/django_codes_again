from django.shortcuts import render,redirect
from author.forms import AuthorForm

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            return redirect('add_author')
            
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})