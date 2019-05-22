from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pmkdata.members.models import Department, Major, Member


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


class MajorResource(resources.ModelResource):
    class Meta:
        model = Major


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ['code', 'name']
    list_display_links = ['code']


@admin.register(Major)
class MajorAdmin(ImportExportModelAdmin):
    resource_class = MajorResource
    list_display = ['department', 'code', 'name', 'nim_prefix', 'tpb']
    list_display_links = ['code']
    list_filter = ['department', 'is_tpb']

    def tpb(self, obj):
        return obj.is_tpb
    tpb.boolean = True


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ['nim', 'name', 'nickname', 'year', 'major', 'status']
    list_display_links = ['name']
    list_filter = ['year', 'status', 'major']
    search_fields = ['name', 'nickname']
