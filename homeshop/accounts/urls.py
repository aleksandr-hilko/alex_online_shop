from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name="signout"),
    path('signup/', views.signup, name="signup"),
]
