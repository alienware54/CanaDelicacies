
from django.contrib import admin
from django.urls import path
from canaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('starter/', views.index, name='starter'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('chefs/', views.chefs, name='chefs'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations'),
    path('thanks/', views.thanks, name='thanks'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit /<int:id>', views.edit, name='edit'),
    path('update /<int:id>', views.update, name='update'),
    path('rooms/', views.rooms, name='rooms'),
    path('received/', views.received, name='received'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('cana/', views.cana, name='cana'),
    path('manager/', views.manager, name='manager'),
    path('make/', views.make, name='make'),

    #mpesa api url
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),




]
