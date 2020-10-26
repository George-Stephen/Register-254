"""member URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import Member_list,New_members,Search_member,New_Order,Order_List



urlpatterns = [
     url(r'^api/member/search',Search_member.as_view(),name="user-projects"),
    url(r'^admin/', admin.site.urls),
    url(r'^api/members',Member_list.as_view()),
    url(r'^api/member/new',New_members.as_view()),
    url(r'^api/orders',Order_List.as_view()),
    url(r'^api/order/new',New_Order.as_view())
]
