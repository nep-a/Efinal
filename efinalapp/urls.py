from django.contrib import admin
from django.urls import path

from efinalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('agent/', views.agent, name='agent'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    path('community/', views.community, name='community'),
    path('service/', views.services, name='service'),

    path('home/', views.home, name='home'),
    path('book/<int:house_id>/', views.book_house, name='book_house'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('inquiry/', views.post_inquiry, name='post_inquiry'),
    path('base/', views.base, name='base'),

]
