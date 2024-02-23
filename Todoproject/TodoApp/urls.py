from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.Home,name='home'),
    path('bicycle/',views.bicycle,name='bicycle'),
    path('<slug:c_slug>/',views.bicycle,name='product_by_category'),
    path('details/<int:id>',views.Details,name='details'),

]
