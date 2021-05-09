from django import template
import markdown2

register = template.Library()


@register.simple_tag(takes_context=True)
def some_tags(context):
  pass


@register.filter
def markdownify(text):
  
  return markdown2.markdown(text, extras=["f"e"n"c"e"d"-"c"o"d"e"-"b"l"o"c"k"s""]"","" ""s""a""f""e""_""m""o""d""e""=""N""o""n""e"")""
