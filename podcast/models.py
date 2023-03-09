from django.db import models
from podcast_user.models import PodcastUser
from django.utils import timezone
import pyaudio,subprocess
import requests
from django.views import View
from django.shortcuts import render,HttpResponse

class Podcast(models.Model):
    creator = models.ForeignKey(PodcastUser, on_delete=models.CASCADE, related_name='created_podcasts')
    guests = models.ManyToManyField(PodcastUser, blank=True, related_name='invited_to_podcasts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)
    is_live = models.BooleanField(default=False)
    is_recorded = models.BooleanField(default=False)
    recording_file = models.FileField(upload_to='podcast_recordings/', blank=True, null=True)
    broadcast_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def start_recording(self):
        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)

        url = f'http://localhost:8000/podcasts/{self.id}/stream_audio/'

        while self.is_recording:
            data = stream.read(CHUNK_SIZE)
            requests.post(url, data=data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def start_live_stream(self):
        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)

        url = f'http://localhost:8000/podcasts/{self.id}/stream_audio/'

        while self.is_live_streaming:
            data = stream.read(CHUNK_SIZE)
            requests.post(url, data=data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def stop_recording(self):
        pid = self.recording_pid
        subprocess.call(['kill', '-SIGTERM', str(pid)])
        self.is_recording = False
        self.save()

    def stop_live_stream(self):
        self.is_live_streaming = False
        self.save()

    def stop_live_stream(self):
        self.is_live_streaming = False
        self.save()

class PodcastStreamView(View):
    def post(self, request, podcast_id):
        audio_data = request.body
        podcast = Podcast.objects.get(id=podcast_id)
        # process audio data in the context of the podcast (e.g., save to a file, stream to a live audience)
        return HttpResponse(status=200)