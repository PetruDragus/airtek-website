from home.models import HomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'banner_title',
        'title',
    )
