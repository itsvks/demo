from django.conf.urls import patterns, url
from app import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^books/?$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/?$', views.BookDetail.as_view()),
    url(r'^authors/?$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/?$', views.AuthorDetail.as_view()),
)
