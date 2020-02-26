from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our custom website"""
    facebook = models.CharField(max_length=200, blank=True, null=True, help_text="Facebook URL")
    twitter = models.CharField(max_length=200, blank=True, null=True, help_text="Twitter URL")
    google = models.CharField(max_length=200, blank=True, null=True, help_text="Google URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("google"),
        ], heading="Social Media Settings")
    ]


@register_setting
class GlobalSettings(BaseSetting):
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    site_title = models.CharField(blank=True, max_length=500)
    site_title_suffix = models.CharField(blank=True, max_length=500)
    site_description = models.CharField(blank=True, max_length=500)

    panels = [
        ImageChooserPanel('site_logo'),
        FieldPanel('site_title'),
        FieldPanel('site_title_suffix'),
        FieldPanel('site_description'),
    ]