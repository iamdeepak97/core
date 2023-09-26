from django.contrib import admin
from recipebook.models import recipes



class recipess(admin.ModelAdmin):
    list_display=("title","description","image","created_at","User")
admin.site.register(recipes,recipess)
# Register your models here.
