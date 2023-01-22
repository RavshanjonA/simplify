from django.contrib import admin
from parler.admin import TranslatableAdmin

from simpleapp.models import Blog, Service


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    pass

@admin.register(Service)
class BlogAdmin(TranslatableAdmin):
    pass
