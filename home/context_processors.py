from home.models import  Category , contact
def add_category_to_context(request):
    return {'categoryList':list (Category.objects.all()),'url':request.get_full_path()}
