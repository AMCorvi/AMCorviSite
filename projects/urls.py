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
from django.conf.urls import url
from django.contrib import admin


from .views import IndexView, ProjectView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', ProjectView.as_view(), name="project")
#    url(r'^d_three$', views.d_three, name="d_three"),
#    url(r'^ots$', views.on_the_scene, name="on_the_scene"),
#    url(r'^$yeller$', views.yeller, name="yeller"),
#    url(r'^nodetalk$', views.node_talk, name="node_talk"),
#    url(r'^communion$', views.communion, name="communion"),
#    url(r'^blog$', views.blog, name="blog")
]
