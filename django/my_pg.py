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
