from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


# Create your models here.
class ProductPage(Page):
    """Product page class"""
    templates = "product/product_page.html"

    subtitle = models.CharField(max_length=200, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "Product Page"
        verbose_name_plural = "Product Pages"