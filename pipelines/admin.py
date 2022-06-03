from csv import list_dialects
from dataclasses import field, fields
from multiprocessing import Event
from pyexpat import model
from statistics import mode
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company, Contact, Department, Road, Task, Meeting, WebsiteLink, Project, Milestone, Reference


class ContactInline(admin.StackedInline):
    model = Contact


class DepartmentInline(admin.TabularInline):
    model = Department


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'number')
    fields = [('name', 'number')]
    inlines = [DepartmentInline, ContactInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    autocomplete_fields = ['company', 'road',
                           'host', 'contact_person', 'project']
    list_display = ('subject', 'meeting_date', 'notification_no',
                    'notification_date', 'issue_no', 'issue_date', 'company_display')
    fieldsets = ((None, {'fields': ('meeting_date', 'subject', 'project', 'notification_date', 'notification_no',
                 'company', 'host', 'contact_person', 'road', 'agenda')}), ('會議記錄', {'fields': ('issue_no', 'issue_date', 'minutes', 'minutes_file',  'keynote_file', 'photo')}),)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    autocomplete_fields = ['company', 'road']
    list_display = ('number', 'subject', 'date',
                    'company_display', 'road_display')


@admin.register(WebsiteLink)
class WebsiteLinkAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('name', 'link', 'type')


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('number', 'name', 'zone', 'width', 'location', 'estimated_construction', 'actual_construction',
                    'estimated_completion', 'actual_completion')


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'completion_date')


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
