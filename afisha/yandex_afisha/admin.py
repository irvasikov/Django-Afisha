from django.contrib import admin
from django.utils.html import format_html

from .models import Places, Images


class ImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ("image_shot",)

    def image_shot(self, obj):
        return format_html("<img src=\"{}\" width={} height={} />",
                           obj.image.url,
                           "auto",
                           "200",
                           )

class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    class Meta:
        model = Places


# class ImagesAdmin(admin.ModelAdmin):



admin.site.register(Places, PlacesAdmin)
admin.site.register(Images)



