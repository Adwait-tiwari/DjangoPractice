from.import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('login',views.LoginUser,name="login"),
    path('logout',views.LogoutUser,name="logout"),
    path('signup',views.SignupUser,name="signup"),
    path('api/home',views.home_api)
]
