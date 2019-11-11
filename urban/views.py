from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from . models import Article, Category
from django.http  import HttpResponse

# Create views here.
def welcome(request):
    date = dt.date.today()
    image = Article.todays_photos()
    return render(request, 'all-photos/todays-photos.html', {"date": date,"image":image})
    
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        category = Category.find_category_id(search_term)
        searched_images = Article.search_image(category)
        message = f"{search_term}" 
        return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message = "No results."
        return render(request, 'search.html',{"message":message})