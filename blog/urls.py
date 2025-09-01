from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"), #localhost:8000/
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>/", views.post_detail, name="post-detail-page") #posts/mi_primer_post
]
