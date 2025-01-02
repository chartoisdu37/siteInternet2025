from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
)

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("", PostListView.as_view(), name='post_list'), # à revoir les adresses de ces 2 lignes
    path('new/', PostCreateView.as_view(), name='post_new')
]

