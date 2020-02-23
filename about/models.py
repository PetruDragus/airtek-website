from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class AboutPage(Page):
    """About page class"""
    templates = "about/about_page.html"

    subtitle = RichTextField()
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"