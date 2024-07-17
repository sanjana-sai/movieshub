from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import movie,Actor,Album,Trackers

from api.serializers import MovieSerializer,ActorSerializer,AlbumSerializer,TrackSerializer,ReviewSerializer

from rest_framework import viewsets

from rest_framework.decorators  import  action 
# Create your views here.


class MovieListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        #//lofic for listing all Movies

        qs=movie.objects.all()

        serializer_instance=MovieSerializer(qs,many=True)    # object is created for serializer and many  is used because more than one objects are used

        return Response (data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        #adding movie 

        serializer_instance=MovieSerializer(data=request.data)  # deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

       
    
class MovieRetriveUpdateDeleteView(APIView):

    def get(self,request,*args,**kwargs):

        #extract id from urls and display the movieid=id

        
        id=kwargs.get("pk")

        movie_obj=movie.objects.get(id=id)

        # movie obj is an query set or model instance  so ew should convert python native type

        serializer_instance =MovieSerializer(movie_obj,many=False)

        return Response(data=serializer_instance.data)
    

       
    def put(self,request,*args,**kwargs):

        #extract the id from the urls and update the movie 

        id=kwargs.get("pk")

        movie_obj=movie.objects.get(id=id)

        # movie obj is an query set or model instance  so ew should convert python native type

        serializer_instance =MovieSerializer(data=request.data,instance=movie_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):

        # logivc for delete the movie

        id=kwargs.get("pk")

        movie_obj=movie.objects.get(id=id)

        movie_obj.delete()

        return Response(data={"message":"movie deleted"})
    

class LanguagesView(APIView):

    def get(self,request,*args,**kwargs):

        qs=movie.objects.all().values_list("language",flat=True).distinct()  # list ayyitu represnt cheeyum so serialization venda

        return Response(data=qs)
    
class GenerView(APIView):

    def get(self,request,*args,**kwargs):

        qs=movie.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=qs)

#================================================

class  ActorViewSets(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serialzer_instance= ActorSerializer(qs,many=True)

        return Response(data=serialzer_instance.data)
    
    def create(self,request,*args,**kwargs):

        serializer_instance=ActorSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:
            return Response(data=serializer_instance.errors)
        

    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=serializer_instance.data)
    
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(data=request.data,instance=actor_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)



    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        actor_obj.delete()

        return Response({"message":"message-deleted"})    
    


class AlbumViewSetView(viewsets.ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()


    #custom methods
    #url:localhost:8000/api/albums/languages/
    
    @action( methods=["GET"],detail=False)
    def language(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("language",flat=True).distinct()
        
        return Response(data=qs)
    
    @action(methods=["GET"],detail=False)
    def director(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("director",flat=True).distinct()

        return Response(data=qs)
    


 #url:localhost:8000/api/albums/{id}/add_track
# method:POST

    @action(methods=["POST"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)


        serializer_instance=TrackSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

 # url:localhost:8000/api/album/{id}/add_review/       
    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

#url:localhost:8000/api/trackers/{id}/

class TrackerViewsetView(viewsets.ModelViewSet):

    serializer_class=TrackSerializer

    queryset=Trackers.objects.all()
        

