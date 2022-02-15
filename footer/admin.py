from django.contrib import admin
from footer.models import FooterLogoMeta, FooterMenusMeta, FooterContactsMeta, FooterServicesMeta


class FooterLogoAdmin(admin.ModelAdmin):
    list_display = ['description', 'image_tag']
    readonly_fields = ['image_tag']


class FooterMenusAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class FooterContactsAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'address']


class FooterServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(FooterLogoMeta, FooterLogoAdmin)
admin.site.register(FooterMenusMeta, FooterMenusAdmin)
admin.site.register(FooterContactsMeta, FooterContactsAdmin)
admin.site.register(FooterServicesMeta, FooterServicesAdmin)
