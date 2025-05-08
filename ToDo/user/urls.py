from django.contrib.auth import views as auth_views
from django.urls import path
import user.views as views


urlpatterns = [
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user, name='login_user'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register_user'), name='logout_user')

]