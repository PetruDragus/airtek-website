from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from django.utils import translation


# Create your models here.
class TranslatedField:
    def __init__(self, en_field, ro_field):
        self.en_field = en_field
        self.ro_field = ro_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'en':
            return getattr(instance, self.ro_field)
        else:
            return getattr(instance, self.en_field)


class TermsPage(Page):
    """Terms page class"""
    templates = "terms/terms_page.html"

    page_title = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Terms Page"
        verbose_name_plural = "Terms Pages"