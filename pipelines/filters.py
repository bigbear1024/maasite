from .models import Contact
import django_filters


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['company']
