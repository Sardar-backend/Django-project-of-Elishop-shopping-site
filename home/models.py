from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return  "{}".format(self.name)


class product(models.Model):
    # author = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    image = models.ImageField(upload_to='products/',default='products/product-1.png')
    # category = models.ManyToManyField(category)
    title = models.CharField(max_length=255)
    # tags =TaggableManager()
    brand= models.CharField(max_length=255,null=True)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.FloatField(default=0)
    Discoust =models.IntegerField(default=0)
    counted_view = models.IntegerField(default=0)
    favorites = models.ManyToManyField(User)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
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

class comment (models.Model):
    pro = models.ForeignKey(product, on_delete=models.SET_NULL ,null=True)
    name =models.CharField(max_length=255,default=None)
    title = models.CharField(max_length=255)
    content = models.TextField()
    cost= models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    Innovation = models.IntegerField(default=0)
    beauty = models.IntegerField(default=0)
    Services = models.IntegerField(default=0)
    Longevity = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
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
     def __str__(self):
         return  " {}".format(self.name)
class contact (models.Model):
    #name = models.CharField(max_length=255)
    name =  models.ForeignKey(User, on_delete=models.CASCADE)
    # email = models.EmailField()
    # telephon = models.IntegerField(default=0)
    # title = models.CharField(max_length=255)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
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












class newsletter (models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name = "ایمیل"
        verbose_name_plural ="ایمیل ها"

    def __str__(self):
        return  "-> {}".format(self.email)
