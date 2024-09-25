from rest_framework import serializers
from ...models import product , comment, Category , Color , Order , contact
class Categoryserializer(serializers.ModelSerializer):
    # name = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Category.objects.all())
    class Meta:
        model = Category
        fields = ['name','image']

class commentserializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['id','pro','name','status','content' ,'created_date']
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


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields  = ['name','answer','content','created_date']
