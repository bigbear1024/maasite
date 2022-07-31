from distutils.command.upload import upload
import email
from email import charset
from email.policy import default
import numbers
from operator import mod, ne
from pydoc import locate
from pyexpat import model
from django.contrib import admin
from re import T
import re
from statistics import mode
from tabnanny import verbose
from turtle import width
from unicodedata import name
from django.db import models
from datetime import date
from django.urls import reverse
from tinymce import models as tinymce_models
from djgeojson.fields import LineStringField


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="單位名稱")
    number = models.CharField(max_length=4, null=True,
                              blank=True, verbose_name="分類編號")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('number',)
        verbose_name = "通訊錄"
        verbose_name_plural = "G.通訊錄"


class Department(models.Model):
    name = models.CharField(max_length=200, unique=False, null=True,
                            blank=True, verbose_name="部門")
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="單位")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部門"
        verbose_name_plural = "部門"


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

    class Meta:
        verbose_name = "聯絡人"
        verbose_name_plural = "聯絡人"


class Road(models.Model):
    number = models.CharField(max_length=20, null=True,
                              blank=True, verbose_name="編號")
    name = models.CharField(max_length=200, null=True,
                            blank=True, verbose_name="道路名稱")
    location = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="位置")
    coordinate = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="座標")

    zone = models.CharField(max_length=10, null=True,
                            blank=True, verbose_name="分區")
    width = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name="路寬")
    estimated_construction = models.DateField(
        default=date.today, null=True,
        blank=True, verbose_name="預計施工日")
    actual_construction = models.DateField(
        default=date.today, null=True,
        blank=True, verbose_name="實際施工日")
    estimated_completion = models.DateField(
        default=date.today, null=True,
        blank=True, verbose_name="預計完工日")
    actual_completion = models.DateField(
        default=date.today, null=True,
        blank=True, verbose_name="實際完工日")
    photo = models.ImageField(
        upload_to="media/road/photo", null=True, blank=True, verbose_name="照片")
    geom = LineStringField(null=True, verbose_name="繪製道路")

    class Meta:
        verbose_name = "計畫道路"
        verbose_name_plural = "E.計畫道路"

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            # 判斷有沒有圖片檔案，沒有這行會跳錯誤，找不到檔案
            return self.photo.url

    def __str__(self):
        return self.name


class Milestone(models.Model):
    name = models.CharField(max_length=200, verbose_name="里程碑")
    completion_date = models.DateField(default=date.today, verbose_name="完成日期")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "里程碑"
        verbose_name_plural = "D.里程碑"


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="專案項目")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "專案項目"
        verbose_name_plural = "C.專案項目"


class Meeting(models.Model):
    meeting_date = models.DateField(default=date.today, verbose_name="開會日期")
    subject = models.CharField(max_length=40, verbose_name="會議名稱")
    project = models.ManyToManyField(Project, blank=True, verbose_name="專案項目")
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
    minutes = tinymce_models.HTMLField(
        max_length=4000, null=True, blank=True, verbose_name="會議記錄")
    issue_no = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="會議記錄文號")
    issue_date = models.DateField(default=date.today, verbose_name="會議記錄發文日期")
    minutes_file = models.FileField(
        upload_to="media/meeting/file", null=True, blank=True, verbose_name="會議(勘)完整掃描檔上傳")
    keynote_file = models.FileField(
        upload_to="media/meeting/keynote", null=True, blank=True, verbose_name="簡報上傳")
    photo = models.ImageField(
        upload_to="media/meeting/photo", null=True, blank=True, verbose_name="照片上傳")

    class Meta:
        verbose_name = "行事曆"
        verbose_name_plural = "A.行事曆"

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
    content = tinymce_models.HTMLField(
        max_length=3000, blank=True, verbose_name="內容")
    date = models.DateField(default=date.today, verbose_name="預計完成日期")
    company = models.ManyToManyField(
        Company, verbose_name="相關單位")
    road = models.ManyToManyField(
        Road, blank=True, verbose_name="影響道路")
    number = models.CharField(max_length=8, null=True, verbose_name="編號")

    class Meta:
        verbose_name = "待辦清單"
        verbose_name_plural = "B.待辦清單"

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


class WebsiteLink(models.Model):
    name = models.CharField(max_length=100, verbose_name="標題")
    link = models.CharField(
        max_length=255, help_text='需包含https://', verbose_name="連結")
    summary = tinymce_models.HTMLField(
        max_length=1000, null=True, blank=True, verbose_name="摘要")
    LINK_TYPE = (('w', '相關網站'), ('n', '新聞媒體'),)
    type = models.CharField(max_length=1, choices=LINK_TYPE,
                            default='n', help_text='選擇網站種類', verbose_name="網站種類")

    class Meta:
        verbose_name = "網站連結"
        verbose_name_plural = "F.網站連結"

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=200, verbose_name="名稱")
    file = models.FileField(upload_to="media/reference/file/",
                            null=True, blank=True, verbose_name="檔案")

    class Meta:
        verbose_name = "參考資料"
        verbose_name_plural = "H.參考資料"

    def __str__(self):
        return self.name
