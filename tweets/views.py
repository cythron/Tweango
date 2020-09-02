import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url

from .models import Tweet
from .forms import TweetForm

ALLOWERD_HOSTS = settings.ALLOWED_HOSTS

def home_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Home View</h1>")
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    print("ajax", request.is_ajax())
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # obj = form.clean_content()
        obj.save()
        if request.is_ajax():
            return JsonResponse({}, status=201)
        if next_url != None and is_safe_url(next_url, ALLOWERD_HOSTS):
            redirect(next_url)
        form = TweetForm()
    return render(request, 'pages/home.html', context={"form":form})

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data["content"] = tweet.content
    except:
        data["message"] = "Not Found"
        status = 404
    return JsonResponse(data, status=status) # json.dumps, content_type='application/json'

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "response": tweets_list,
        "is_user": False,
    }
    return JsonResponse(data)