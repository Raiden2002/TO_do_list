from django.shortcuts import render ,redirect
from .forms import MyForm
# Create your views here.
def register(request):
    form = MyForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request,'register.html',{'form':form})