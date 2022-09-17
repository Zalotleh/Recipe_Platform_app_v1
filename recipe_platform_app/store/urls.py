from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import *

app_name = 'store'

urlpatterns = [
                  path('', store_page, name='store_page'),
                  path('<slug:category_slug>', store_page, name='product_list_by_category'),
                  path('<int:id>/<slug:slug>', product_detail, name='product_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
