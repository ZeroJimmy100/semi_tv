from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

#taking the objects in show
def index(request):
    show = Show.objects.all()
    context = {
        "these_show": show
    }
    return render(request, "index.html", context)

#takes every objects in Show
def addPage(request):
    show = Show.objects.all()
    context = {
        "these_show": show,
        
    }
    return render(request, "shows.html", context)
    

def Create_Show(request):
    # hereShow = Show.objects.get(id=show_Val) 
    #if request.method == "POST":
    newShow = Show.objects.create(title = request.POST["call_title"], 
    network = request.POST["call_network"], description = request.POST["call_desc"], 
    release_date = request.POST["call_RD"])
    show_Val = newShow.id
    print(show_Val)
    return redirect(f"/shows/{show_Val}")


#Process the page and creates it with the id it was given when made
def letShow(request, show_Val):
    hereShow = Show.objects.get(id=show_Val)
    context = {
        "this_show": hereShow
    }
    return render(request, 'shows_read.html', context)


#Edit the show page 
def EditShow(request, my_Val):
    myShow = Show.objects.get(id = my_Val)
    print(myShow.title)
    
    context = {
        "this_show": myShow,
    }
    return render(request, "shows_edit.html", context)

#letEdit takes the process of what was given in EditShow
def letEdit(request, my_Val):
    myShow = Show.objects.get(id = my_Val)
    myShow.title = request.POST["call_title"]
    myShow.network = request.POST["call_network"]
    myShow.description = request.POST["call_desc"]
    myShow.release_date = request.POST["call_RD"]
    myShow.save()
    return redirect("/shows/{}/edit".format(my_Val)) #formating

def deleteShow(request, got_Val):
    delShow = Show.objects.get(id = got_Val)
    delShow.delete()
    return redirect("/shows")





# Create your views here.
