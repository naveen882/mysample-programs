naveen@naveen-laptop:/opt/ilabs/site_config$ su
Password: 
root@naveen-laptop:/opt/ilabs/site_config# python
Python 2.6.5 (r265:79063, Oct  1 2012, 22:07:21) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from polls.models import Poll,Choice
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named polls.models
>>> from test_pt.models import Poll,Choice
>>> Poll.objects.all()
[]
>>> Poll.objects.all()
[]
>>> from django.utils import timezone
>>> Poll.objects.all(question="this i smy first question?how about it",pub_date=timezone.now(),access=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: all() got an unexpected keyword argument 'question'
>>> Poll(question="this i smy first question?how about it",pub_date=timezone.now(),access=1)
<Poll: Poll object>
>>> p=Poll(question="this i smy first question?how about it",pub_date=timezone.now(),access=1)
>>> p.save()
>>> Poll.objects.all()
[<Poll: Poll object>]
>>> pp=Poll.objects.all()
>>> for p in pp:
...     print p
... 
Poll object
>>> for p in pp:
...     print p.question
...     print p.pub_date
...     print p.access
... 
this i smy first question?how about it
2013-07-03 08:59:40+00:00
1
>>> p=Poll(question="this is my second question?how about it",pub_date=timezone.now(),access=2)
>>> p.save()
>>> p=Poll(question="this is my third question?how about it",pub_date=timezone.now(),access=3)
>>> p.save()
>>> for p in pp:
...     print p.question
...     print p.pub_date
...     print p.access
... 
this i smy first question?how about it
2013-07-03 08:59:40+00:00
1
>>> pp=Poll.objects.all()
>>> for p in pp:
...     print p.question
...     print p.pub_date
...     print p.access
...     print "========"
... 
this i smy first question?how about it
2013-07-03 08:59:40+00:00
1
========
this is my second question?how about it
2013-07-03 09:07:40+00:00
2
========
this is my third question?how about it
2013-07-03 09:07:57+00:00
3
========
>>> ch=Choice(poll__id=1,choice_text="The sky",votes=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/base.py", line 367, in __init__
    raise TypeError("'%s' is an invalid keyword argument for this function" % kwargs.keys()[0])
TypeError: 'poll__id' is an invalid keyword argument for this function
>>> ch=Choice(poll_id=1,choice_text="The sky",votes=1)
>>> ch.save()
>>> ch=Choice(poll_id=2,choice_text="The sky",votes=1)
>>> ch=Choice(poll_id=2,choice_text="The sky",votes=2)
>>> ch.save()
>>> ch=Choice(poll_id=1,choice_text="The sky",votes=1)
>>> ch.save()
>>> ch=Choice(poll_id=3,choice_text="The sky",votes=1)
>>> ch.save()
>>> p=Poll.objects.get(pk=1)
>>> p.aquestion
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Poll' object has no attribute 'aquestion'
>>> p.question
u'this i smy first question?how about it'
>>> unicode(p.question)
u'this i smy first question?how about it'
>>> p.question
u'this i smy first question?how about it'
>>> p.question
u'this i smy first question?how about it'
>>> cc=p.choices_set.all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Poll' object has no attribute 'choices_set'
>>> cc=p.choice_set.all()
>>> for c in cc:
...     print c
... 
Choice object
Choice object
>>> for c in cc:
...     print c.id
...     print c.choice_text
...     print c.votes
... 
1
The sky
1
3
The sky
1
>>> p=Poll.objects.get(pk=2)
>>> print c.votes
1
>>> p.choice_set.create(votes=3,choices_text="my text")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 485, in create
    return super(RelatedManager, self.db_manager(db)).create(**kwargs)
  File "/opt/ilabs/django/django/db/models/manager.py", line 137, in create
    return self.get_query_set().create(**kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 375, in create
    obj = self.model(**kwargs)
  File "/opt/ilabs/django/django/db/models/base.py", line 367, in __init__
    raise TypeError("'%s' is an invalid keyword argument for this function" % kwargs.keys()[0])
TypeError: 'choices_text' is an invalid keyword argument for this function
>>> p.choice_set.create(votes=3,choices_text="my text")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 485, in create
    return super(RelatedManager, self.db_manager(db)).create(**kwargs)
  File "/opt/ilabs/django/django/db/models/manager.py", line 137, in create
    return self.get_query_set().create(**kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 375, in create
    obj = self.model(**kwargs)
  File "/opt/ilabs/django/django/db/models/base.py", line 367, in __init__
    raise TypeError("'%s' is an invalid keyword argument for this function" % kwargs.keys()[0])
TypeError: 'choices_text' is an invalid keyword argument for this function
>>> p.choice_set.create(votes=3,choice_text="my text")
<Choice: Choice object>
>>> p.choice_set.create(votes=3,choice_text="my text").save()
>>> p=Poll.objects.get(pk=2)
>>> print c.votes
1
>>> p.question
u'this is my second question?how about it'
>>> c=p.choices_set.all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Poll' object has no attribute 'choices_set'
>>> c=p.choice_set.all()
>>> print c.votes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'votes'
>>> for i in c:
...     print 
... 



>>> print c.choice_text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'choice_text'
>>> for i in c:
... print i.choice_text
  File "<stdin>", line 2
    print i.choice_text
        ^
IndentationError: expected an indented block
>>> for i in c:
...     print i.choice_text
... 
The sky
my text
my text
>>> Choice.objects.filter(poll__pub_date__year=current_year)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'current_year' is not defined
>>> current_year = timezone.now().year
>>> Choice.objects.filter(poll__pub_date__year=current_year)
[<Choice: Choice object>, <Choice: Choice object>, <Choice: Choice object>, <Choice: Choice object>, <Choice: Choice object>, <Choice: Choice object>]
>>> cc=Choice.objects.filter(poll__pub_date__year=current_year)
>>> for c in cc:
...     print c.id
...     print c.choice_text
... 
1
The sky
2
The sky
3
The sky
4
The sky
5
my text
6
my text
>>> cc=Choice.objects.filter(poll__pub_date="2013-07-03 09:07:40+00:00")
>>> print cc.choice_text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'choice_text'
>>> for c in cc:
...     print c.choice_text
... 
The sky
my text
my text
>>>  c = p.choice_set.create(choice_text='Just hacking again', votes=0)
  File "<stdin>", line 1
    c = p.choice_set.create(choice_text='Just hacking again', votes=0)
    ^
IndentationError: unexpected indent
>>> c = p.choice_set.create(choice_text='Just hacking again', votes=0)
>>> print c
Choice object
>>> print c.poll
Poll object
>>> c = p.choice_set.create(votes=0)
>>> for c in cc:
...     print c.choice_text
... 
The sky
my text
my text
>>> p.choice_set.count()
5
>>> p.id
2L
>>> print p.id
2
>>> c = p.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
>>> from django.contrib import admin
>>> admin.site.register(Poll)
>>> import django
>>> print dir(django)
['VERSION', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'conf', 'contrib', 'core', 'db', 'dispatch', 'forms', 'get_version', 'http', 'middleware', 'shortcuts', 'template', 'utils', 'views']
>>> 
>>> print django.__path__
['/opt/ilabs/django/django']
>>> print django.shortcuts
<module 'django.shortcuts' from '/opt/ilabs/django/django/shortcuts/__init__.pyc'>
>>> print django.shortcuts()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> print django.views
<module 'django.views' from '/opt/ilabs/django/django/views/__init__.pyc'>
>>> print django.http
<module 'django.http' from '/opt/ilabs/django/django/http/__init__.pyc'>
>>> from django.http import HttpResponse
>>> HttpResponse("Hello, world. You're at the poll index.")
<django.http.HttpResponse object at 0x86f8a8c>
>>> from test_pt import urls
>>> for u in urlpatterns:
...     print u
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'urlpatterns' is not defined
>>> for u in urls.urlpatterns:
...     print u
... 
<RegexURLPattern None ^addcontent>
<RegexURLPattern None ^listcontent>
<RegexURLPattern None ^savecontent>
<RegexURLPattern None ^flag_data>
>>> cc=Choice.objects.get(pk=6)
>>> cc.polls.question
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Choice' object has no attribute 'polls'
>>> cc.poll.question
u'this is my second question?how about it'
>>> cc=Choice.objects.get(choice_set="The sky")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/manager.py", line 131, in get
    return self.get_query_set().get(*args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 358, in get
    clone = self.filter(*args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 621, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 639, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1250, in add_q
    can_reuse=used_aliases, force_having=force_having)
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1122, in add_filter
    process_extras=process_extras)
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1316, in setup_joins
    "Choices are: %s" % (name, ", ".join(names)))
django.core.exceptions.FieldError: Cannot resolve keyword 'choice_set' into field. Choices are: choice_text, id, poll, votes
>>> cc=Choice.objects.get(choice_text="The sky")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/manager.py", line 131, in get
    return self.get_query_set().get(*args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 368, in get
    % (self.model._meta.object_name, num, kwargs))
test_pt.models.MultipleObjectsReturned: get() returned more than one Choice -- it returned 4! Lookup parameters were {'choice_text': 'The sky'}
>>> cc=Choice.objects.filter(choice_text="The sky")
>>> cc.poll
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'poll'
>>> cc.poll.question
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'poll'
>>> for c in cc:
...     c.poll.question
... 
u'this i smy first question?how about it'
u'this is my second question?how about it'
u'this i smy first question?how about it'
u'this is my third question?how about it'
>>> cc=Choice.objects.get(pk=1)
>>> cc.poll_set.all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Choice' object has no attribute 'poll_set'
>>> cc.poll
<Poll: Poll object>
>>> cc.poll.question
u'this i smy first question?how about it'
>>> cc=Choice.objects.filter(choice_text="The sky")
>>> cc.poll_set.all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'poll_set'
>>> from test_pt.models import Publication,Article
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name Publication
>>> from test_pt.models import Publication,Article
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name Publication
>>> test_pt.models.reload()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test_pt' is not defined
>>> test_pt.models.reload
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test_pt' is not defined
>>> import test_pt.models.reload
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named reload
>>> import test_pt.models.reload()
  File "<stdin>", line 1
    import test_pt.models.reload()
                                ^
SyntaxError: invalid syntax
>>> import test_pt.models
>>> reload(test_pt.models)
<module 'test_pt.models' from 'test_pt/models.pyc'>
>>> from test_pt.models import Publication,Article
>>> p=Publication(title="title1")
>>> p.save()
>>> Publication(title="title2").save()
>>> Publication(title="title3").save()
>>> Publication(title="title4").save()
>>> Publication(title="title5").save()
>>> Article(headline="headline1").save()
>>> a1=Article.objects.get(pk=1)
>>> #a1.publications.add([])
... 
>>> p=Publication.objects.filter(pk=1)
>>> a1.publications.add(p)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 578, in add
    self._add_items(self.source_field_name, self.target_field_name, *objs)
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 647, in _add_items
    '%s__in' % target_field_name: new_ids,
  File "/opt/ilabs/django/django/db/models/query.py", line 621, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 639, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1250, in add_q
    can_reuse=used_aliases, force_having=force_having)
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1185, in add_filter
    connector)
  File "/opt/ilabs/django/django/db/models/sql/where.py", line 69, in add
    value = obj.prepare(lookup_type, value)
  File "/opt/ilabs/django/django/db/models/sql/where.py", line 320, in prepare
    return self.field.get_prep_lookup(lookup_type, value)
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 139, in get_prep_lookup
    return [self._pk_trace(v, 'get_prep_lookup', lookup_type) for v in value]
  File "/opt/ilabs/django/django/db/models/fields/related.py", line 210, in _pk_trace
    v = getattr(field, prep_func)(lookup_type, v, **kwargs)
  File "/opt/ilabs/django/django/db/models/fields/__init__.py", line 312, in get_prep_lookup
    return [self.get_prep_value(v) for v in value]
  File "/opt/ilabs/django/django/db/models/fields/__init__.py", line 537, in get_prep_value
    return int(value)
TypeError: int() argument must be a string or a number, not 'QuerySet'
>>> p=Publication.objects.get(pk=1)
>>> a1.publications.add(p)
>>> p.article_set.all()
[<Article: headline1>]
>>> art=p.article_set.all()
>>> art.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> for i in art:
...     print i.id
...     print i.headline
...     print i.publication.id
... 
1
headline1
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AttributeError: 'Article' object has no attribute 'publication'
>>> for i in art:
...     print i.id
...     print i.publications.id
...     print i.headline
... 
1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
AttributeError: 'ManyRelatedManager' object has no attribute 'id'
>>> for i in art:
...     print i.publications_id
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'Article' object has no attribute 'publications_id'
>>> for i in art:
...     print dir(i.publications)
... 
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_items', '_clear_items', '_copy_to_model', '_db', '_inherited', '_insert', '_pk_val', '_remove_items', '_set_creation_counter', '_update', 'add', 'aggregate', 'all', 'annotate', 'bulk_create', 'clear', 'complex_filter', 'contribute_to_class', 'core_filters', 'count', 'create', 'creation_counter', 'dates', 'db', 'db_manager', 'defer', 'distinct', 'exclude', 'exists', 'extra', 'filter', 'get', 'get_empty_query_set', 'get_or_create', 'get_prefetch_query_set', 'get_query_set', 'in_bulk', 'instance', 'iterator', 'latest', 'model', 'none', 'only', 'order_by', 'prefetch_cache_name', 'prefetch_related', 'query_field_name', 'raw', 'remove', 'reverse', 'select_for_update', 'select_related', 'source_field_name', 'symmetrical', 'target_field_name', 'through', 'update', 'using', 'values', 'values_list']
>>> for i in art:
...     pp =i.publications.all()
...     for ii in pp:
...             print ii.id
... 
1
>>> a1 = Article.objects.get(pk=1)
>>> a1.publications.all()
[<Publication: title1>]
>>> a1.publications.all().id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> p1=a1.publications.all()
>>> p1.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> for p in p1:
...     print p.id
... 
1
>>> p2=Publication.objects.filter(title="title5")
>>> p2=Publication.objects.get(pk=2)
>>> p2.id
2L
>>> unicode(p2.id)
u'2'
>>> a4 = Article(headline='NASA finds intelligent life on Earth')
>>> a4.save()
>>> p2.article_set.add(a4)
>>> tt=p2.article_set.all()
>>> for t in tt:
...     t.headline
... 
u'NASA finds intelligent life on Earth'
>>> a4.publications.all()
[<Publication: title2>]
>>> a4.id
2L
>>> a4.delete()
>>> a4 = Article(headline='NASA finds intelligent life on Earth')
>>> a4.save()
>>> p2.article_set.add(a4)
>>> p2.delete()
>>> p2=Publication.objects.filter(id=2,title="title2")
>>> p2.save()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'save'
>>> p2=Publication(id=2,title="title2")
>>> p2.save()
>>> p2.article_set.add(a4)
>>> at=p2.article_set.all()
>>> at.delete()
>>> p2.article_set.clear()
>>> p2.article_set.add(a4)
>>> a4.save()
>>> a4.save()
>>> a5 = Article(headline='NASA finds intelligent life on Earth')
>>> a5.save()
>>> p2.article_set.add(a5)
>>> Article.objects.values_list(id)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/ilabs/django/django/db/models/manager.py", line 182, in values_list
    return self.get_query_set().values_list(*args, **kwargs)
  File "/opt/ilabs/django/django/db/models/query.py", line 585, in values_list
    _fields=fields)
  File "/opt/ilabs/django/django/db/models/query.py", line 864, in _clone
    c._setup_query()
  File "/opt/ilabs/django/django/db/models/query.py", line 988, in _setup_query
    self.query.add_fields(self.field_names, True)
  File "/opt/ilabs/django/django/db/models/sql/query.py", line 1649, in add_fields
    name.split(LOOKUP_SEP), opts, alias, False, allow_m2m,
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> Article.objects.values_list(id,headline)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'headline' is not defined
>>> Article.objects.values_list('id','headline')
[(1L, u'headline1'), (3L, u'NASA finds intelligent life on Earth'), (4L, u'NASA finds intelligent life on Earth')]
>>> Article.objects.values_list('id')
[(1L,), (3L,), (4L,)]
>>> 

"""
p.choice_set.create()
p.choice_set.all()
p.choice_set.count()
p.choice_set.filter(choice_text__startswith='Just hacking')

p.choice_set.clear()
Image.objects.all().order_by("-id")[0] //gets max(id)

Entry.objects.get(headline__contains='Lennon')

Roughly translates to this SQL:

SELECT ... WHERE headline LIKE '%Lennon%';


"""
