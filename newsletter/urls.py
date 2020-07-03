from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from newsletter import views

from newsletter.views import email_list_signup


urlpatterns = [
    path('subscribe', email_list_signup, name='subscribe')
]
