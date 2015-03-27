from django.shortcuts import render, redirect
import requests
import base64
import json

# Create your views here.
def hello(request):

        return render(request, "bye.html")
def parse_response(twitter_feed):
    final_array = []

    for tweet in twitter_feed:
        tweet = {
            "image_url": tweet['user']['profile_image_url'],
            "text": tweet['text'],
            "name": tweet['user']['name'],
            "screen_name": tweet['user']['screen_name'],
            "place": tweet['place']['full_name']
        }
        final_array.append(tweet)

    return final_array

def tweets(request):
    print request.GET['lat']
    print request.GET['long']
    lat = request.GET['lat']
    long = request.GET['long']
    consumer_key = "KQzqRm5CWEZ2gFfLnjTaB9Bhg"
    consumer_secret = "WukZb9SOT4jK5IOltdpIPiI3SW61mM5FHpzE68yuTSp4ZwdfwY"

    bearer_credentials = base64.b64encode(consumer_key + ":" + consumer_secret)
    bearer_response = requests.post("https://api.twitter.com/oauth2/token", headers={"Authorization": "Basic " + bearer_credentials, "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}, data="grant_type=client_credentials")
    bearer_token = json.loads(bearer_response.text)["access_token"]

    response = requests.get("https://api.twitter.com/1.1/search/tweets.json?geocode="+lat+","+long+",25mi&src=typd", headers={"Authorization": "Bearer " + bearer_token, "Accept-Encoding":"gzip"})
    r_array = response.json()['statuses']
    final_array = parse_response(r_array)


    return render(request, "hello.html", {"data":final_array})
#
# def bye(request):
#     foo = (2+ 2)
#     return render(request, "bye.html", {"name": foo})
