from rest_framework import serializers
from ...models import product , comment, Category , Color , Order , contact ,adresses
class Categoryserializer(serializers.ModelSerializer):
    # name = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Category.objects.all())
    class Meta:
        model = Category
        fields = ['name','image']

class commentserializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['id','pro','name','status','content' ,'created_date']
        read_only_fields  =['status']
class Productserializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Category.objects.all())
    color = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Color.objects.all())
    # comments = serializers.SlugRelatedField(many=True,slug_field='content',queryset=comment.objects.all())
    comments = serializers.SerializerMethodField()  # استفاده از SerializerMethodField برای کامنت‌ها
    class Meta:
        model = product
        fields = ['id','category','title','description','Discoust','count','Ready_to_send','image','color','price','code','brand','warranty','counted_view','comments']
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = Categoryserializer(instance.category).data
        return rep
    def get_comments(self, obj):
        # واکشی کامنت‌های مرتبط با محصول
        comments = comment.objects.filter(pro=obj, status=True)
        return commentserializer(comments, many=True).data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields  = ['user','order_number','Amount_payable','Amount_total','Order_registration_date','Order_delivery_time']


class adressSerializer(serializers.ModelSerializer):
    class Meta:
        model = adresses
        fields  = ['user','recipient_name','ostan','city','Postal_code','content','created_date']


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields  = ['name','answer','content','created_date']

class contactcreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['content']

class CartSerializer(serializers.Serializer):
    # quantity = serializers.IntegerField()
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    discount = serializers.DecimalField(max_digits=5, decimal_places=2)
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2)
    product = Productserializer()
    # def to_representation(self, instance):
    #     # سریالایز کردن فیلدها
    #     data = super().to_representation(instance)
    #     # حذف فیلد product اگر مقدار نداشته باشد
    #     if 'product' in instance and instance['product'] is None:
    #         data.pop('product', None)
    #     return data
