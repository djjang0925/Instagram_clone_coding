from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
]
