from django.urls import path

from post.views import post_create_view, post_list_view, post_detail_view, post_update_view, post_delete_view, \
    post_list_tag_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('detail/<slug:slug>', post_detail_view, name='post_detail'),
    path('create-post/', post_create_view, name='create_post'),
    path('update-post/<int:pk>', post_update_view, name='update_post'),
    path('delete-post/<slug:slug>', post_delete_view, name='delete_post'),
    path('tag/<slug:tag_slug>/', post_list_tag_view, name='tag_post'),
]
