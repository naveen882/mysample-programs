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
How Django processes a request

Published June 13, 2006. Filed under: Django, Frameworks.

In a comment he left yesterday, Jonathan Snook posed an excellent challenge: document the chain of how Django processes a request, from start to finish, with plenty of detail on the various things being called internally and links to the appropriate documentation.

Simon Willison once wrote such a document, but it was a fairly high-level view and a fair number of things have changed since then, so I’m going to take a stab at it myself, and hopefully the result will be comprehensible.

Note: this is a first draft. Not a finished product, not a complete listing. Expect it to change frequently as I work on it. Ideally I’ll be able to get some help generating a visualization at some point, but for now I’ll stick to plain text.

Where official documentation for an item is available I’ll link to it. For items which don’t yet have documentation I’ll provide links to the current locations of the relevant code in the Django repository — these locations may change over time, particularly because I’m often going to be linking to line numbers in individual files, but I’ll do my best to keep them up to date. If you see something here that’s incorrect, or spot something I’ve left out or could have explained better, please leave a comment to let me know.

Updated October 2, 2006: I’ve just gone through and done quite a bit of updating of this article; several references to places in the code needed to be updated, and I rewrote a few things to reflect some shuffling around of internal bits that’s taken place recently.

Updated November 28, 2006: Added a note about when the database connection is closed.

Updated December 20, 2006: linked to notes on the Django wiki about the dispatcher.

Let’s get started.
Incoming!

The very first thing that happens is that something else invokes Django. That happens in one of two ways:

    Apache/mod_python is the server setup, in which case the request is handed to Django by mod_python creating an instance of django.core.handlers.modpython.ModPythonHandler.
    Something else is the server, in which case it needs to be WSGI-compliant. In this situation, an instance of django.core.handlers.wsgi.WsgiHandler is created by the server.

Both of those classes inherit from django.core.handlers.base.BaseHandler, which contains common code needed for any type of request.
I’ve got a handle on it

When one of the above handlers is instantiated, a couple things happen immediately:

    The handler imports your Django settings file.
    The handler imports Django’s custom exception classes.
    The handler calls its own load_middleware method, which loads all the middleware classes it finds listed in the MIDDLEWARE_CLASSES setting and introspects them.

That last bit is somewhat complicated, so let’s look at it in detail.

A middleware class can hook into any of four phases of processing: request, view, response and exception. It does so by defining methods named, appropriately enough, process_request, process_view, process_response and process_exception. The middleware can define any or all of these depending on what functionality it wants to provide.

When the handler introspects the middleware, it looks for methods with those names, and builds up four lists which are stored as instance variables of the handler:

    _request_middleware is a list of the process_request methods (in each case these will be the actual methods, so they’re directly callable) from any middleware classes which defined them.
    _view_middleware is a list of the process_view methods from any middleware classes which defined them.
    _response_middleware is a list of the process_response methods from any middleware classes which defined them.
    _exception_middleware is a list of the process_exception methods from any middleware classes which defined them.

Green light: now begin

Now the handler is ready to really begin processing, so it fires the dispatcher signal request_started (the internal dispatcher in Django allows various components to advertise what they’re doing, and allows other bits of code to listen for certain events; it’s currently not documented officially, but there are some notes on the wiki). Then it instantiates a subclass of django.http.HttpRequest. Depending on the handler, this may be an instance of django.core.handlers.modpython.ModPythonRequest or it may be an instance of django.core.handlers.wsgi.WSGIRequest. The two different classes are needed because the mod_python and WSGI APIs pass in the request information in different formats, and that information needs to be parsed into a single standard format Django can work with.

Once an HttpRequest of some sort exists, the handler calls its own get_response method, passing theHttpRequest as the only argument. This is where nearly all of the actual activity happens.
Middleware, round 1

The first thing get_response does is loop through the handler’s _request_middleware instance variable and call each method in that list, passing in the HttpRequest instance as an argument. These methods have the option of short-circuiting the rest of the process and immediately causing get_response to return, by returning a value themselves (if they do so, the return value needs to be an instance of django.http.HttpResponse, which we’ll talk about in a bit). If one of them does so, that’s it and we’re back into the main handler code; get_response won’t even wait to see what the other middleware classes wanted to do, it will just return and the handler will go into its response phase.

More commonly, though, the middleware methods applied here simply do some processing and decide whether to add, remove or supplement attributes of the request.
Resolution time

Assuming that none of the middlewares which acted on the request short-circuited straight to a response, the handler next tries to resolve the requested URL. It looks in the settings file for a setting called ROOT_URLCONF, and hands that, along with a base URL of /, as arguments to create an instance of django.core.urlresolvers.RegexURLResolver, then calls the RegexURLResolver‘s resolve method with the requested URL path.

