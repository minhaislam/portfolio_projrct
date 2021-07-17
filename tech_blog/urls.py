from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import tech_blog

urlpatterns = [
    path('hello/',views.hello)

]