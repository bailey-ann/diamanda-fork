from os import environ
environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from settings import *
from wiki.models import *
from myghtyboard.models import *

Cbc.objects.all().delete()
c = Cbc(tag='art', tag_example='[rk:art slug="SLUG_NAME"]', description='Will insert a link to a given page (by the given slug) using it title and description')
c.save()
c = Cbc(tag='h', tag_example='[rk:h id="1-4"]Title[/rk:h]', description='Will insert the given title in a H1-4 tag (as defined in the id attribute). Use this tags if you want to use Page Table of Contents generated by [toc]')
c.save()
c = Cbc(tag='link', tag_example='[rk:link href="URL" desc="DESCRIPTION"]TITLE[/rk:link]', description='Will insert a external link with nice icon. "desc" attribute is optional and if added will display a description text by the link.')
c.save()
c = Cbc(tag='syntax', tag_example='[rk:syntax lang="LANG"]CODE[/rk:syntax]', description='Will highlight the code using entered in the "lang" attribute scheme - python, xml, html, ruby, perl, lua, cpp, delphi, java, php, makefile, diff, javascript, css, sql.')
c.save()
c = Cbc(tag='thumb', tag_example='[rk:thumb src="image.jpg"] [rk:thumb src="folder/image.jpg"]', description='Will insert a link to a local image using a thumb and a pop-up. The thumb will be created by PIL. Images can be in SITE_IMAGES_DIR_PATH subfolders')
c.save()
c = Cbc(tag='lthumb', tag_example='[rk:lthumb src="image.jpg"] [rk:lthumb src="folder/image.jpg"]', description='Will insert a link to a local image using a thumb and lightbox JS widget. The thumb will be created by PIL. Images can be in SITE_IMAGES_DIR_PATH subfolders')
c.save()
c = Cbc(tag='topic', tag_example='[rk:topics forum="Forum_id"]', description='Will insert a list of 10 latest active topics from selected forum or from all forums if "forum attribute is set to 0')
c.save()
c = Cbc(tag='table', tag_example='''[rk:table name="tablea" width="50%" sort="'N', 'S', 'S'"]
field1|field2|fiel3
1|valuex|valuey
4|bar|text
2|tekx2|foo
[/rk:table]''', description='Will insert a table with row highlighting and column sorting. name - unique name for each table on the page, width - optional, default 100%, sort - defines sorting rules, S - string, N - number - for each column. Between tags you place the table structure, using | as a column separator. First row is the table head, the rest is the table data.')
c.save()


