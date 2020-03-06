from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """Homepage model"""
    templates = "home/home_page.html"
    # max_count = 1

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_title_en = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
