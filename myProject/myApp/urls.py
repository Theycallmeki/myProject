from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('navbar/', views.navbar, name='navbar'),
    path('logout/', views.user_logout, name='logout'), 
    path('create/', views.create, name='create'),  # Ad # Ad
    path('creates/', views.create_portfolio, name='create_portfolio'),
    path('edit/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
    path('portfolios/', views.portfolio_list, name='portfolio_list'),  # For function-based view
        path('ckeditor/upload/', views.upload_image, name='upload_image'),

    



]