The URL resolver follows a fairly simple pattern. For each item in the urlpatterns list generated by the URL configuration file specified by the ROOT_URLCONF setting, it checks whether the requested URL path matches that item’s regular expression; if so , there are two options:

    If the item has a call to include, the resolver chops off the bit of the URL that matched, moves to the URL configuration file specified by the include and begins iterating over the items in its urlpatterns list. Depending on the depth and modularity of your URL hierarchy, this may be repeated several times.
    Otherwise, the resolver returns three items: the view function specified by the matched item, a list of non-named matched groups from the URL (to be used as positional arguments for the view) and a dictionary of keyword arguments, built from a combination of any named matched groups in the URL and any extra keyword arguments specified in that line in the URLConf.

Note that this stops at the first match which specifies a view, so it’s best to have your URL configuration proceed from more specific regexes to less specific ones, in order to ensure that the resolver doesn’t match one of the less specific ones first and end up returning the wrong view function.

If no matches are found, the resolver raises the exception django.core.urlresolvers.Resolver404, a subclass of the exception django.http.Http404. We’ll get to how that’s handled a little later on.
Middleware, round 2

Once it knows the view function it will be using and what arguments to pass to it, the handler looks at its _view_middleware list, and calls each method in that list, passing the HttpRequest, the view function, the list of positional arguments for the view and the dictionary of keyword arguments for the view.

Again, it’s possible for middleware to intervene at this stage and force the handler to return immediately.
Into the view

If processing is still going at this point, the handler calls the view function. Views in Django are somewhat nebulous because only a few requirements are placed on them:

    They must be callable.
    They must accept as their first positional argument an instance of django.http.HttpRequest.
    They must either raise an exception or return an instance of django.http.HttpResponse.

Beyond that, the sky’s the limit. Most commonly, though, views will use Django’s database API to create, retrieve, update or delete something in the database, and they’ll load and render a template to display something to the end user.
Templates

Django’s template system is two-faceted: there’s one part that’s HTML with a few extra things mixed in and is mostly used by designers, and one part that’s pure Python and is used by programmers.

From an HTML author’s point of view, Django’s template system is pretty simple. There are three constructs you need to know about:

    Variable references. In a template they look like this: {{ foo }}.
    Template filters, which act on the above. Using the filter bar on the example above would look like this: {{ foo|bar }}. Generally these are used for output formatting (e.g., running Textile over something, formatting a date, etc.)
    Template tags. They look like this: {% baz %}. This is where the “logic” of templates is implemented, you can do things like {% if foo %}, {% for bar in foo %}, and so on, and if and for are template tags.

Variable references work in a fairly simple way; if you’re just printing a variable directly, as in {{ foo }}, the template system just outputs it. The only complexity here is when you do something like {{ foo.bar }}; in that case, the template system tries a few things in order:

    First it tries a dictionary-style lookup, to see if foo[‘bar’]exists. If it does, then that value is output and that’s the end of the process.
    If dictionary lookup fails, next the template system tries an attribute lookup, to see if foo.bar exists. It also checks whether the attribute is callable, and tries calling it in that case.
    If attribute lookup fails, the template system tries looking it up as a list index.

If all of these fail, the template system outputs the value of the setting TEMPLATE_STRING_IF_INVALID, which defaults to an empty string.

Template filters are simply Python functions which accept a value and an argument, and return a new value. For example, the date filter takes a Python datetime object as its value and a standard strftime formatting string as its argument, and returns the result of applying that formatting string to that datetime object.

Template tags are where things are a bit complicated, and where you get close to how the Django template system really works.
The structure of a Django template

Internally, a Django template is represented as a collection of ‘nodes’; these are Python classes which all inherit from the base node class django.template.Node. Nodes can do various sorts of processing, but they have one thing in common: every Node must have a method called render which accepts as its second argument (the first argument, of course, will be the Node instance) an instance of django.template.Context, which is a dictionary-like object containing all the variables which are accessible to the template. The render method of a Node must return a string, but if the Node is meant to carry out some task other than output (for example, if it’s meant to modify the template context by adding, removing or modifying variables in the Context instance passed to it) it can return an empty string.

Django includes a number of subclasses of Node which provide useful functions; each of the built-in template tags, for example, is handled by a subclass of Node (e.g., there’s an IfNode which implements the if tag, a ForNode which implements the for tag, etc.). All of the built-in tags are found in django.template.defaulttags. In reality, all of the template constructs described above are Nodes of some sort, and so is plain text; a variable lookup is handled by a VariableNode, filters, by their nature, get applied in a VariableNode, tags are Nodes of various types and plain text is a TextNode.

