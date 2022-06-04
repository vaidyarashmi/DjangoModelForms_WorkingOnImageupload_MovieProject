from django import forms
from testapp.models import Movie
import re
import datetime
from django.core.exceptions import ValidationError
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

    def clean_movie_title(self):
        get_movie_title=self.cleaned_data['movie_title']
        if not re.match("^[A-Za-z0-9 ]*$",get_movie_title):
            raise ValidationError("Please enter only string value for movie title")
        return get_movie_title

    def clean_director(self):
        get_director=self.cleaned_data['director']
        if not re.match("^[A-Za-z ]*$",get_director):
            raise ValidationError("Please enter only string value for movie title")
        return get_director
    
    def clean_movie_plot(self):
        get_movie_plot=self.cleaned_data['movie_plot']
        if len(get_movie_plot)>=1000:
            raise ValidationError('Maximum character are allowed is 1000')
        return get_movie_plot
    
    def clean_release_year(self):
        get_release_year=self.cleaned_data['release_year']
        year = datetime.date.today().year
        if get_release_year > year:
            raise ValidationError('Release year cannot be greater than todays date ')  
        return get_release_year

    def clean_movie_poster(self):
        get_movie_poster=self.cleaned_data['movie_poster']
        main, sub = get_movie_poster.content_type.split('/')
        if not (sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
            raise ValidationError('Please use a JPEG or PNG image.')
        return get_movie_poster