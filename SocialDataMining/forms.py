from django import forms
import tweepy
import praw

consumer_key = "DK5tOhScNSfC3KQpB2JygCZMT"
consumer_secret_key = "dUcgkJUuUoAvKCWMzH4VYnGdqH6AewWi4JaEGpOnQnEeDgehUb"
access_token = "1353025325014380546-6pxpG5qNrrryXH4sD1OkHRRgY6Y9PQ"
access_token_secret = "hsUbC58XN2dI6ZbS1frbYyjkbVhNEEjTwi1CzYPvIbhRC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id="ExnOhz7DPrSj6A",
                     client_secret="i37JQJjharBA72fQd1f-nPVBdIyUQQ",
                     password="synchronizedA@w5",
                     user_agent="test app posting in reddit by u/blueblueandblack",
                     username="blueblueandblack")


class tweetForm(forms.Form):
    message = forms.CharField()

    def tweetData(self, message):
        print(message)
        tweet = message
        api.update_status(tweet)


class redditForm(forms.Form):
    title = forms.CharField()
    message = forms.CharField()

    def redditData(self, title, message):
        print(title, message)
        reddit.subreddit("test").submit(title, message)



