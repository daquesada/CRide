"""users URLs"""
#django
from django.urls import path,include

#views 
from cride.users.views import UserLoginApiView

urlpatterns = [
    path('users/login/',UserLoginApiView.as_view(),name='login')
]