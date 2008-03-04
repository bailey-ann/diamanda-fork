#!/usr/bin/python
# Diamanda Application Set
# Pages module

from datetime import datetime, timedelta

from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic.list_detail import object_list
from django import newforms as forms

from boxcomments.models import Comment
from pages.models import *
from userpanel.models import Profile
from myghtyboard.models import Topic
from translator.models import Translation

def show_index(request):
	"""
	Show the main page
	"""
	itopics = Topic.objects.all().values('id', 'topic_name', 'topic_last_pagination_page', 'topic_lastpost').order_by('-topic_modification_date')[:4]
	for t in itopics:
		lastposter = str(t['topic_lastpost'])
		br = lastposter.find('<br />')
		t['last'] = lastposter[:br]
	entries = Content.objects.all().order_by('-date')[:5]
	com = Comment.objects.order_by('-id')[:5]
	now = datetime.now()
	check_time = now - timedelta(hours=1)
	onsite = Profile.objects.filter(onsitedata__gt=check_time).order_by('-onsitedata')[:5]
	tra = Translation.objects.order_by('-id').values('id', 'name')[:4]
	return render_to_response(
		'pages/show_index.html',
		{'slug': 'index', 'entries': entries, 'itopics': itopics, 'com': com, 'onsite': onsite, 'tra':tra},
		context_instance=RequestContext(request))

def list_news(request, book=False):
	"""
	List news
	
	* book - slug of a Content entry (book content_type)
	"""
	if book:
		bk = Content.objects.get(slug=book)
		news = Content.objects.filter(content_type='news', place=bk).order_by('-date').values('slug', 'title', 'date')
		return object_list(
			request,
			news,
			paginate_by = 10,
			allow_empty = True,
			template_name = 'pages/news_list.html',
			extra_context = {'book': book, 'bk':bk})
	else:
		news = Content.objects.filter(content_type='news').order_by('-date').values('slug', 'title', 'date')
	return object_list(
		request,
		news,
		paginate_by = 10,
		allow_empty = True,
		template_name = 'pages/news_list.html',
		extra_context = {'book': book})

def show(request, slug):
	"""
	show Content entry
	
	* slug - slug of a Content entry
	"""
	try:
		page = Content.objects.select_related().get(slug=slug)
	except Content.DoesNotExist:
		return render_to_response('pages/bug.html', {'bug': _('Page does not exist')}, context_instance=RequestContext(request))
	crumb = ''
	a = page
	if a.place:
		while a:
			crumb = '<a href="/w/p/' + a.place.slug + '/">' + a.place.title + '</a> > ' + crumb
			a = a.place
			if not a.place:
				a = False
	if page.content_type == 'news':
		return render_to_response(
			'pages/show_news.html',
			{'page': page, 'slug': slug, 'crumb': crumb[:-3], 'com': Comment.objects.filter(apptype= 1, appid = page.id).count()},
			context_instance=RequestContext(request))
	return render_to_response(
		'pages/show.html',
		{'page': page, 'slug': slug, 'crumb': crumb[:-3], 'com': Comment.objects.filter(apptype= 1, appid = page.id).count()},
		context_instance=RequestContext(request))

def sitemap(request):
	"""
	Sitemap generator
	"""
	pages = Content.objects.values('slug', 'date', 'content_type')
	for p in pages:
		p['date'] = str(p['date'])[0:10]
	return render_to_response('pages/sitemap.html', {'pages': pages}, context_instance=RequestContext(request))

def full_rss(request):
	"""
	RSS channel
	"""
	pages = Content.objects.all().values('slug', 'title', 'description', 'date', 'content_type').order_by('-id')[:10]
	return render_to_response('pages/rss2.html', {'pages': pages}, context_instance=RequestContext(request))

def book_rss(request, slug):
	"""
	RSS channel for a book
	
	* book - slug of a Content entry (book content_type)
	"""
	book = Content.objects.get(slug=slug)
	pages = Content.objects.all().filter(place=book).values('slug', 'title', 'description', 'date', 'content_type').order_by('-id')[:10]
	return render_to_response('pages/rss1.html', {'pages': pages, 'book': book}, context_instance=RequestContext(request))

def search_pages(request):
	"""
	Search view
	"""
	if request.POST:
		data = request.POST.copy()
		return render_to_response('pages/search.html', {'term': data['term'], 'key': settings.GOOGLE_AJAX_SEARCH_API_KEY}, context_instance=RequestContext(request))
	else:
		return render_to_response('pages/search.html', {'key': key}, context_instance=RequestContext(request))