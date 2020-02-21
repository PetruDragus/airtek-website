from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


# Create your models here.
class ContactPage(Page):
    """Contact page class"""
    templates = "about/about_page.html"

    subtitle = models.CharField(max_length=200, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"