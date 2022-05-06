from dataclasses import dataclass, field, fields
from pyexpat import model
from .models import Contact, Meeting
import django_filters


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['company']


class MeetingFilter(django_filters.FilterSet):
    class Meta:
        model = Meeting
        fields = ['meeting_date', 'project', 'company']
