
from bot_cms_apiw import views
from bot_cms_apiw.restapi import router
from django.urls import path, include

urlpatterns = [
    path('', include(router.urls)),
    # path('create_file/',  views.create_file, name='create_file'),
    # path('update_file/', views.update_file, name='update_file'),
    # path('delete_file/', views.delete_file, name='delete_file'),
    #
    # path('create_folder/', views.create_folder, name='create_folder'),
    # path('update_folder/', views.update_folder, name='update_folder'),
    # path('delete_folder/', views.delete_folder, name='delete_folder'),

]
