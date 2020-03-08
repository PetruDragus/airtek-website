
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class MainBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    subtitle = blocks.TextBlock(required=True, help_text='Add subtitle text')

    class Meta:
        template = "streams/main_block.html"
        icon = "edit"
        label = "Main Block"