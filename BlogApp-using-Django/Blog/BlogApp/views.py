import re
from django.shortcuts import render,redirect
from matplotlib.style import use
from urllib3 import HTTPResponse
from BlogApp.models import Posts,Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth
from datetime import date
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.user.is_authenticated: 
        return redirect('/blogs')
    return render(request, 'home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/blogs')
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/blogs')
    return render(request, 'signup.html')

def blogs(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        posts = Posts.objects.all().order_by('id')
        author = Author.objects.all()
        users = User.objects.all()
        
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blogs.html',{"posts":page_obj, "users":users})

def signedup(request):
    if request.method == "POST":
        try: 
            user = User.objects.get(username = request.POST['username'] )
            return render(request,"signup.html",{'messages' : "User has already registered"})
        except User.DoesNotExist:

            if len(request.POST['password']) <8:
                return render(request,"signup.html", {'messages':'Password should be greater than 8 characters'})
            else:
                user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'] , password = request.POST['password'])
                auth.login(request, user)
                return redirect('/login')
    else:
        return redirect('/signup')
    return redirect('/signup')


def loggedin(request):
    if request.method == 'POST':
        user = request.POST['username']
        pswd = request.POST['password']
        
        users = auth.authenticate(username = user, password = pswd)

        if users is not None:
            auth.login(request,users)
            return redirect("/blogs")
        else:
            return render(request, "login.html", {'messages':'Invalid Credentials'})
    return redirect('/login')
        

def logout(request):
    auth.logout(request)
    return redirect("/login")


def addpost(request):
    return render(request, 'addpost.html')

def postadded(request):
    if request.method == "POST":
        blogtitle = request.POST['blogtitle']
        content = request.POST['content']
        post_date = date.today()

        post = Posts(blog_title=blogtitle, content=content, post_date=post_date, username=request.user)
        post.save()
        return redirect('/blogs')
    return render(request, 'addpost.html')

def showpost(request, id):
    posts = Posts.objects.filter(id=id)
    return render(request, 'showpost.html', {"posts":posts[0]})



def yourposts(request):
    posts = Posts.objects.filter(username=request.user)
    return render(request, 'yourposts.html', {"posts":posts})

def updatepost(request, id):
    posts = Posts.objects.filter(id=id)
    return render(request, 'updatepost.html', {"posts":posts[0]})

def updatedone(request, id):
    blogtitle = request.POST['blogtitle']
    content = request.POST['content']
    posts = Posts.objects.filter(id=id).update(blog_title= blogtitle, content = content)
    return redirect('/yourposts')


def aboutauthor(request):
    author = Author.objects.filter(authorname=request.user)
    if len(author) != 0:
        return render(request, 'aboutauthor.html',{"bio" : author[0]})
    else:
            return render(request, 'aboutauthor.html')

def updatebio(request):
    author = Author.objects.filter(authorname=request.user)
    if len(author)!=0:
        return render(request, 'bioform.html',{"bio" : author[0]})
    else:
        return render(request, 'bioform.html')
def bioupdated(request):
    if request.method == "POST":
        about = request.POST['aboutauthor']

        author = Author.objects.filter(authorname=request.user)
        if len(author) !=0:
            author = Author.objects.filter(authorname=request.user).update(about= about)
            return redirect("/aboutauthor")
            
        else:

            author = Author(about = about, authorname = request.user)
            author.save()
            return redirect("/aboutauthor")
    return redirect("/updatebio")

def userbio(request,name):
    author = Author.objects.filter(authorname=name)
    if len(author)!=0:
        return render(request, 'userbio.html',{"bio" : author[0]})
    else:
        return render(request, 'userbio.html')


def deletepost(request, id):
    posts = Posts.objects.filter(id=id).delete()
    return redirect('/yourposts')