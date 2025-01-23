from rest_framework import serializers

from cinema.models import Genre, Directer, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directer
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieReadSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()  
    genres = GenreSerializer(many=True) 

    class Meta:
        model = Movie
        fields = '__all__'
    
