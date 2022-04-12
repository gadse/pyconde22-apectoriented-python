# Base

- Aspect-Oriented stuff = Cross-cutting concerns that are NOT business-logic
- Closure = (Pre-)Parameterized function
- You could actually write "decorators" that simply override the decorated function and so something completely different, but that's usually not intended.
- Decorated functions are decorated at definition time - not at call time.
- Wrapping stuff trivially erazes func names... Use functools.wraps and use it on the wrapped function. It's still a different function, but python only cares for names and behavior, so that's fine here.
- Note that @wraps() has problems with recursion

```
@dec
def foo():
    pass

does the same as

foo = dec(foo)
```


# Use Cases

## Caching

The stuff in cached.py explains the concept, but shouldn't be used in prod in this form. (Not able to invalidate cache, file handles can't be pickled, etc.) --> Probably use LRU-Cache provided by Python or just improve the cache solution.


## Logging

==> Highly interesting for DS!
If logging overhead is interesting and


## Registry

Could be used for things like plugins. --> DS scanners?


# Parameterization

You can do this by wrapping your wrapper again!

# Callable classes and decorators

Implemented by adding a `__call__` method. We can use callebla classes to implement decorators --> might be nicer if we need to store stuff like cached results, since the storage doesn just "float around" in our module namespace.

Also, with this, you can map the decorator parameterization onto the `__init__` method.


# Class Decorators

```python
def mark(cls):
    cls.new = 100
    return cls

@mark
class A:
    pass

assert A().new == 100
```

Members added by class decorators are NOT inherited by subclasses.


# Q&A

> When to switch from func to class? Whatever makes sense and is more understandable.

