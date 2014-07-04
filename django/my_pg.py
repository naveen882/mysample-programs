from models import Poll,Choice,Article,Publication

p=Poll.objects.all()
for i in p:
	print i.id
	print i.access
	print i.question
print "==========================="
ch=Choice.objects.all()
for i in ch:
	print i.poll.id
	print i.poll.question	
	print i.votes
	print i.choice_text
print "==========================="
p=Poll.objects.get(pk=1)
p.choice_set.create(choice_text="new",votes=5)
p.choice_set.add()
pp = p.choice_set.all()
print "count = %d"%(p.choice_set.count())
for l in pp:
	print l.choice_text
	print l.id
print "==========================="
pub= Publication.objects.all()
for i in pub:
	print i.id
	print i.title
art=Article.objects.all()
for i in art:
	print i.id
	print i.headline
	for t in i.publications.all():
		print t.title

pb=Publication.objects.get(pk=1)
print pb.id
try:
	#print pb.article_set.get(pk=4).delete()
	pass
except:
	pass

at=Article(headline="NASA finds intelligent life on Earth",pk=4)
at.save()
#at=Article.objects.get(pk=4)
at.publications.add(pb)

class A(object):
	a='hello'
	def printing(self):
		a='world'
		print a
		print self.a
x=A()
x.a
x.printing()
print "====================================="
class A(object):
	def hello(self):
		print 'It is class A'
 
class B(object):
	def hello(self):
		print 'It is class B'
 
class C(A,B):
	def hello(self):
		print 'It is class C'
 
c = C()
c.hello()
print "====================================="
if __name__ == "__main__":
	print "main"
print "====================================="
#To find the 1st,2nd lowest,
def ty(l,n):
	l=sorted(l)[n-1]
	print l

ty([4,3,5,2,1],2)
print "====================================="
#To find the 1st,2nd highest,
def ty(l,n):
	l=sorted(l)[-n]
	print l

ty([4,3,5,2,1],2)
print "====================================="
print "====================================="

"""
value_list is used to get tuples
==========
at=Article.objects.values_list("id","headline","publications")
at
[(1L, u'headline1', 1L), (3L, u'NASA finds intelligent life on Earth', None), (4L, u'NASA finds intelligent life on Earth', 1L), (5L, u'NASA finds intelligent life on Earth', None)]

order_by: 
=========
(-id) to get decreasing order
Image.objects.all().order_by("-id")[0] //gets max(id)

lte or gte:
===========
Entry.objects.filter(pub_date__lte='2006-01-01') or Entry.objects.filter(pub_date__gte='2006-01-01')

translates (roughly) into the following SQL:

SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

Contains:
=========
Entry.objects.get(headline__contains='Lennon')

Roughly translates to this SQL:

SELECT ... WHERE headline LIKE '%Lennon%';

ISNULL:
=======
Blog.objects.filter(entry__authors__name__isnull=True)

IN:
===
Blog.objects.filter(pk__in=[1,4,7])

Complex lookups with Q objects:
===============================
from django.db.models import Q
Q(question__startswith='What')

ex:
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)

Updating multiple blogs at once:
================================
Entry.objects.all().update(blog=b)

related_name:
===============
If specified
blog = ForeignKey(Blog, related_name='entries')
b.entries.all() 

Middleware is a framework of hooks into Django's request/response processing. It's a light, low-level "plugin" system for globally altering Django's input or output.

Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, TransactionMiddleware, that wraps the processing of each HTTP request in a database transaction.
A Django installation doesn't require any middleware - MIDDLEWARE_CLASSES can be empty, if you'd like - but it's strongly suggested that you at least use CommonMiddleware.
The order in MIDDLEWARE_CLASSES matters because a middleware can depend on other middleware. For instance, AuthenticationMiddleware stores the authenticated user in the session therefore, it must run after SessionMiddleware.


//To add a module to admin admin.site.register(Author)


"""


"""
append:

x = [1, 2, 3]
x.append([4, 5])
print (x)

gives you: [1, 2, 3, [4, 5]]

extend:

x = [1, 2, 3]
x.extend([4, 5])
print (x)

gives you: [1, 2, 3, 4, 5]
"""


"""
Django Request Response processing

The steps are. (With Apache/Mod_wsgi, similar steps for other setup.)

    User's request comes to Apache etc.
    Apache sends request to django.core.handlers.wsgi via mod_wsgi.
    A list of request and response middleware callables is created.
    Request middleware is applied. If it sends a response, it is returned to the user.
    urlresolvers.resolve finds the view funcion to use.
    View middleware is applied. If response comes, it is sent back to the user.
    View function is called. It talks to models to do business logic, and renders the templates.
    The response middleware is applied, and response is sent back to the users.

This misses a lot of important steps (Exception middleware, request_context populating, ...) but is a basic high level overview.


http://agiliq.com/blog/2009/06/django-request-response-processing/
"""


