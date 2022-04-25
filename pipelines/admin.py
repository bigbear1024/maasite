from csv import list_dialects
from dataclasses import field
from multiprocessing import Event
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company, Contact, Department, Road, Task, Meeting, WebsiteLink
# Register your models here.
admin.site.register(Company)
admin.site.register(Road)
# admin.site.register(Contact)
# admin.site.register(Meeting)
# admin.site.register(Task)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'company')


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('name', 'company', 'department',
                    'tel', 'mobile', 'email', 'note')
    fields = ['company', 'department', 'name',
              ('tel', 'mobile', 'email'), 'note']


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'meeting_date', 'notification_no',
                    'notification_date', 'summary', 'issue_no', 'issue_date', 'company_display')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date',
                    'company_display', 'road_display')


@admin.register(WebsiteLink)
class WebsiteLinkAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('name', 'link', 'type')
