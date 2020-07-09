from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup, name='signup'),
    path('userlogin/', views.login_view, name='userlogin'),
    path('userlogout/', views.logout_view, name='userlogout'),
    path('faqs/', views.faq, name='faqs'),
]