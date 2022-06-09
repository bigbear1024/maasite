from django.urls import path

from .models import Road
from . import views
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

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
    path('roads/', views.RoadListView.as_view(), name='roads'),
    path('references/', views.references, name='references'),
    path('roadmap/', TemplateView.as_view(template_name='roads.html'), name='roadmap'),
    path('data.geojson', GeoJSONLayerView.as_view(model=Road, properties=(
        'name', 'estimated_construction', 'actual_construction')), name='data'),
]
