from django.urls import path
import user.views as views

urlpatterns = [
    path('register', views.register_user, name='user_register'),
    path('login', views.login_user, name='token_obtain_pair'),
    path('profile', views.get_user_profile, name='user_profile'),
]