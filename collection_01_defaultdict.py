from collections import defaultdict

items: list[tuple[str, int]] = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('a', 5), ('b', 6)]

d: defaultdict[str, list] = defaultdict(list)
x: dict = {}

for k,v in items:
    d[k].append(v)
    x[k] = v

print(type(items))
print(items)

print(d)
print(x)


# This is the default factory example
d_default_factory: defaultdict[str, str] = defaultdict(lambda: '<missing>')
d_default_factory['a'] = 'Apple'
d_default_factory['b'] = 'Banana'

print(d_default_factory)
print(d_default_factory['a'])
print(d_default_factory['no_such_key'])