Page.objects.all().delete()
p = Page(title='Diamanda Wiki Main Page', slug='index', description='A description :)', text='''[rk:h id="1"]Diamanda Wiki SVN[/rk:h]
[toc]<br><br>

Diamanda (wiki and forum) is released under GPL License<br>
<b>Author</b>: Piotr Malinski - riklaunim@gmail.com | <a href="http://www.rkblog.rk.edu.pl">English support</a> | <a href="http://www.python.rk.edu.pl">Polskie Wsparcie</a><br>

<div class="notice">This applications is in developement and currently is in Beta stage.</div>
<br>
[rk:h id="2"]Features[/rk:h]
<b>WIKI</b>
<blockquote>
- add, Edit Pages with permission controll<br>
- full history support<br>
- diffs between all versions of a wikiPage<br>
- safe HTML markup and plugable ContentBBcode tags<br>
- multilingual interface (pl/en currently)<br>
- google sitemap generation<br>
- PDF export with htmldoc<br>
- bans<br>
- Task Management
</blockquote><br>
<b>MyghtyBoard Forum</b>
<blockquote>
- Add Topic/Post<br>
- Edit my posts<br>
- Permission controll, user cant post a new post after his post<br>
- IP, hostname saved<br>
- Nice themes :)<br>
- Lock/Open topics, sticky/global topics<br>
- Topics with my posts, My Topics, Last active Topics lists<br>
- Move Topics
</blockquote><br><br>

[rk:h id="2"]Requirements:[/rk:h]
- install <b>strip-o-gram</b> from <a href="http://www.zope.org/Members/chrisw/StripOGram" target="_blank">here</a> - its a safe HTML filter which is used in Diamanda WikiPages and forums.
<div class="box">python setup.py install</div>
will install it.<br>
- <b>pyGoogle</b>: optional, if you want to use Google Search API as an extra site search<br>
- <b>PIL - Python Imaging Library</b>: makes thumbs and Captcha<br><br>

[rk:h id="2"]Instalation:[/rk:h]
- edit urls.py and change the site_media path /home/piotr/diamanda/media to that on your computer:
<div class="box">(r^site_media/(.*)$, django.views.static.serve, {document_root: /path/here}),</div>

- create tables (sqlite3 by default):
<div class="box">python manage.py syncdb<br>
python install.py</div>
- create a superuser when creating tables!<br>

- run the dev server: python
<div class="box">manage.py runserver 8080</div>
<br>
<div class="note">- http://localhost:8080/ is the main wiki page<br>
- http://localhost:8080/forum/ is the main MyghtyBoard Forum page</div><br>

<div class="notice">Debug is set to True by default!</div>
<br><br>

[rk:h id="2"]MyghtyBoard[/rk:h]
MyghtyBoard is the name of the forum script which is in heavy developement right now but all the "basic" features
work nicely. Categories and Forums are managed by the Django Admin Panel. Staff members and superusers are forum moderators.
<br><br>

[rk:h id="2"]Extra settings in settings.py[/rk:h]
You will find at the end of the file:
[rk:syntax lang="python"]DQojIFJTUyBTZXR0aW5ncw0KU0lURV9OQU1FID0gJ0RpYW1hbmRhIFdpa2kgIScNClNJVEVfREVTQ1JJUFRJT04gPSAnQSBEaWFtYW5kYSBXaWtpIFNjcmlwdCcNClNJVEVfTkVXU19MSU5LID0gJy8nICMgd2hlcmUgbGlua3Mgb2YgdGhlIFJTUyBmZWVkcyBzaG91bGQgcG9pbnQNCg0KIyBBbm9ueW1vdXMgcGVybXMgU2V0dGluZ3MNCkFOT05ZTU9VU19DQU5fRURJVD1UcnVlDQpBTk9OWU1PVVNfQ0FOX0FERD1UcnVlDQpBTk9OWU1PVVNfQ0FOX1ZJRVc9VHJ1ZQ0KQU5PTllNT1VTX0NBTl9TRVRfQ1VSRU5UPUZhbHNlDQoNCiMgbXlnaHR5Ym9hcmQgY29uZmlnDQpBTk9OWU1PVVNfQ0FOX0FERF9UT1BJQz1UcnVlDQpBTk9OWU1PVVNfQ0FOX0FERF9QT1NUPVRydWUNCk1ZR0hUWUJPQVJEX1RIRU1FPSdhZW9sdXMnICMgdGhlbWUgbmFtZSwgY3VycmVuICJ3b3ciIGFuZCAiYWVvbHVzIg0KTVlHSFRZQk9BUkRfTEFORz0nZW5nbGlzaCcgIyBsYW5ndWFnZSBuYW1lIGZvciBpMThuIGdyYXBoaWNzICh0aGVtZSBtdXN0IGhhdmUgaW1hZ2VzIGZvciBzZWxlY3RlZCBsYW5ndWFnZQ0KDQojIHRodW1iIENCQw0KU0lURV9JTUFHRVNfRElSX1BBVEggPSAnL2hvbWUvcGlvdHIvZGlhbWFuZGEvbWVkaWEvaW1hZ2VzLycNClNJVEVfSU1BR0VTX1NSQ19QQVRIID0gJy9zaXRlX21lZGlhL2ltYWdlcy8nDQoNCiMgT3RoZXINClVTRV9CQU5TID0gRmFsc2UgIyB1c2UgV0lraUJhbnMgdG8gcHJldmVudCBiYW5lZCBmcm9tIGFkZC9lZGl0IGFjdGlvbnMNCg==[/rk:syntax]
- RSS settings are used when generating RSS Feeds, SITE_NEWS_LINK doesnt require any changes, the rest can be edited.<br>
- Anonymous Permissions: True/False<br>
- USE_BANS - if True the Wiki Ban module (see Admin Panel) will be used to Ban users from add/edit actions (add, edit, restore actions will be disabled for baned users)
<br><br>

[rk:h id="2"]Logged in users - Permissions[/rk:h]
- add, edit perms are used on Wiki Pages to check if user can add or edit pages. There are also two extra options:<br>
"Can view Page" - can see pages<br>
"Can set Page as current" - can set edited page as current<br><br>

[rk:h id="3"]CAN_SET_CURENT and Edit Proposals[/rk:h]
If someone cant set edited page as current it will be saved as a one of older versions of that Wiki Page but it will be market as Edit Proposal 
and on the history list will be highlighted in green. Staff members can "unpropose" it (becomes normal "old version") or anyone who CAN_SET_CURENT and edit can
restore it / and if needed - edit it.<br>
- A list of all Edit Proposals can be found on /wiki/proposals/<br><br>

[rk:h id="2"]RSS Feeds[/rk:h]
<div class="box">http://localhost:8080/wiki/feeds/latestpages/ - latest pages</div>
<br>

[rk:h id="2"]Wiki Markup[/rk:h]
Wiki uses HTML as a markup :) and some helpers. There are tree CSS styles for creating "boxes":
[rk:syntax lang="xml"]PGRpdiBjbGFzcz0ibm90ZSI+dGV4dCBoZXJlPC9kaXY+DQo8ZGl2IGNsYXNzPSJub3RpY2UiPnRleHQgaGVyZTwvZGl2Pg0KPGRpdiBjbGFzcz0iYm94Ij50ZXh0IGhlcmU8L2Rpdj4=[/rk:syntax]
<br>

[rk:h id="2"]ContentBBCode[/rk:h]
Wiki CBC Descriptions module in the Admin Panel is designed to keep descriptions of all CBC plugins you have. ContentBBcode is a pluggable 
tags system (CBC for short). A CBC plugin can be a JS widget wrapper or perform other dynamic operations like display latest changes on the wiki.<br><br>


[rk:h id="1"]TODO[/rk:h]
- Files/Images upload/handling on wikiPages - ideas welcomed<br>
- More CBC<br>
- A lot of work in MyghtyBoard...<br><br>

[rk:h id="2"]ToooooooDooooo[/rk:h]
- Fulltext search (SoC code) ?<br>
- Row level permission (SoC, Ill check this later when the wiki will be "finished") ?''', changes='Page Creation', creation_date='2006-09-04 15:42:46', modification_date='2006-09-04 15:42:46', modification_user='piotr', modification_ip='666.69.69.69')
p.save()

