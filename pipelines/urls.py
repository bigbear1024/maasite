from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.MeetingListView.as_view(), name='meetings'),
    path('meeting/<int:pk>', views.MeetingDetailView.as_view(),
         name='meeting-detail'),
    path('tasks/', views.TaskLiskView.as_view(), name='tasks'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('minutes/', views.minutes, name='minutes'),
    path('news/', views.news, name='news'),
    path('links/', views.links, name='links'),
    path('milestones/', views.milestones, name='milestones'),
]
