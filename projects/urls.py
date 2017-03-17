"""amcorvi_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from projects import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^d3$', views.d3, name="d3"),
#    url(r'^ots$', views.on_the_scene, name="on_the_scene"),
#    url(r'^$yeller$', views.yeller, name="yeller"),
#    url(r'^nodetalk$', views.node_talk, name="node_talk"),
#    url(r'^communion$', views.communion, name="communion"),
#    url(r'^blog$', views.blog, name="blog")
]
