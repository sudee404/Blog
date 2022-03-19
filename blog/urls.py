from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post-list'),
    path('post/new/',views.PostCreateView.as_view(), name='post-form'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(), name='post-remove'), 
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add-comment'),
    path('comment/<int:pk>/approve/',views.approve_comment,name='approve-comment'),
    path('comment/<int:pk>/remove/',views.remove_comment,name='remove-comment'),
    path('post/<int:pk>/publish',views.publish_post,name='post-publish') ,
    path('my-stories/',views.stories,name='stories'),
    path('signup/',views.signup,name='signup'),
]
