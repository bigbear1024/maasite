from import_export import resources
from .models import Company, Contact


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
