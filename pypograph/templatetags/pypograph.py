from django import template
from pypograph import Pypograph

register = template.Library()
typograph = Pypograph()


@register.filter
def typo(text):
    return pypograph.typo(text)


@register.tag('typo')
class TypoNode(template.Node):

    def __init__(self, parser, token):
        self.nodelist = parser.parse(('endtypo', ))
        parser.delete_first_token()

    def render(self, context):
        output = self.nodelist.render(context)
        return typograph.typo(output)
