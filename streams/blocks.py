
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class MainBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    subtitle = blocks.TextBlock(required=True, help_text='Add subtitle text')

    class Meta:
        template = "streams/main_block.html"
        icon = "edit"
        label = "Main Block"


class TeamBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add title"),
    name = blocks.CharBlock(required=True, help_text="Add block title"),
    phone = blocks.CharBlock(required=True, help_text="Add phone number"),
    email = blocks.CharBlock(required=True, help_text="Add email address")

    class Meta:
        template = "streams/team_block.html"
        icon = "edit"
        label = "Team Block"