from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

class Location(models.Model):       
    location = models.CharField(max_length=20)
    @classmethod
    def find_location(cls,location):
        location = cls.objects.filter(location = location).all()
        return location

class Category(models.Model):
    IMAGE_CATEGORIES = (
        ('travel',"Travel"),
        ('food',"Food"),
        ('places',"Places"),
        ('people','People'),
        ('sports','Sports'),
    )
    category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)

    @classmethod
    def search_by_category(cls,category):
        category = cls.objects.filter(category =category)
        return category
    
    @classmethod
    def find_category_id(cls,category):
        category = cls.objects.filter(category=category).all()
        return category

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'photos/' , default='default.jpg')
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default=22)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image

    @classmethod
    def days_photos(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

    def save_article(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    
    @classmethod
    def search_image(cls,category):
        cat_image = []
        for item in category:
            images = cls.objects.filter(category_id = item.id)
            cat_image.append(images)
        return cat_image

    @classmethod
    def filter_by_location(cls,location):

        images = cls.objects.all()
        location_images=[]

        for image in images:
            for location in location:
                if image.location_id == location.id:
                    location_images.append(image)
        
        return location_images

    @classmethod
    def copy_image_url(cls,image_id):
        image = cls.objects.filter(id=image_id)
        print(image[0].name)
        image_url = f'{settings.BASE_DIR}{image[0].image.url}'
        pyperclip.copy(image_url)


    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(pk=id)
        return image        

    def __str__(self):
        return self.title