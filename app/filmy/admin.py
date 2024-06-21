from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "footage", "director", "genres_display"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "director_name"] 
    list_filter = ["year", "genres"]


class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    list_filter = ["birth_year"]
    pass


class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    pass

class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    list_filter = ["birth_year"]
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)