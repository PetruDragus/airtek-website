from .models import MenuItem
from contact.models import ContactPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(MenuItem)
class MenuItemTR(TranslationOptions):
    fields = (
        'link_title',
    )


