from django.shortcuts import render,redirect
from .models import User,NotesDb
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.urls import reverse
from urllib.parse import urlencode
import os
# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'home.html')

@csrf_exempt
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if password == user.password:
            base_url = 'http://192.168.52.125:5030'  # 1 /<redirect-route>
            query_string = urlencode({'token': jwt.encode({'pass': password}, os.environ.get('SECRET_KEY'), algorithm='HS256')})
            url = '{}?{}'.format(base_url, query_string)
            print(url)
            return HttpResponseRedirect(url)
    return redirect('/')
@csrf_exempt
def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(username=username,password=password)
        return redirect('/')
    return render(request,'signup.html')

def notes(request):
    for note in NotesDb.objects.all():
        print(note.title,note.content,note.created_at)
    return render(request,'notes.html')