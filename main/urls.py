from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),

    path('type/c/', views.tc),
    path('type/<int:tt>/u', views.tu),
    path('type/r/', views.tr),
    path('type/<int:_id>/d', views.td),

    path('link/s/', views.ls),
    path('link/c/', views.lc),
    path('link/<int:tt>/u', views.lu),
    path('link/r/', views.lr),
    path('link/<int:_id>/d', views.ld)
]
