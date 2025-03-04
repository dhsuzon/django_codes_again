from django.shortcuts import render,redirect
from profiles.forms import ProfileForm

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        
            return redirect('add_profile')
            
    
    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {'form': form})