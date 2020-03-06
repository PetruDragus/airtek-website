from .models import ContactPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(ContactPage)
class FooTR(TranslationOptions):
    fields = (
        'intro',
    )