from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()    # object is created

router.register("actors",views.ActorViewSets,basename="actors")  # method is called by created object

router.register("albums",views.AlbumViewSetView,basename="albums")

router.register("trackers",views.TrackerViewsetView,basename="trackers")

urlpatterns=[

    path("movies/",views.MovieListCreateView.as_view()),
    path("movies/<int:pk>/",views.MovieRetriveUpdateDeleteView.as_view()),
    path("movies/languages/",views.LanguagesView.as_view()),
    path("movies/genre/",views.GenerView.as_view())
]+router.urls # object.urls