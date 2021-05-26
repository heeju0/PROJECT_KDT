from django import template
register = template.Library()

@register.filter
def union_list(lst1, lst2):
    return list(set(lst1 + lst2))


@register.filter
def ranges(a):
    return range(a)