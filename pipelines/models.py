from distutils.command.upload import upload
import email
from email.policy import default
from operator import mod
from pydoc import locate
from pyexpat import model
from re import T
import re
from statistics import mode
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.contrib import admin
from datetime import date
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="單位")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "單位"
        verbose_name_plural = "單位"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=False, null=True,
                            blank=True, verbose_name="部門")
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="單位")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部門"
        verbose_name_plural = "部門"


class Road(models.Model):
    name = models.CharField(max_length=10, null=True,
                            blank=True, verbose_name="道路名稱")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "道路清單"
        verbose_name_plural = "道路清單"


class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name="單位")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,
                                   blank=True, verbose_name="部門")
    name = models.CharField(max_length=10, verbose_name="名字")
    tel = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="電話")
    mobile = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="手機")
    email = models.EmailField(
        max_length=70, blank=True, null=True, verbose_name="信箱")
    note = models.TextField(max_length='500', null=True,
                            blank=True, verbose_name="備註")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "聯絡人"
        verbose_name_plural = "聯絡人"


class Meeting(models.Model):
    meeting_date = models.DateField(default=date.today, verbose_name="開會日期")
    subject = models.CharField(max_length=40, verbose_name="會議名稱")
    notification_date = models.DateField(
        default=date.today, verbose_name="通知單日期")
    notification_no = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="通知單文號")
    company = models.ManyToManyField(
        Company, verbose_name="與會單位")
    host = models.ForeignKey(Contact, related_name='host', on_delete=models.SET_NULL, null=True,
                             blank=True, verbose_name="主持人")
    contact_person = models.ForeignKey(Contact, related_name='contact_person', on_delete=models.SET_NULL, null=True,
                                       blank=True, verbose_name="聯絡人")
    road = models.ForeignKey(Road, on_delete=models.SET_NULL, null=True,
                             blank=True, verbose_name="地點")
    agenda = models.TextField(null=True, blank=True, verbose_name="議題")
    minutes = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name="會議記錄")
    summary = models.TextField(
        max_length=500, null=True, blank=True, verbose_name="摘要")
    issue_no = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="會議記錄文號")
    issue_date = models.DateField(default=date.today, verbose_name="會議記錄發文日期")
    minutes_file = models.FileField(
        upload_to="media/meeting/file/", null=True, blank=True, verbose_name="會議記錄上傳")
    sign_file = models.FileField(
        upload_to="media/meeting/sign/", null=True, blank=True, verbose_name="簽到表上傳")
    keynote_file = models.FileField(
        upload_to="media/meeting/keynote/", null=True, blank=True, verbose_name="簡報上傳")
    other_file = models.FileField(
        upload_to="media/meeting/other/", null=True, blank=True, verbose_name="附件上傳")
    photo = models.ImageField(
        upload_to="media/meeting/photo/", null=True, blank=True, verbose_name="照片上傳")

    class Meta:
        verbose_name = "行事曆"
        verbose_name_plural = "行事曆"

    def company_display(self):
        return '、'.join([company.name for company in self.company.all()])
    company_display.short_description = '相關單位'

    def get_absolute_url(self):
        return reverse('meeting-detail', args=[str(self.id)])

    def __str__(self):
        return self.subject


class Task(models.Model):
    subject = models.ForeignKey(
        Meeting, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="名稱")
    content = models.TextField(max_length=1000, blank=True, verbose_name="內容")
    date = models.DateField(default=date.today, verbose_name="預計完成日期")
    company = models.ManyToManyField(
        Company, verbose_name="相關單位")
    road = models.ManyToManyField(
        Road, verbose_name="影響道路")

    class Meta:
        verbose_name = "待辦清單"
        verbose_name_plural = "待辦清單"

    def company_display(self):
        return '、'.join([company.name for company in self.company.all()])
    company_display.short_description = '相關單位'

    def road_display(self):
        return '、'.join([road.name for road in self.road.all()])
    road_display.short_description = '影響道路'

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.subject.subject)
