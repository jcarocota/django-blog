from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"), #localhost:8000/
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>/", views.SinglePostView.as_view(), name="post-detail-page") #posts/mi_primer_post
]
