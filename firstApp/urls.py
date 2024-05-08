from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/<str:name>", views.catalog, name="catalog"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("registr/", views.registr, name="registr"),
    path("login_User/", views.login_User, name="login_User"),
    path("profile/", views.profile, name="profile"),
    path("productCart/<int:id>/<str:name>", views.productCart, name="productCart"),
    path('remove_favorite/<int:id>', views.remove_favorite, name='remove_favorite'),
    path('search', views.search, name="search"),
    path("logout", views.logoutView, name="account_logout"),
    path("newsPost/<int:id>/<str:title>", views.newsPost, name="newsPost"),
#прочие urls
    path("company/", views.company, name="company"),
    path("services/", views.services, name="services"),
    path("serviceRepair/", views.serviceRepair, name="serviceRepair"),
    path("wholesale/", views.wholesale, name="wholesale"),
    path("faq/", views.faq, name="faq"),
]
