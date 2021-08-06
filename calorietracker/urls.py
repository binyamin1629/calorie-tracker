
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('article/<int:pk>', views.showArticle,name='showarticle'),
    path('accounts/', include('accounts.urls')),
    path('body-stats/', include('bodystats.urls')),
    path('diet-track/', include('meal.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
