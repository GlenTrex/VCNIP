from django.shortcuts import render
from django.http import HttpResponse
from .models import VoteCenter
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchVoteCenter')
    if searchTerm:
        votecenters = VoteCenter.objects.filter(sitename__icontains=searchTerm)
    else:
        votecenters = VoteCenter.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'votecenters':votecenters})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})