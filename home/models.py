from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return  "{}".format(self.name)


class product(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    image = models.ImageField(upload_to='products/',default='products/product-1.png')
    # category = models.ManyToManyField(category)
    title = models.CharField(max_length=255)
    tags =TaggableManager()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.FloatField(default=0)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_date']
        verbose_name = "محصول"
        verbose_name_plural = "محصولات "
    def __str__(self):
        return  "{} - {}".format(self.title,self.status)

    def get_absolute_url(self):
        return reverse('blog:product_view',kwargs={'pid':self.id})

class comment (models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL ,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_date']
        verbose_name = "کامنت"
        verbose_name_plural ="کامنت ها"

    def __str__(self):
        return  "{} - {}".format(self.title,self.status)

class Categorys (models.Model):
     name = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
     image = models.ImageField(upload_to='products/',default='products/product-1.png')
     Discoust =models.IntegerField(default=0)
     def __str__(self):
         return  " {}".format(self.name)
class contact (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephon = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name = "پیغام"
        verbose_name_plural ="پیغام ها"

    def __str__(self):
        return  "{} - {}".format(self.title,self.name)
class newsletter (models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name = "ایمیل"
        verbose_name_plural ="ایمیل ها"

    def __str__(self):
        return  "-> {}".format(self.email)