"""
To access a url from template ex: {% url "nav_bar:index"%}
Step 1: install nav_bar in installed apps in settings.py
step 2 : configure main urls.py as 
	urlpatterns = patterns('',
	url(r'^help/', include('nav_bar.urls', namespace='nav_bar', app_name='nav_bar')), #where nav_bar is a separate app and include is very important
) 
step 3:
nav_bar.urls.py include name ="index" as the following	
urlpatterns = [
    url(r'^$', views.blog.index,name='index'),
]

"""


"""
Template context processors are for adding a new tag in template in django
"""


"""
https://docs.djangoproject.com/en/1.6/topics/http/middleware/#hooks-and-application-order  #important
Middle ware in django
During the request phase, before calling the view, Django applies middleware in the order it’s defined in MIDDLEWARE_CLASSES, top-down. Two hooks are available:

    process_request()
    process_view()

During the response phase, after calling the view, middleware are applied in reverse order, from the bottom up. Three hooks are available:

    process_exception() (only if the view raised an exception)
    process_template_response() (only for template responses)
    process_response()

middleware application order

If you prefer, you can also think of it like an onion: each middleware class is a “layer” that wraps the view.

The behavior of each hook is described below.

Note:After a view function is called and completed the middle ware is applied in the reverse order before retutning the response
"""


"""
http://www.b-list.org/weblog/2006/jun/13/how-django-processes-request/
http://www.youtube.com/watch?v=q0YqAbI7rw4
"""


"""
Static request: is one when a request comes to a webserver they are usually accessing files and that can be handled by the web server itself(apache or nginx) and there is no need of a framework
mod_python or mod_wsgi is a handler 
mod_python or mod_wsgi from which a webserver passes the request on  
WSGI : Web server gateway interface
Session management has to be happen in web application layer
WSGI handlers in django is located in django.core.handlers.wsgi.WSGIHandler which has a method as get_response() which calls the base handler
'django.core.handlers.base.BaseHandler is the one that is triggered after wsgi handler
Through WSGI layer the request comes request middleware via basehandler. Note : request middle ware takes request object
All middle wares can return two things i.e, httpresponse or None
http response : is returned then no views or any other middlewares will be applied.So this is a best place to check for authenitication/If user is not authenticated redirect him to login page from here.
None : if None is returned in request middleware then the request is middle is saying i do not not what do to with this request and then the next middle ware comes into picture.
After request middleware to resolve the url,  urlresolvers middle ware is applied to resolve the url from import django.core.urlresolvers and from which the particular url is looked up
After matching the url view middleware is applied and the respective view is called.Note: view middleware take request and view object
Different response types are : 
httpresponse : plain html response example is html = "hello <b>world</b>" return httpresponse(html)
httpresponseredirect : is redirecting to a different page
jsonresponse : this wil serialize a dictionary and send the headers appropriate in the json response
streaminghttpresponse: it takes an iterable. its an iterable response when dealing with large response.Its cool since it will not fill up memory since it is an iterator and bad because it a long response process and will not use all the memory
template context processor: takes a request object and returns a dict
if you want a common template tag to be defined for all the template pages then use the template processor tag to use it instead of view which will be common to all pages and the overhead is avoided of defining the same variable in all the views
 then process midlleware is applied which is also to deal with performance tuning-process_response()
exception middle ware is called only when you do not handle excpetion in view.It only fires when something goes wrong .not only in view but also in some other context
_exception_middleware is a list of the process_exception methods from any middleware classes which defined them.

Notes about template:
There are three contructs in a django template:
1.Variable references. In a template they look like this: {{ foo }}.
2.Template filters, which act on the above. Using the filter bar on the example above would look like this: {{ foo|bar }}. Generally these are used for output formatting (e.g., running Textile over something, formatting a date, etc.)
3.Template tags. They look like this: {% baz %}. This is where the “logic” of templates is implemented, you can do things like {% if foo %}, {% for bar in foo %}, and so on, and if and for are template tags.
Variable references work in a fairly simple way; if you’re just printing a variable directly, as in {{ foo }}, the template system just outputs it. The only complexity here is when you do something like {{ foo.bar }}; in that case, the template system tries a few things in order:

First it tries a dictionary-style lookup, to see if foo[‘bar’]exists. If it does, then that value is output and that’s the end of the process.
If dictionary lookup fails, next the template system tries an attribute lookup, to see if foo.bar exists. It also checks whether the attribute is callable, and tries calling it in that case.
If attribute lookup fails, the template system tries looking it up as a list index.
if all of these fail, the template system outputs the value of the setting TEMPLATE_STRING_IF_INVALID, which defaults to an empty string.
"""
