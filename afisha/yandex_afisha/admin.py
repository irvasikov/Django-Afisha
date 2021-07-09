from django.contrib import admin

from .models import Places, Images


class ImageInline(admin.TabularInline):
    model = Images


class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    class Meta:
        model = Places
    pass


admin.site.register(Places, PlacesAdmin)
admin.site.register(Images)



