from django.conf.urls import   url
from . import views
from django.views.generic import TemplateView

# from myapplibrary.views import ConnectionView
urlpatterns = [
        url(r'^$', views.home, name='home'),
        # #url(r'^$', views.index, name='index'),
        # url(r'^morning$', views.morning, name='morning'),
        # url(r'^hello_with_parameter$', views.hello_with_parameter, name='hello_with_parameter'),
        # url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
        # url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name = 'articles'),
        # url(r'^sendEmail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', views.sendEmail , name = 'sendEmail'),
        # url(r'^login/', views.login, name = 'login'),
        # url(r'^connection/', views.connection, name = 'connection'),
]
