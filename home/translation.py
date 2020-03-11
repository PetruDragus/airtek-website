from .models import HomePage

from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'hero_title',
        'hero_subtitle',
    )