Generally, a view renders a template by carrying out the following steps, in order:

    Loading the template to be rendered; this is handled by the function django.template.loader.get_template, which can use any of several methods to locate the desired template file. The get_template function returns an instance of django.template.Template, which is an object containing the parsed template and methods for using it.
    Instantiating a Context to be used in rendering the template; if the Context subclass django.template.RequestContext is used, additional context-processing functions will be applied which can automatically add variables which were not defined in the view. The constructor method for Context takes a dictionary of key/value pairs (which will become the variable names/values for the template) as its only argument; RequestContext takes an instance of HttpRequest and a dictionary.
    Calling the Template instance’s render method, with the Context object as the first positional argument.

The return value of the Template‘s render method is a string, which is the concatenation of the return values of the render methods of all the Template‘s constituent Nodes, called in the order in which they occur in the Template.
Response time, sort of

Once a template has been rendered, or some other sort of suitable output has been generated, the view is responsible for creating an instance of django.http.HttpResponse. The constructor for this class takes two optional arguments:

    A string (which should be the first positional argument, or the keyword argument content) which will be the body of the response. Most of the time, this will be the output of rendering a template, but it doesn’t have to be; you can pass any valid Python string in here.
    A value for the Content-Type header of the response (which should be the second positional argument, or the keyword argument mime_type). If you don’t provide this argument, Django will fill in the value of the setting DEFAULT_MIME_TYPE and the value of the setting DEFAULT_CHARSET which, if you haven’t changed them from the defaults in Django’s global settings file, will be “text/html” and “utf-8”, respectively.

Middleware, round 3: exception edition

If the view function, or something which happens inside it, raises an exception, then get_response (I know we spent a while digging into views and templates, but once the view returns or raises we pick up again in the middle of the handler’s get_response method) will loop through its _exception_middleware instance variable and call each method there, passing the HttpRequest and the exception as arguments. Hopefully one of those methods will instantiate and return an HttpResponse.
Still not responding?

At this point it’s possible that there still isn’t an HttpResponse; this could be due to a number of factors:

    The view might not have returned a value.
    The view might have raised an exception that none of the middleware was able to deal with.
    A middleware method that was trying to deal with an exception might have raised a new exception itself.

When this happens, get_response falls back to its own exception handling mechanisms; these come in several layers:

    If the execption was Http404 and the DEBUG setting is True, get_response will execute the view django.views.debug.technical_404_response, passing the HttpRequest and the exception as arguments. This view displays information about the patterns the URL resolver tried to match against.
    If DEBUG is False, and the exception was Http404, get_response calls the URL resolver’s resolve_404 method; this method looks at the URL configuration to determine which view has been specified for handling 404 errors. This defaults to django.views.defaults.page_not_found, but can be overridden in the URL configuration by assigning a value to the variable handler404.
    For any other type of exception, If the DEBUG setting is True, get_response will execute the view django.views.debug.technical_500_response, passing the HttpRequest and exception information as arguments. This view provides detailed information about the exception, including the traceback, local variables at each level of the stack, a detailed representation of the HttpRequest object and a listing of all non-sensitive settings.
    If DEBUG is False, get_response calls the URL resolver’s resolve_500 method, which works in mostly the same way as resolve_404; the default view in this case is django.views.defaults.server_error, and can be overridden in the URL configuration by assigning a value to the variable handler500.

Additionally, for any exception other than django.http.Http404 or Python’s built-in SystemExit, the handler will fire the dispatcher signal got_request_exception, and construct a description of the exception which is mailed to each person listed in the Django settings file’s ADMINS setting before returning.
Middleware, final round

At this point, regardless of anything which went wrong at any level in get_response, it should have returned an HttpResponse instance, so we’re back up into the main part of the handler. The first thing it does once it gets that HttpResponse is loop through its _response_middleware instance variable and apply the methods it finds there, passing the HttpRequest and the HttpResponse as arguments.

Note that this is the last chance any middleware has to modify things.
The check is in the mail

And now it’s time to wrap up. Once the final round of middleware has been applied, the handler fires the dispatcher signal request_finished, which is the absolute last call for anything that wanted to execute during the current request. Handlers which listen for this signal should clean up and free any resources which were being used; for example, Django attaches a listener to request_finished which will close any open database connections.

After that happens, the handler builds up an appropriate return value to send back to whatever instantiated it (currently, either a mod_python-appropriate response or a WSGI-compliant response depending on the handler), and returns it.
Whew

And we’re done. From beginning to end, that’s how Django processes a request.

"""
