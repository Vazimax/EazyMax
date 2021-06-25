from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

appname= 'accounts'

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('jobs/',include('jobs.urls'),name="jobs"),
    path('contact/',include('contact.urls'),name="contact"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

