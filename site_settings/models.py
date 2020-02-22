from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
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