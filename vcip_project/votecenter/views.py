from django.shortcuts import render
from django.http import HttpResponse
from .models import VoteCenter
from django.shortcuts import get_object_or_404

# Create your views here.
# each function defines a html page

def home(request):
    searchTerm = request.GET.get('searchVoteCenter')
    if searchTerm:
        votecenters = VoteCenter.objects.filter(sitename__icontains=searchTerm)
    else:
        votecenters = VoteCenter.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'votecenters':votecenters})

# about page
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

# signup page
def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

# detail page
def detail(request, votecenter_id):
    votecenter = get_object_or_404(VoteCenter,pk=votecenter_id)
    return render(request, 'detail.html', {'votecenter':votecenter})