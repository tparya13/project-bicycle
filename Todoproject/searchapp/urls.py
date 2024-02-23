from django.urls import path
from . import views
app_name='searchapp'
urlpatterns = [
    path('searchproduct/',views.SearchResult,name='searchproduct'),
]