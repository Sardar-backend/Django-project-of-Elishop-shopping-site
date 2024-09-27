from django.db import models
from project import settings
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
import json
# class Rating(models.IntegerChoices):
#     ONE_STAR = 1, 'One Star'
#     TWO_STARS = 2, 'Two Stars'
#     THREE_STARS = 3, 'Three Stars'
#     FOUR_STARS = 4, 'Four Stars'
#     FIVE_STARS = 5, 'Five Stars'

# class Garanti(models.TextChoices):
#     ONE_STAR = 1, 'بدون گارنتی '
#     TWO_STARS = 2, 'Two Stars'
#     THREE_STARS = 3, 'Three Stars'

class Warranty(models.TextChoices):
    WITHOUT_WARRANTY = 'no_warranty', 'بدون گارانتی'
    SIX_MONTHS = 'six_months', 'شش ماهه'
    ONE_YEAR = 'one_year', 'یک ساله'



class Color(models.Model):
    name = models.CharField(max_length=255)
    EnglishName = models.CharField(max_length=255)
    def __str__(self):
        return  "{}".format(self.name)
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorys/',default='categorys/422.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('home:pros',kwargs={'cat_name':self.name})


class product(models.Model):

    image = models.ImageField(upload_to='products/',default='products/product-1.png')
    # category = models.ManyToManyField(category)
    title = models.CharField(max_length=255)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=1)
    # garanti = models.TextChoices(choices=Warranty.choices , default=Warranty.WITHOUT_WARRANTY )
    warranty = models.CharField(max_length=20, choices=Warranty.choices, default=Warranty.WITHOUT_WARRANTY)
    # tags =TaggableManager()
    code = models.CharField(max_length=255,null=True)
    brand= models.CharField(max_length=255,null=True)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    #stars = models.IntegerField(choices=Rating.choices,validators=[MinValueValidator(1), MaxValueValidator(5)],default=Rating.THREE_STARS)
    price = models.FloatField(default=0)
    Discoust =models.IntegerField(default=0)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    color=models.ManyToManyField(Color, blank=True)
    count= models.IntegerField(default=0)
    Ready_to_send = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_date']
        verbose_name = "محصول"
        verbose_name_plural = "محصولات "
    def __str__(self):
        return  "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('blog:product_view',kwargs={'pid':self.id})
class ProductAttribute(models.Model):
    product = models.ForeignKey(product, related_name='attributes', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)  # نام ویژگی (مثلا: رنگ، سایز)
    value = models.CharField(max_length=255)  # مقدار ویژگی (مثلا: قرمز، 42)

    def __str__(self):
        return f'{self.key}: {self.value}'

class CustomUser(AbstractUser):
    # age = models.IntegerField(null=True, blank=True)
    # bio = models.TextField(null=True, blank=True)
    favorites = models.ManyToManyField(product,blank=True)

    phone = models.IntegerField(null=True, blank=True)
    meli = models.IntegerField(null=True, blank=True)
    card = models.CharField(null=True, blank=True , max_length=255)
    image =models.ImageField(upload_to='UserProfile/',default='categorys/422.jpg')
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='customuser_set',  # تغییر نام رابطه معکوس
    #     blank=True
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='customuser_set',  # تغییر نام رابطه معکوس
    #     blank=True
    # )


class comment (models.Model):
    pro = models.ForeignKey(product, on_delete=models.SET_NULL ,null=True)
    name =models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    cost= models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    Innovation = models.IntegerField(default=0)
    beauty = models.IntegerField(default=0)
    Services = models.IntegerField(default=0)
    Longevity = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_date']
        verbose_name = "کامنت"
        verbose_name_plural ="کامنت ها"

    def __str__(self):
        return  "{} - {}".format(self.title,self.status)

    def get_absolute_url(self):
        return reverse('home:comment_view',kwargs={'id':self.id})


class contact (models.Model):
    name =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.TextField(null=True,default=None)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name = "پیغام"
        verbose_name_plural ="پیغام ها"

    def __str__(self):
        return  "{}     {} ".format(self.name,self.answer)



class Order (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL ,null=True)
    order_number = models.CharField(max_length=255)
    Amount_payable = models.IntegerField(default=0)
    Amount_total = models.IntegerField(default=0)
    Order_registration_date = models.DateTimeField(auto_now_add=True)
    Order_delivery_time = models.DateTimeField(default=None)
    class Meta:
        ordering = ['Order_registration_date']
        verbose_name = "سفارش"
        verbose_name_plural ="سفارشات"

    def __str__(self):
        return  "{} - {}".format(self.user,self.order_number)


class adresses (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL ,null=True)
    recipient_name = models.CharField(max_length=255)
    ostan = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    mobile_recver = models.IntegerField(default=0)
    Postal_code = models.IntegerField(default=0)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name = "آدرس"
        verbose_name_plural ="آدرس ها"

    def __str__(self):
        return  "{} - {}".format(self.recipient_name,self.user)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
