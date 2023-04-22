from msilib.schema import ListView
from django.shortcuts import render


# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'post/home.html'



