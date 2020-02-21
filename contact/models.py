from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


# Create your models here.
class ContactPage(Page):
    """Contact page class"""
    templates = "contact/contact_page.html"

    subtitle = models.CharField(max_length=200, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"