
from rest_framework import serializers

from myapp.models import movie,Actor,Album,Trackers,Review


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=movie
        fields="__all__"


class ActorSerializer(serializers.ModelSerializer):

    class Meta:

        model=Actor
        fields="__all__"


class TrackSerializer(serializers.ModelSerializer):

    album_object=serializers.StringRelatedField(read_only=True)    # to get the title of the album instead of id

    class Meta:

        model=Trackers

        fields="__all__"

        read_only_fields=["id","album_object"]


class ReviewSerializer(serializers.ModelSerializer):

    album_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review
        fields="__all__"

        read_only_fields=["created_date","id","album_object"]



class AlbumSerializer(serializers.ModelSerializer):

    songs=TrackSerializer(many=True,read_only=True)

    song_count=serializers.CharField(read_only=True)

    reviews=ReviewSerializer(many=True,read_only=True)

    review_count=serializers.CharField(read_only=True)

    average_rating=serializers.CharField(read_only=True)

    class Meta:

        model=Album
        fields=["id","title","language","director","year","song_count","review_count","average_rating","songs","reviews"]







