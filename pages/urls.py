
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    #WhenusingClass-BasedViews,youalwaysaddas_view()
    path('', HomePageView.as_view(), name = "home"),
    path('about/', AboutPageView.as_view(), name='about'),
]