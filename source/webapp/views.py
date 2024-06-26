from urllib import request

from django.shortcuts import render, redirect

from webapp.artcile_db import ArticleDb
from webapp.models import Cat


# Create your views here.
def start(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        if name:
            cat = Cat(name=name)
            ArticleDb.add_cat(cat)
            request.session['cat_name'] = name
            return redirect('cat_info')
    return render(request, 'start.html')

def cat_info(request):
    cat_name = request.session.get('cat_name')
    if not cat_name:
        return redirect('start')

    cat = ArticleDb.get_cat(cat_name)
    if not cat:
        return redirect('start')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
        return redirect('cat_info')

    return render(request, 'cat_info.html', {'cat': cat})