Category.objects.all().delete()
mc = Category(cat_name='First Category', cat_order='0')
mc.save()
mc = Category(cat_name='Second Category', cat_order='1')
mc.save()

Forum.objects.all().delete()
mf = Forum(forum_category = Category.objects.get(id=1), forum_name = 'First Forum', forum_description ='A Forum', forum_order='0', forum_posts='4', forum_lastpost = 'piotr<br>2006-09-04 15:56:29<br><a href="/forum/topic/1/2/">Frugalware Topic</a>')
mf.save()
mf = Forum(forum_category = Category.objects.get(id=1), forum_name = 'Second Forum', forum_description ='A description', forum_order='1')
mf.save()
mf = Forum(forum_category = Category.objects.get(id=2), forum_name = 'Bla bla bla', forum_description ='Extra Forum', forum_order='0')
mf.save()

Topic.objects.all().delete()
mt = Topic(topic_forum = Forum.objects.get(id=1), topic_name = 'A Test Topic', topic_author = 'piotr', topic_posts = '2', topic_lastpost = 'piotr<br>2006-09-04 15:55:11', topic_modification_date = '2006-09-04 15:55:11')
mt.save()
mt = Topic(topic_forum = Forum.objects.get(id=1), topic_name = 'Frugalware Topic', topic_author = 'piotr', topic_posts = '2', topic_lastpost = 'piotr<br>2006-09-04 15:56:29', topic_modification_date = '2006-09-04 15:56:29')
mt.save()

