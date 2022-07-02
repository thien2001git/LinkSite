from django.urls import path

from . import views

urlpatterns = [
    path('', views.to_html.index, name="index"),
    path('addlink/', views.xldl.add_link, name="addlink"),
    path('dem/<int:id>', views.xldl.dem, name="dem"),
    path('del-link/<int:id>', views.xldl.del_link, name="del-link"),
    path('del-type/<int:id>', views.xldl.del_type, name="del-type"),
    path('addtype/', views.xldl.add_type, name="add-type"),
    path('tk/', views.to_html.tk, name="tk"),


]
