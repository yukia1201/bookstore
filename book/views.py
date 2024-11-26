from django.shortcuts import render
from django.http.response import HttpResponse

from book.models import book
# Create your views here.

def index(request):
    # return HttpResponse("書名列表...")
    return render(request, 'index.html')

def harrypotter(request):
    # return HttpResponse("我是哈利波特")

    user = {'name':'devin', 'age':25, 'place':'高雄'}
    return render(request, "harrypotter.html", user)

def lordofring(request):
    # return HttpResponse("我是魔戒~!")
    user = {'name':'Wenzao', 'age':35, 'place':'台北'}
    return render(request, 'lordofring.html', user)

def janeeyre(request):
    return render(request, 'janeeyre.html')
