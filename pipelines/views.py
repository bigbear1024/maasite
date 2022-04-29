from asyncio import tasks
from multiprocessing import context
from pipes import Template
from pyexpat import model
from re import template
from unittest import TestProgram
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contact, Meeting, Task, WebsiteLink
from django.views import generic
# Create your views here.


def index(request):
    last_meeting = Meeting.objects.all().order_by('-meeting_date')[:5]
    last_task = Task.objects.all().order_by('-id')[:5]
    context = {'last_meeting': last_meeting, 'last_task': last_task}
    return render(request, 'index.html', context=context)


def minutes(request):
    minutes = Meeting.objects.all().order_by('-id')
    return render(request, 'minutes.html', {'minutes': minutes})


class MeetingListView(generic.ListView):
    model = Meeting
    queryset = Meeting.objects.order_by('-meeting_date')
    paginate_by = 10


class MeetingDetailView(generic.DetailView):
    model = Meeting


class TaskLiskView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 10


class ContactDetailView(generic.DetailView):
    model = Task


def news(request):
    news_link = WebsiteLink.objects.filter(type='n')
    paginator = Paginator(news_link, 6)  # Show 6 links per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news_link': news_link, 'page_obj': page_obj})


def links(request):
    website_link = WebsiteLink.objects.filter(type='w')
    return render(request, 'links.html', {'website_link': website_link})
