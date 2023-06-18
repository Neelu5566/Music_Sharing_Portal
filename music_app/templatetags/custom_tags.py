from django import template

register = template.Library()


@register.filter
def unique_titles(songs_data):
    unique_titles = set()
    unique_songs = []
    for song in songs_data:
        if song.title not in unique_titles:
            unique_titles.add(song.title)
            unique_songs.append(song)
    return unique_songs
