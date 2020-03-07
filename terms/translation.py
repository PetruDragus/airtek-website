from terms.models import TermsPage
from contact.models import ContactPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(TermsPage)
class TermsPageTR(TranslationOptions):
    fields = (
        'page_title',
        'content',
    )


