from django.shortcuts import render

# Create your views here.

def index(r):
    return render(r,"home.html")
def h(r):
    return render(r,"Project.htm")
def about(r):
    return render(r,"about.html")
def login(r):
    return render(r,"login.html")
def tutor_register(r):
    return render(r,"tutor_register.html")
def terms(r):
    return render(r,"terms.html")
def profilee(r):
    return render(r,"profilee.html")
def doctor(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"doctor.html",context)

def repair(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"repair.html",context)

def education(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"education.html",context)
def sports(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"sports.html",context)
def restaurant(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"restaurant.html",context)
def housekeep(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"housekeep.html",context)
def baby(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"baby.html",context)    
def beauty(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"beauty.html",context)
def needs(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"needs.html",context)
def loans(r):
    name=r.GET["credential"]
    context={"detail":name}
    print(name,"home")
    return render(r,"loans.html",context)
def doct1(r):
    return render(r,"doct1.html")

