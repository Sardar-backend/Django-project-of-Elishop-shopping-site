from rest_framework.pagination import PageNumberPagination
class Resultpagniton(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10000
