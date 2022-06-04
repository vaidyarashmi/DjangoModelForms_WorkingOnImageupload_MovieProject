from django.contrib import admin
from testapp.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=['id','movie_title','release_year','director','movie_poster','movie_plot']


admin.site.register(Movie,MovieAdmin)