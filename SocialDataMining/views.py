from .forms import tweetForm, redditForm
from django.views.generic.edit import FormView
import pymongo
from django.shortcuts import render

client = pymongo.MongoClient(
    "mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/SDMTechniques?retryWrites=true&w=majority")
dataBase = client["SDMTechniques"]
twitterCollection = dataBase["twitterData"]
redditCollection = dataBase["redditData"]


# Create your views here.
def index(request):
    return render(request, 'home.html')


class postTweetView(FormView):
    template_name = 'tweet.html'
    form_class = tweetForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            message = form.cleaned_data.get("message")
            insert_val = {'message': message}
            twitterCollection.insert_one(insert_val)
            form.tweetData(message)
            return super().form_valid(form)


class postRedditView(FormView):
    template_name = 'reddit.html'
    form_class = redditForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            title = form.cleaned_data.get("title")
            message = form.cleaned_data.get("message")
            insert_val = {
                'title': title,
                'message': message
            }
            redditCollection.insert_one(insert_val)
            form.redditData(title, message)
            return super().form_valid(form)
