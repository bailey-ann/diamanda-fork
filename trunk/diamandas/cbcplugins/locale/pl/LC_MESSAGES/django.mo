��          �      ,      �  �   �  �   2  U   �  �   
  �   �  u   ;  X  �  �   
     �     �  6   �  >     '   M  �   u  <   �     3  Z  P  �   �	  B   a
  A   �
  �   �
  �   �  �   O  �   �  J   �           <  0   Y  >   �  (   �  ~   �  >   q     �                                                      
   	                     Will highlight the code using entered in the "lang" attribute scheme - python, xml, html, ruby, perl, lua, cpp, delphi, java, php, makefile, diff, javascript, css, sql. Will insert a external link with nice icon. "desc" attribute is optional and if added will display a description text by the link Will insert a link to a given page (by the given slug) using it title and description Will insert a link to a local image using a thumb and a pop-up. The thumb will be created by PIL. Images can be in SITE_IMAGES_DIR_PATH subfolders. Will insert a link to a local image using a thumb and lightbox JS widget. The thumb will be created by PIL. Images can be in SITE_IMAGES_DIR_PATH subfolders Will insert a list of 10 latest active topics from selected forum or from all forums if "forum attribute is set to 0. Will insert a table with row highlighting and column sorting. name - unique name for each table on the page, width - optional, default 100%, sort - defines sorting rules, S - string, N - number - for each column. Between tags you place the table structure, using | as a column separator. First row is the table head, the rest is the table data. Will insert the given title in a H1-4 tag (as defined in the id attribute). Use this tags if you want to use Page Table of Contents generated by [toc] [rk:art slug="SLUG_NAME"] [rk:h id="1-4"]Title[/rk:h] [rk:link href="URL" desc="DESCRIPTION"]TITLE[/rk:link] [rk:lthumb src="image.jpg"] [rk:lthumb src="folder/image.jpg"] [rk:syntax lang="LANG"]CODE[/rk:syntax] [rk:table name="tablea" width="50%" sort="'N', 'S', 'S'"]
field1|field2|fiel3
1|valuex|valuey
4|bar|text
2|tekx2|foo
[/rk:table] [rk:thumb src="image.jpg"] [rk:thumb src="folder/image.jpg"] [rk:topics forum="Forum_id"] Project-Id-Version: cbcplugins
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2006-11-12 15:36+0000
PO-Revision-Date: 2006-04-08 12:19+0900
Last-Translator: Piotr Maliński <riklaunim@gmail.com>
Language-Team: Polish <translation-team-pl@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 Podświetli kod bazując na języku podanym w atrybucie "lang". Możliwe opcje to - python, xml, html, ruby, perl, lua, cpp, delphi, java, php, makefile, diff, javascript, css, sql. Wstawi odnośnik używając ikonki. Atrybut "desc" jest opcjonalny Wstawi odnośnik do podanej strony używając jej tytułu i opisu Stworzy odnośnik do lokalnej grafiki z wykorzystaniem miniatury i popupa. Lokalne grafiki znajdują się w katalogu określonym przez SITE_IMAGES_DIR_PATH i jego podkatalogach. Stworzy odnośnik do lokalnej grafiki z wykorzystaniem miniatury i widżeta JS. Lokalne grafiki znajdują się w katalogu określonym przez SITE_IMAGES_DIR_PATH i jego podkatalogach. Wyświetli listę 10 ostatnich tematów z wybranego forum. By wyświetlić listę tematów ze wszystkich for wstaw 0 jako "forum" Wyświetli tabelę z podświetlanymi wierszami i sortowaniem kolumn (JS). Atrybut "name" to unikalny identyfikator tabelki. "sort" określa reguły sortowania - S - łańuch, N - liczba. Znak | oddziela kolumny, pierwsza kolumna jest nagłówkiem tabeli. Wstawi podany "Tytuł" w tagu H1-4 wraz z zakładką używaną przez [toc] [rk:art slug="Nazwa Odnośnika"] [rk:h id="1-4"]Tytuł[/rk:h] [rk:link href="URL" desc="OPIS"]TYTUŁ[/rk:link] [rk:lthumb src="image.jpg"] [rk:lthumb src="folder/image.jpg"] [rk:syntax lang="JĘZYK"]KOD[/rk:syntax] [rk:table name="tabela" width="50%" sort="'N', 'S', 'S'"]
pole1|pole2|pole3
1|valuex|valuey
4|bar|text
2|tekx2|foo
[/rk:table] [rk:thumb src="grafa.jpg"] [rk:thumb src="folder/grafika.jpg"] [rk:topics forum="id_Forum"] 