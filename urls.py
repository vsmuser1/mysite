from django.urls import path

# importing views from views..py
from mini import views

urlpatterns = [
    path('simple',views.simple_view),
    path('condition', views.check_age),
    path('loop', views.loop),
]
