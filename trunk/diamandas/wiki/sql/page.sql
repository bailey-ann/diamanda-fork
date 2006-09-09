INSERT INTO wiki_cbc (id, tag, tag_example, description) VALUES (1, 'art', '[rk:art slug="SLUG_NAME"]', 'Will insert a link to a given page (by the given slug) using it title and description'),
(2, 'catlist', '[rk:catlist name="CATEGORY_NAME"]', 'Will insert a tree like list of pages and subcategories of a given category by name in the name attribute or by id in id attribute'),
(3, 'h', '[rk:h id="1-4"]Title[/rk:h]', 'Will insert the given title in a H1-4 tag (as defined in the id attribute). Use this tags if you want to use Page Table of Contents generated by [toc] '),
(4, 'news', '[rk:news name="CATEGORY_NAME"]', 'Will insert a list of 10 latest news from given category.'),
(5, 'syntax', '[rk:syntax lang="LANG"]CODE[/rk:syntax]', 'Will highlight the code using entered in the "lang" attribute scheme - python, css, csharp (C#), php, js, java, vb, sql, delphi and ruby'),
(6, 'thumb', '[rk:thumb src="image.jpg"]', 'Will insert a link to a local image using a thumb and a pop-up. The thumb will be created by PIL.'),
(7, 'topic', '[rk:topics forum="Forum_id"]', 'Will insert a list of 10 latest active topics from selected forum or from all forums if "forum attribute is set to 0.');
INSERT INTO wiki_page (id, site_id, title, slug, description, text, changes, creation_date, modification_date, modification_user, modification_ip, modification_host) VALUES (1, 1, 'Diamanda Wiki Main Page', 'index', 'A description :)', '[rk:h id="1"]Diamanda Wiki SVN[/rk:h]\r\n[toc]<br><br>\r\n\r\nDiamanda (wiki and forum) is released under GPL License<br>\r\n<b>Author</b>: Piotr Malinski - riklaunim@gmail.com<br>\r\n\r\n<div class="notice">This applications is in developement and currently is in Beta stage.</div>\r\n<br>\r\n[rk:h id="2"]Features[/rk:h]\r\n<b>WIKI</b>\r\n<blockquote>\r\n- add, Edit Pages with permission controll<br>\r\n- full history support<br>\r\n- diffs between all versions of a wikiPage<br>\r\n- safe HTML markup and plugable ContentBBcode tags<br>\r\n- wikiNews with RSS feeds<br>\r\n- wikiPages and wikiNews set as many2many with wikiCategories<br>\r\n- wikiCategories set as Many2One with it self<br>\r\n- multilingual interface (pl/en currently)<br>\r\n- google sitemap generation<br>\r\n- PDF export with htmldoc<br>\r\n- bans\r\n</blockquote><br>\r\n<b>MyghtyBoard Forum</b>\r\n<blockquote>\r\n- Add Topic/Post<br>\r\n- Edit my posts<br>\r\n- Permission controll, user can''t post a new post after his post<br>\r\n- IP, hostname saved<br>\r\n- Nice themes :)\r\n</blockquote><br><br>\r\n\r\n[rk:h id="2"]Requirements:[/rk:h]\r\n- install <b>strip-o-gram</b> from <a href="http://www.zope.org/Members/chrisw/StripOGram" target="_blank">here</a> - it''s a safe HTML filter which is used in Diamanda WikiPages and forums.\r\n<div class="box">python setup.py install</div>\r\nwill install it.\r\n\r\n[rk:h id="2"]Instalation:[/rk:h]\r\n- edit urls.py and change the site_media path ''/home/piotr/diamanda/media'' to that on your computer:\r\n<div class="box">(r''^site_media/(.*)$'', ''django.views.static.serve'', {''document_root'': ''/path/here''}),</div>\r\n\r\n- create tables (sqlite3 by default):\r\n<div class="box">python manage.py syncdb</div>\r\n- create a superuser when creating tables!<br>\r\n\r\n- run the dev server: python\r\n<div class="box">manage.py runserver 8080</div>\r\n<br>\r\n<div class="note">- http://localhost:8080/ is the main wiki page<br>\r\n- http://localhost:8080/forum/ is the main MyghtyBoard Forum page</div><br>\r\n\r\n<div class="notice">Debug is set to True by default!</div>\r\n<br><br>\r\n\r\n[rk:h id="2"]MyghtyBoard[/rk:h]\r\nMyghtyBoard is the name of the forum script which is in heavy developement right now but all the "basic" features\r\nwork nicely. Categories and Forums are managed by the Django Admin Panel. Staff members and superusers are forum moderators.\r\n<br><br>\r\n\r\n[rk:h id="2"]Extra settings in settings.py[/rk:h]\r\nYou will find at the end of the file:\r\n[rk:syntax lang="python"]DQojIFJTUyBTZXR0aW5ncw0KU0lURV9OQU1FID0gJ0RpYW1hbmRhIFdpa2kgIScNClNJVEVfREVTQ1JJUFRJT04gPSAnQSBEaWFtYW5kYSBXaWtpIFNjcmlwdCcNClNJVEVfTkVXU19MSU5LID0gJy8nICMgd2hlcmUgbGlua3Mgb2YgdGhlIFJTUyBmZWVkcyBzaG91bGQgcG9pbnQNCg0KIyBBbm9ueW1vdXMgcGVybXMgU2V0dGluZ3MNCkFOT05ZTU9VU19DQU5fRURJVD1UcnVlDQpBTk9OWU1PVVNfQ0FOX0FERD1UcnVlDQpBTk9OWU1PVVNfQ0FOX1ZJRVc9VHJ1ZQ0KQU5PTllNT1VTX0NBTl9TRVRfQ1VSRU5UPUZhbHNlDQoNCiMgbXlnaHR5Ym9hcmQgY29uZmlnDQpBTk9OWU1PVVNfQ0FOX0FERF9UT1BJQz1UcnVlDQpBTk9OWU1PVVNfQ0FOX0FERF9QT1NUPVRydWUNCk1ZR0hUWUJPQVJEX1RIRU1FPSdhZW9sdXMnICMgdGhlbWUgbmFtZSwgY3VycmVuICJ3b3ciIGFuZCAiYWVvbHVzIg0KTVlHSFRZQk9BUkRfTEFORz0nZW5nbGlzaCcgIyBsYW5ndWFnZSBuYW1lIGZvciBpMThuIGdyYXBoaWNzICh0aGVtZSBtdXN0IGhhdmUgaW1hZ2VzIGZvciBzZWxlY3RlZCBsYW5ndWFnZQ0KDQojIHRodW1iIENCQw0KU0lURV9JTUFHRVNfRElSX1BBVEggPSAnL2hvbWUvcGlvdHIvZGlhbWFuZGEvbWVkaWEvaW1hZ2VzLycNClNJVEVfSU1BR0VTX1NSQ19QQVRIID0gJy9zaXRlX21lZGlhL2ltYWdlcy8nDQoNCiMgT3RoZXINClVTRV9CQU5TID0gRmFsc2UgIyB1c2UgV0lraUJhbnMgdG8gcHJldmVudCBiYW5lZCBmcm9tIGFkZC9lZGl0IGFjdGlvbnMNCg==[/rk:syntax]\r\n- RSS settings are used when generating RSS Feeds, SITE_NEWS_LINK doesn''t require any changes, the rest can be edited.<br>\r\n- Anonymous Permissions: True/False<br>\r\n- USE_BANS - if True the Wiki Ban module (see Admin Panel) will be used to Ban users from add/edit actions (add, edit, restore actions will be disabled for baned users)\r\n<br><br>\r\n\r\n[rk:h id="2"]Logged in users - Permissions[/rk:h]\r\n- add, edit perms are used on Wiki Pages to check if user can add or edit pages. There are also two extra options:<br>\r\n"Can view Page" - can see pages<br>\r\n"Can set Page as current" - can set edited page as current<br><br>\r\n\r\n[rk:h id="3"]CAN_SET_CURENT and Edit Proposals[/rk:h]\r\nIf someone can''t set edited page as current it will be saved as a one of older versions of that Wiki Page but it will be market as Edit Proposal \r\nand on the history list will be highlighted in green. Staff members can "unpropose" it (becomes normal "old version") or anyone who CAN_SET_CURENT and edit can\r\nrestore it / and if needed - edit it.<br>\r\n- A list of all Edit Proposals can be found on /wiki/proposals/<br><br>\r\n\r\n[rk:h id="2"]RSS Feeds[/rk:h]\r\n<div class="box">http://localhost:8080/wiki/feeds/latestpages/ - latest pages<br>\r\nhttp://localhost:8080/wiki/feeds/latestnews/ - 10 latest news<br>\r\nhttp://localhost:8080/wiki/feeds/latestnewsbycategory/X/ - where X is the category ID - latest 10 news from that category</div>\r\n<br>\r\n\r\n[rk:h id="2"]Wiki Markup[/rk:h]\r\nWiki uses HTML as a markup :) and some helpers. There are tree CSS styles for creating "boxes":\r\n[rk:syntax lang="xml"]PGRpdiBjbGFzcz0ibm90ZSI+dGV4dCBoZXJlPC9kaXY+DQo8ZGl2IGNsYXNzPSJub3RpY2UiPnRleHQgaGVyZTwvZGl2Pg0KPGRpdiBjbGFzcz0iYm94Ij50ZXh0IGhlcmU8L2Rpdj4=[/rk:syntax]\r\n<br>\r\n\r\n[rk:h id="2"]ContentBBCode[/rk:h]\r\nWiki CBC Descriptions module in the Admin Panel is designed to keep descriptions of all CBC plugins you have. ContentBBcode is a pluggable \r\ntags system (CBC for short). A CBC plugin can be a JS widget wrapper or perform other dynamic operations like display latest changes on the wiki.<br><br>\r\n\r\n\r\n[rk:h id="1"]TODO[/rk:h]\r\n- Files/Images upload/handling on wikiPages - ideas welcomed<br>\r\n- More CBC<br>\r\n- A lot of work in MyghtyBoard...<br><br>\r\n\r\n[rk:h id="2"]ToooooooDooooo[/rk:h]\r\n- Fulltext search (SoC code)<br>\r\n- Row level permission (SoC, I''ll check this later when the wiki will be "finished")', 'Page Creation', '2006-09-04 15:42:46', '2006-09-04 16:33:17', 'piotr', '127.0.0.1', 'localhost.localdomain');
INSERT INTO wiki_page_categories (id, page_id, wikicategory_id) VALUES (7, 1, 1);
INSERT INTO wiki_wikicategory (id, site_id, cat_parent_id, cat_name, cat_description, cat_depth) VALUES (1, 1, NULL, 'Main', 'Main WikiCategory', 0);
INSERT INTO auth_group (id, name) VALUES (1, 'users');
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (14, 1, 48),
(13, 1, 50),
(12, 1, 49),
(11, 1, 45),
(10, 1, 29),
(9, 1, 31),
(8, 1, 32),
(15, 1, 28);
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (1, 10, 1),
(2, 11, 1),
(3, 13, 1),
(4, 2, 1);