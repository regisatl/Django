from django import template

register = template.Library()

@register.simple_tag
def get_mangas(username):
      return f"hello {username} !"

