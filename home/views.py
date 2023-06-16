from django.shortcuts import render,redirect
from django.http import HttpResponse
import random

from . import modules

# Create your views here.


def index(request):
    
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html")
    
    
def about(request):
    return render( request,"about_us.html")
def contact(request):
    return render(request,"contact_us.html")
def booking(request):
    if request.session["login_status"]:
        user_id=request.session["user_id"]
        details=modules.booking_details(user_id)
        ids=modules.approved_ids()
        context={"data":details,"ids":ids}
       
        return render( request,"gallery.html",context)
    else:
        return redirect("/login")
def service(request):
    return render( request,"services.html")
def signup(request):
    return render( request,"signup.html")
def signup_button(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    password=request.POST.get("password")
    data={"name":name,"email":email,"password":password}
    if modules.check_email(email)==True:
        request.session["signup_status"]=False
        request.session["signup_error"]=True
        
        
        return redirect("/signup")
    else:
        request.session["signup_status"]=True
        request.session["signup_error"]=False
        modules.signup(data)
        
        return redirect("/")
def login(request):
    return render(request,"login.html")
def logout(request):
    request.session["login_status"]=False
    return redirect("/")
def login_button(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    if modules.login(email,password)==True:
        request.session["user_id"]=email
        request.session["login_status"]=True
        request.session["login_error"]=False
    
        return redirect("/")
    else:
        request.session["login_error"]=True
        return redirect("/login")
     
def booking_button(request):
    department=request.POST.get("department")
    doctor=request.POST.get("doctor")
    date=request.POST.get("date")
    time=request.POST.get("time")
    id=random.randint(1000, 9999)
    context={"id":id,"department":department,"doctor":doctor,"date":date,"time":time}
    request.session["context"]=context
    return render(request,"confirmation.html",context)
def booking_confirm(request):
    
    modules.booking(request.session["context"],request.session["user_id"])
    
    return redirect("/booking")
def admin_page(request):
    return render(request,"admin_login.html")

def booking_cancel(request):
    id=request.POST.get("id")
    modules.cancel_booking(id,request.session["user_id"])
    return redirect("/booking")
def admin_login_submit(request):
    email=request.POST.get("email") 
    password=request.POST.get('password')
    print(email,password)
    if modules.admin_login(email,password):
        return render(request,"admin.html")
    else:
        return redirect("/admin_login_page") 
def admin_bookings(request):
    users=modules.booking_admin()
    context={"context":users}
    return render(request,"booking_admin.html",context)
def user_select(request):
    email=request.POST.get("email")
    bookings=modules.users_bookings(email)
    ids=modules.approved_ids()
    context={"data":bookings,"ids":ids}
    return render(request,"users_bookings.html",context)
def booking_approve(request):
    id=request.POST.get("id")
    modules.id_enter(id)
    
    return redirect("/bookings_admin") 