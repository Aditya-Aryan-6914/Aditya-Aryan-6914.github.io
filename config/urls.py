from django.urls import path
from portfolio import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/page/<int:page>/", views.blog_list, name="blog_page"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("blog/category/<slug:slug>/", views.blog_category, name="blog_category"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("search-index.json", views.search_index, name="search_index"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("feed.xml", views.feed, name="feed"),
    path("robots.txt", views.robots, name="robots"),
    path("ads.txt", views.ads_txt, name="ads_txt"),
    path("404.html", views.not_found, name="not_found"),
]
