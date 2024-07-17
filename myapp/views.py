from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import movie

from myapp.forms import MovieForm, MovieModelForm

# Create your views here.


class Movie_list(View):

    def  get(self,request,*args,**kwargs):

        qs=movie.objects.all()

        return render(request,"movie_list.html",{"data":qs})
    
class MovieCreateView(View):

    def get(self,request,*args,**kwargs):
        
        #form_instance=MovieForm()   # create a movie form instance

        form_instance=MovieModelForm()

        return render(request,"movie_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        #form_instance=MovieForm(request.POST)
        form_instance=MovieModelForm(request.POST)

        if form_instance.is_valid():

            #data=form_instance.cleaned_data

            #print(data)

            #movie.objects.create(**data)
            form_instance.save()

            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form_instance})    # evide redirect kodutha the enter details in the form  will detail and gives a new form so render is given
        
            
# localhost:8000/movies/2/
# path("movies/<int:pk>/")  ivide <> igane koduthathu values dynamic anu athaa
#method:get


class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        #kwargs={"pk":2}

        id=kwargs.get("pk")

        qs=movie.objects.get(id=id)

        return render(request,"movie_details.html",{"data":qs})


# localhost:8000/movies/{id}/remove
#method:get

class  MovieDeleteView(View):
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie.objects.get(id=id).delete()

        return redirect("movie-list")

# editing movie

# url: localhost:8000/movie/{id}/change/
#method :get ,post

class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        
        movie_object=movie.objects.get(id=id)         # ithu oru query set we cwn't take values from .it should change in dictionatry

        #dictionary={
        
        #    "run_time":movie_object.run_time,
        #    "director":movie_object.director,
        #    "language":movie_object.language,
        #    "genre":movie_object.genre,
        #    "producer":movie_object.producer

        #}                         # dictionary here used is a variable name

        #form_instance=MovieForm(initial=dictionary)
        form_instance=MovieModelForm(instance=movie_object)

        return render(request,"movie_update.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            movie.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        else:

            return render(request,"movie_update.html",{"form":form_instance})











