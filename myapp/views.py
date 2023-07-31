from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import form_Customer,loginform,logoutform,password_changeform,Talk_form,Name_changeform,Email_changeform,Img_changeform
from django.contrib.auth.views import LoginView
from .models import CustomUser, Talk_model
import datetime
from django.db.models import Q
def index(request):
    return render(request, "myapp/index.html")


def login_view(request):
    if request.method=="GET":
        form=loginform()
        return render(request, "myapp/login.html",{"form":form})

def friends(request):
    return render(request, "myapp/friends.html")

def talk_room(request,CustomUser_id):
    talk_list=CustomUser.objects.filter(id=CustomUser_id).first()
    friend=get_object_or_404(CustomUser,id=CustomUser_id)
    friend_information=Talk_model.objects.filter(Q(talk_from=request.user,talk_to=friend)|Q(talk_from=friend,talk_to=request.user)).order_by("talk_time")
    print(request, "this")
    params={"friend_information":friend_information}
    params["talk_list"]= talk_list
    
    
    if request.method =="POST":
        form=Talk_form(request.POST)
        if form.is_valid():
            form_saved = form.save(commit=False)
            today = datetime.datetime.today()
            talk_from = request.user
            talk_to = CustomUser.objects.get(pk=CustomUser_id)
            message = request.POST.get("message")
            form_saved.talk_time = today
            form_saved.talk_from = talk_from
            form_saved.talk_to = talk_to
            form_saved.message = message 
            form_saved.save()
            # return redirect("talk_room", CustomUser_id=CustomUser_id)
            params["form"] = Talk_form() 
            return render(request, "myapp/talk_room.html", params)
        else:
            print(form.errors)
    else:
        form = Talk_form()
        params["form"] = form
    return render(request, "myapp/talk_room.html",params)
    

def setting(request):
    return render(request, "myapp/setting.html")

class UserCreateView(CreateView):
    form_class = form_Customer
    template_name = 'myapp/signup.html'
    def post(self, request):
        if request.method =="POST":
            form=form_Customer(request.POST,request.FILES)
            if form.is_valid():
                print("form.is_valid")
                form.save()
                
                return render(request, "myapp/index.html") 
            else:
                return render(request,"myapp/signup.html", {"form": form})
        if request.method=="GET":
            form=form_Customer()
            return render(request,"myapp/signup.html",{"form":form})
class User_Confirmation(LoginView):
    form_class=loginform
    template_name='myapp/login.html'
    success_url = reverse_lazy('friends')
class User_Logout(LogoutView):
    form_class=logoutform
    template_name='myapp/index.html'

class User_PasswordChangeView(PasswordChangeView):
    form_class=password_changeform
    template_name="myapp/passchan.html"
    success_url=reverse_lazy('passwordchangedone')


def namechange(request):
    if request.method=="POST":
        form=Name_changeform(request.POST,instance=request.user)
        if form.is_valid():
           form.save()
           return redirect("namechangedone")
        else:
            print(form.errors) 
    if request.method=="GET":
        form=Name_changeform(instance=request.user)
        return render(request,"myapp/name_change.html",{"form":form})

def namechangedone(request):
    return render(request,"myapp/name_change_done.html")
def emailchange(request):
    if request.method=="POST":
        form=Email_changeform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('emailchangedone')
        else:
            print(form.errors)
    if request.method=="GET":
        form=Email_changeform(instance=request.user)
        return render(request,"myapp/mail_change.html",{"form":form})        
def emailchangedone(request):
    return render(request,'myapp/mail_change_done.html')
def imgchange(request):
    if request.method=="POST":
        form=Email_changeform(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('imgchangedone')
        else:
            print(form.errors)
    if request.method=="GET":
        form=Img_changeform(instance=request.user)
        return render(request,"myapp/img_change.html",{"form":form})
def imgchangedone(request): 
    return render(request,'myapp/img_change_done.html')   
    
class User_PasswordChangeViewDoneView(PasswordChangeDoneView):
    template_name="myapp/donepasschan.html"    

def lists(request):
    talking_user_list=CustomUser.objects.all().exclude(pk=request.user.pk)
    return render(request, 'myapp/friends.html',{'talking_user_list':talking_user_list})

    