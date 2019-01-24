from django.contrib import admin
from pmkdata.members.models import Department, Major, Member


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    list_display_links = ['code']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['department', 'code', 'name', 'nim_prefix', 'tpb']
    list_display_links = ['code']
    list_filter = ['department', 'is_tpb']

    def tpb(self, obj):
        return obj.is_tpb
    tpb.boolean = True


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['nim', 'name', 'nickname', 'year', 'major', 'status']
    list_display_links = ['name']
    list_filter = ['year', 'status', 'major']
    search_fields = ['name', 'nickname']
