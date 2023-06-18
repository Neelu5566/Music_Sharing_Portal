from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Song
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q


def home(request):
    return render(request, 'home.html')


def songs(request):
    if request.user.is_authenticated:
        songs_data = Song.objects.filter(
            Q(user=request.user) | Q(privacy='public') | Q(privacy='protected', allowed_users=request.user)
        ).distinct()  # Add distinct() to remove duplicate songs
        allowed_emails = (
            Song.objects.filter(privacy='protected', allowed_users=request.user)
            .values_list('allowed_users__email', flat=True)
            .distinct()
        )
    else:
        songs_data = Song.objects.filter(privacy='public')
        allowed_emails = []

    user = request.user

    context = {'songs_data': songs_data, 'user': user, 'allowed_emails': allowed_emails}
    return render(request, 'songs.html', context)




@login_required
def song_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        artist = request.POST['artist']
        audio_file = request.FILES['audio_file']
        privacy = request.POST['privacy']

        song = Song(user=request.user, title=title, artist=artist, audio_file=audio_file, privacy=privacy)
        song.save()

        allowed_emails = request.POST.getlist('allowed_emails')
        if allowed_emails:
            allowed_users = User.objects.filter(email__in=allowed_emails)
            song.allowed_users.set(allowed_users)

        messages.success(request, "Song uploaded successfully.")
        request.session['allowed_emails'] = allowed_emails
        return redirect('songs')
    else:
        users = User.objects.all().exclude(pk=request.user.pk)
        context = {'users': users,}
        return render(request, 'upload_song.html', context)






