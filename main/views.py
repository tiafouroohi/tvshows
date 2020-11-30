from django.shortcuts import render, redirect
from .models import Show, Network
from django.contrib import messages

def index(request):
    all_show = Show.objects.all ()
    all_network = Network.objects.all()
    context = {
        "all_show" : all_show,
        "all_network" : all_network,
    }
    return render(request, "add_a_show.html", context)

def process(request):
    err = Network.objects.basic_validator(request.POST)
    if len(err) > 0:
        for item in err.values():
            messages.error(request, item)
        return redirect('/')
    Show.objects.create(
        title = request.POST['title'],
        release_date = request.POST['release_date'],
    )
    return redirect('/shows')

def shows(request): #THIS SHOWS A LIST OF THE SHOWS
    all_show = Show.objects.all ()
    all_network = Network.objects.all()
    context = {
        "all_show" : all_show,
        "all_network" : all_network,
    }
    return render(request, "all_shows.html", context)

def all_shows(request, show_id): #THIS REDIRECTS TO THE INDIVIDUAL PAGE
    this_show = Show.objects.get(id=show_id)
    context = {
        'show' : this_show,
        'all_show' : Show.objects.all()
    }
    return render(request, "shows.html", context)

def edit_shows(request, show_id): #TAKES US TO EDIT THE SHOW
    this_show = Show.objects.get(id=show_id)
    context = {
        'show' : this_show,
        'all_show' : Show.objects.all()
    }
    return render(request, "edit_shows.html", context)

def process_edit_shows(request, show_id):
    err = Network.objects.basic_validator(request.POST)
    if len(err) > 0:
        for item in err.values():
            messages.error(request, item)sh
        return redirect('/')
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.release_date = request.POST['release_date']
    show.save()
    print(request.POST)
    return redirect(f'/shows/{show.id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    show.save()
    return redirect('/shows')



# Create your views here.
#First go thorugh and make the routes where you can render the pages(all html, put h1 saying something)
#Make navigation between them to see if it works 
#Put the logic in(make route to process post requests, etc)
#Print statement, urls.py, html
#Check the exact route something is taking!!!!! url, shows, functions 