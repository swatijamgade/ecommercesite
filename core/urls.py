from django.urls import path
from core.panties import index, about, contact, fruit, testimonial



app_name = "core"

urlpatterns = [

    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("fruit/", fruit, name='fruit'),
    path("testimonial/", testimonial, name='testimonial'),
]