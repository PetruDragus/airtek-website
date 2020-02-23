from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
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