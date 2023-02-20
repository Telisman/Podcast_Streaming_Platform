from django.urls import path
from .views import FAQ,contact_us


urlpatterns = [
    path('FAQ/', FAQ, name='faq'),
    path('contact_us/', contact_us, name='contact_us'),
]