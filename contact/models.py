from django.db import models

from wagtail.core.models import Page
from django.utils import translation
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

from streams import blocks


class TranslatedField:
    def __init__(self, en_field, ro_field):
        self.en_field = en_field
        self.ro_field = ro_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'en':
            return getattr(instance, self.ro_field)
        else:
            return getattr(instance, self.en_field)


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm, Page):
    templates = "contact/contact_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content = StreamField(
        [
            ("team_block", blocks.TeamBlock())
        ],
        blank=True,
        null=True,
        default=[],
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        StreamFieldPanel("content"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col-6"),
                FieldPanel("to_address", classname="col-6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"
