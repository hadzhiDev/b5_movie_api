from django import forms

from cinema.models import Genre, Directer, Movie


class GenreForm(forms.Form):
    name = forms.CharField(max_length=300, label='название',)



class MovieForm(forms.ModelForm):
    class Meta: 
        model = Movie
        fields = (
            'name', 
            'description', 
            'year',
            'rating',
            'duration',
            'image',
            'director',
            'genres',
            'is_published',
        )
        # fields = '__all__'
        # exclude = ('is_published',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'span_red ', 'id': 'name_id'}, ),
            'description': forms.TextInput(),
            'year': forms.NumberInput(),
            'rating': forms.NumberInput(),
            'duration': forms.TextInput(),
            'image': forms.FileInput(),
            'genres': forms.CheckboxSelectMultiple(),
            # 'is_published': forms.BooleanField(),
            'director': forms.Select(),
        }