from dataclasses import dataclass, field, fields
from pyexpat import model
from tabnanny import verbose
from .models import Contact, Meeting, Road
import django_filters


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['company']


class MeetingFilter(django_filters.FilterSet):
    meeting_year = django_filters.NumberFilter(
        field_name='meeting_date', lookup_expr='year', label='年份（西元）')
    meeting_month = django_filters.NumberFilter(
        field_name='meeting_date', lookup_expr='month', label='月份')

    class Meta:
        model = Meeting
        fields = ['meeting_year', 'meeting_month',
                  'project', 'company']


class RoadFilter(django_filters.FilterSet):
    estimated_construction_year = django_filters.NumberFilter(
        field_name='estimated_construction', lookup_expr='year', label='預計施工日-年份（西元）')
    estimated_construction_month = django_filters.NumberFilter(
        field_name='estimated_construction', lookup_expr='month', label='預計施工日-月份')
    estimated_completion_year = django_filters.NumberFilter(
        field_name='estimated_completion', lookup_expr='year', label='預計完工日-年份（西元）')
    estimated_completion_month = django_filters.NumberFilter(
        field_name='estimated_completion', lookup_expr='month', label='預計完工日-月份')

    class Meta:
        model = Road
        fields = ['zone']
