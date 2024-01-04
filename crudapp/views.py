from django.shortcuts import render,redirect
from .forms import personform
from .forms import Person
from django.http import HttpResponse
# Create your views here.


def create(request):
    form = personform
    context = {"form":form}

    if request.method == "POST":
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/read")

    else:
        form = personform()
    return render(request,"create.html",context)

def read(request):
    form = Person.objects.all()
    context = {"form": form}

    return render(request,"viewpage.html",context)


def update(request,id):
    data = Person.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        form = personform(request.POST,instance = data)
        print("post check")
        if form.is_valid():
            print("valid check")
            form.save()
            return redirect("/read")
    return render(request,"updatepage.html",context)   


   



def delete(request,id):
    data = Person.objects.get(id=id)
    data.delete()
    return redirect("/read")

