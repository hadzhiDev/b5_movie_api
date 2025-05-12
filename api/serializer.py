from rest_framework import serializers

from cinema.models import Genre, Directer, Movie, Atrubute


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directer
        fields = '__all__'


class AtrubuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrubute
        fields = '__all__'


class AtrubuteForMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrubute
        fields = ('name', 'value')


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateSerializer(serializers.ModelSerializer):
    atributes = AtrubuteForMovieSerializer(many=True, required=False)
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False, allow_empty=True
    )

    class Meta:
        model = Movie
        fields = (
            'name', 'description', 'year', 'rating', 'duration', 'image', 
            'director', 'genres', 'is_published', 'content', 'atributes'
        )
    
    def create(self, validated_data: dict):
        print(validated_data, type(validated_data))
        atributes = validated_data.pop("atributes", [])
        genres = validated_data.pop("genres", [])
        print(validated_data)

        movie = Movie.objects.create(**validated_data)

        for atribute in atributes:
            Atrubute.objects.create(movie=movie, **atribute)

        if genres:
            movie.genres.set(genres)

        return movie



class MovieReadSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()  
    genres = GenreSerializer(many=True) 
    atributes = AtrubuteSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = '__all__'
    
