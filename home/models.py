from django.db import models

from wagtail.admin.edit_handlers import \
    FieldPanel, \
    StreamFieldPanel, \
    MultiFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks
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


class HomePage(Page):
    """Homepage model"""
    templates = "home/home_page.html"
    # max_count = 1

    hero_title = models.CharField(max_length=100, blank=True, null=True)
    hero_subtitle = models.TextField(blank=True, null=True)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    background_vertical = models.CharField(max_length=100, blank=True, null=True)
    background_horizontal = models.CharField(max_length=100, blank=True, null=True)

    content = StreamField(
        [
            ("main_block", blocks.MainBlock())
        ],
        blank=True,
        null=True,
        default=[]
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                ImageChooserPanel('hero_image'),
                FieldPanel('background_vertical'),
                FieldPanel('background_horizontal'),
            ], "Hero"
        ),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
