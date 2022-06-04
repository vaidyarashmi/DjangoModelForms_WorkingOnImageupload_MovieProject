from django.shortcuts import render,redirect
from testapp.forms import MovieForm
from testapp.models import Movie
from django.contrib import messages

# Create your views here.

def movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/testapp/movie')
        else:
            print("Invalid form submission")  
        
    movies=Movie.objects.all()
    return render(request,'index.html',{'form':form,'movies':movies})