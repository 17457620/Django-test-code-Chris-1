from django.contrib import admin
from django.urls import path, include 
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#the +static(...) line allows us to upload images

#Git Bash virtual environment resume
#cd /c/ecom/ecom
#source virt/Scripts/activate
#python manage.py runserver