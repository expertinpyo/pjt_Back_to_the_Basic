from django.urls import path
from . import views

urlpatterns = [
    path('secret/<int:secret_pk>/', views.articles_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.like_article),

    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # path('<int:article_pk>/comments/<int:comment_pk>/like/', views.like_comment),
]