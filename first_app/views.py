from django.shortcuts import render
from .forms import MyForm  # Replace with your actual form

def home(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    return render(request, 'home.html', {'form': form})
