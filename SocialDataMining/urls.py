from django.urls import path
from .views import postTweetView, postRedditView, index

urlpatterns = [
    # ' '
    path('', index),
    # postTweet/
    path('tweet/', postTweetView.as_view()),
    # postReddit/
    path('reddit/', postRedditView.as_view())

]
