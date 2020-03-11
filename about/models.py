from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from django.utils import translation


class TranslatedField:
    def __init__(self, en_field, ro_field):
        self.en_field = en_field
        self.ro_field = ro_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'en':
            return getattr(instance, self.ro_field)
        else:
            return getattr(instance, self.en_field)


# Create your models here.
class AboutPage(Page):
    """About page class"""
    templates = "about/about_page.html"

    subtitle_ro = RichTextField()
    subtitle_en = RichTextField()
    content_ro = RichTextField()
    content_en = RichTextField()

    subtitle = TranslatedField(
        'subtitle_ro',
        'subtitle_en',
    )

    content = TranslatedField(
        'content_ro',
        'content_en',
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle_ro"),
        FieldPanel("subtitle_en"),
        FieldPanel("content_ro"),
        FieldPanel("content_en"),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"