Post.objects.all().delete()
mp = Post(post_topic = Topic.objects.get(id=1), post_text = 'This is a test topic\r\n\r\n:twisted::grin:', post_author = 'piotr', post_date = '2006-09-04 15:55:00', post_ip = '127.0.0.1')
mp.save()
mp = Post(post_topic = Topic.objects.get(id=1), post_text = 'and a test reply', post_author = 'piotr', post_date = '2006-09-04 15:55:11', post_ip = '1.2.3.4')
mp.save()
mp = Post(post_topic = Topic.objects.get(id=2), post_text = 'Miklos Vajna has announced the second release candidate of Frugalware Linux 0.5, the last development build before the stable release, expected at the end of September: "The Frugalware Developer Team is pleased to announce the immediate availability of Frugalware 0.5rc2, the second release candidate of the upcoming 0.5 stable release. A short and incomplete list of changes since 0.5rc1: updated GNOME to 2.16 Release Candidate (2.15.92); ~300 bugfixes; updated KDE and GRUB artwork; more than 30 new packages: ntfs-3g, avifile, gnome-sharp and many more!" Here is the brief release announcement. Download (SHA1): frugalware-0.5rc2-i686-dvd1.iso (4,264MB).', post_author = 'piotr', post_date = '2006-09-04 15:56:12', post_ip = '1.2.3.4')
mp.save()
mp = Post(post_topic = Topic.objects.get(id=2), post_text = '<blockquote><b>piotr wrote:</b><br><cite>Mikos Vajna has announced the second release candidate of Frugalware Linux 0.5, the last development build before the stable release, expected at the end of September: "The Frugalware Developer Team is pleased to announce the immediate availability of Frugalware 0.5rc2, the second release candidate of the upcoming 0.5 stable release. A short and incomplete list of changes since 0.5rc1: updated GNOME to 2.16 Release Candidate (2.15.92); ~300 bugfixes; updated KDE and GRUB artwork; more than 30 new packages: ntfs-3g, avifile, gnome-sharp and many more!" Here is the brief release announcement. Download (SHA1): frugalware-0.5rc2-i686-dvd1.iso (4,264MB).</cite></blockquote>\r\nTollef Fog Heen has announced the second alpha release (also known as "Knot") of Ubuntu 6.10, code name "Edgy Eft": "Welcome to Edgy Eft Knot 2, which will in time become Ubuntu 6.10. The primary changes from Knot 1 have been implementations of feature goals as listed on this page. Common to all variants, we have upgraded X.Org to the 7.1 release. In Ubuntu, GNOME has been updated to 2.16.0 Release Candidate 1. Other notable changes are listed here. KDE has been updated to 3.5.4. Other notable Kubuntu changes are listed here." Read the full release announcement for further information and a list of up-to-date download mirrors. As always, the full range of live and installation CDs for various architectures is available for download from the project''s main server; here is a quick link to the i386 Desktop CD: edgy-desktop-i386.iso (666MB, MD5). Kubuntu 6.10 Knot 2 CDs have also been released.', post_author = 'piotr', post_date = '2006-09-04 15:56:29', post_ip = '1.2.3.4')
mp.save()

from django.contrib.auth.models import Group, Permission
Group.objects.all().delete()
g = Group(name='users')
g.save()
#a = Permission.objects.all()
#for i in a:
	#print str(i.name) + ' - ' + str(i.codename)
g.permissions.add(Permission.objects.get(codename='can_view'), Permission.objects.get(codename='can_set_current'), Permission.objects.get(codename='add_page'), Permission.objects.get(codename='add_taskcomment'), Permission.objects.get(codename='change_page'), Permission.objects.get(codename='add_topic'), Permission.objects.get(codename='add_post'))
