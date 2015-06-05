from pypograph.typograph import DEFAULT_RULES
from django.conf import settings
from pypograph import Typograph
from django import template

TYPOGRAPH_RULES = getattr(settings, 'TYPOGRAPH_RULES', DEFAULT_RULES)
typograph = Typograph(TYPOGRAPH_RULES)
register = template.Library()


@register.filter
def typo(text):
    return typograph.typo(text)


@register.tag('typo')
class TypoNode(template.Node):

    def __init__(self, parser, token):
        self.nodelist = parser.parse(('endtypo', ))
        parser.delete_first_token()

    def render(self, context):
        output = self.nodelist.render(context)
        return typograph.typo(output)
