from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Stream

def index(request):
    return render(request, 'stream/index.html')

def stream(request, username):
    context = { 'username': username}
    return render(request, 'stream/user.html', context)

# https://benwilber.github.io/streamboat.tv/nginx/rtmp/streaming/2016/10/22/implementing-stream-keys-with-nginx-rtmp-and-django.html
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def on_publish(request):
    # nginx-rtmp makes the stream name available in the POST body via `name`
    stream_key = request.POST['name']
    # Assuming we have a model `Stream` with a foreign key
    # to `django.contrib.auth.models.User`, we can
    # lookup the stream and verify the publisher is allowed to stream.
    stream = get_object_or_404(Stream, key=stream_key)

    # You can ban streamers by setting them inactive.
    if not stream.user.is_active:
        return HttpResponseForbidden("inactive user")

    # Set the stream live
    stream.live_at = timezone.now()
    stream.save()

    # Redirect the private stream key to the user's public stream
    # NOTE: a relative redirect like this will not work in
    #       Django <= 1.8
    return HttpResponseRedirect(stream.user.username)


@csrf_exempt
@require_POST
def on_publish_done(request):
    # When a stream stops nginx-rtmp will still dispatch callbacks
    # using the original stream key, not the redirected stream name.
    stream_key = request.POST['name']

    # Set the stream offline
    Stream.objects.filter(key=stream_key).update(live_at=None)

    # Response is ignored.
    return HttpResponse("OK")
