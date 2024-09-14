from rest_framework import serializers
from ...models import product , comment, Category

class Categoryserializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Category.objects.all())
    class Meta:
        model = Category
        fields = ['name']

class Postserializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Category.objects.all())

    class Meta:
        model = product
        fields = ['id','category','title','description','Discoust']
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['category'] = Categoryserializer(instance.category).data
    #     return rep

class commentserializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['id','pro','name'   ,'likes','status' ,'created_date']
