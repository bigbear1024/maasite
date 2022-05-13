from asyncio import tasks
from multiprocessing import context
from pipes import Template
from pyexpat import model
from re import template
from unittest import TestProgram
from urllib import request
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contact, Meeting, Milestone, Road, Task, WebsiteLink
from django.views import generic
from .filters import ContactFilter, MeetingFilter


def index(request):
    last_meeting = Meeting.objects.all().order_by('-meeting_date')[:5]
    last_task = Task.objects.all().order_by('number')[:5]
    context = {'last_meeting': last_meeting, 'last_task': last_task}
    return render(request, 'index.html', context=context)


def minutes(request):
    minutes = Meeting.objects.all().order_by('-id')
    return render(request, 'minutes.html', {'minutes': minutes})


class MeetingListView(generic.ListView):
    model = Meeting
    queryset = Meeting.objects.order_by('-meeting_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MeetingFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class MeetingDetailView(generic.DetailView):
    model = Meeting


class TaskLiskView(generic.ListView):
    model = Task
    queryset = Task.objects.order_by('-number')
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class ContactListView(generic.ListView):
    model = Contact
    ordering = ('company__number',)
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ContactFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class ContactDetailView(generic.DeleteView):
    model = Contact


# def contacts(request):
#     contacts = Contact.objects.all()
#     contact_filter = ContactFilter(queryset=contacts)
#     paginator = Paginator(contacts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     if request.method == "POST":
#         contact_filter = ContactFilter(request.POST, queryset=contacts)
#     context = {'contact_filter': contact_filter}
#     return render(request, 'contacts.html', context)


def news(request):
    news_link = WebsiteLink.objects.filter(type='n')
    paginator = Paginator(news_link, 6)  # Show 6 links per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news_link': news_link, 'page_obj': page_obj})


def links(request):
    website_link = WebsiteLink.objects.filter(type='w')
    return render(request, 'links.html', {'website_link': website_link})


def milestones(request):
    milestones = Milestone.objects.all().order_by('name')
    return render(request, 'milestones.html', {'milestones': milestones})


def roads(request):
    roads = Road.objects.all().order_by('number')
    return render(request, 'roads.html', {'roads': roads})
