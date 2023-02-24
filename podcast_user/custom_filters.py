from django import template

register = template.Library()

@register.filter
def add_line_breaks(value, arg):
    sentences = value.split(". ")
    num_sentences = int(arg)
    return "<br>".join([". ".join(sentences[i:i+num_sentences]) for i in range(0, len(sentences), num_sentences)])