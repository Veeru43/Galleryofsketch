from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('handcraft',views.handcraft,name='handcraft'),
    path('plant',views.plant,name='plant'),
    path('card',views.card,name='card'),  
    path('human',views.human,name='human'),
    path('building',views.building,name='building'),
    path('nature',views.nature,name='nature'),
]