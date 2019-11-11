from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from . models import Article
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    date = dt.date.today()
    image = Article.todays_photos()
    return render(request, 'all-photos/todays-photos.html', {"date": date,"image":image})

def photos_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY

    return render(request, 'all-photos/todays-photos.html', {"date": date,})

def past_days_photos(request,past_date):
        # Converts data from the string Url
        try:
        # Converts data from the string Url
            date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        except ValueError:
        # Raise 404 error when ValueError is thrown
            raise Http404()

        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        day = convert_dates(date)
        html = f'''
            <html>
                <body>
                    <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
                </body>
            </html>
                '''
        return HttpResponse(html)

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        category = Category.find_category_id(search_term)
        searched_images = Image.search_image(category)
        message = f"{search_term}" 


        return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message = "No results."
        return render(request, 'search.html',{"message":message})