from django.contrib import admin
from .models import EmployeeDetail, Activity
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.fields import widgets
# Register your models here.

admin.site.site_header = "Portal Administration"
admin.site.set_title = "Admin Panel"
admin.site.index_title = "Welcome To Admin Panel..."
admin.site.site_title = "Portal Administration"


@admin.action(description="Approve User")
def approve_user(modeladmin, request, queryset):
    for item in queryset:
        item.user.is_active = True
        item.user.save()


@admin.action(description="Remove User")
def remove_user(modeladmin, request, queryset):
    for item in queryset:
        item.user.is_active = False
        item.user.save()


@admin.register(EmployeeDetail)
class Employee(admin.ModelAdmin):
    list_display = ['id', "user", "first_name", "last_name", "designation", "department", "mobile_number", "approved"]
    list_filter = ["user__is_active"]
    actions = [approve_user, remove_user]

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def approved(self, obj):
        return obj.user.is_active

    approved.short_description = "active"
    approved.boolean = True


class ActivityResource(resources.ModelResource):
    date = Field(attribute='activity_at', column_name='date', widget=widgets.DateTimeWidget(format='%d %B %Y'))
    time = Field(attribute='activity_at', column_name='time', widget=widgets.DateTimeWidget(format='%H:%M %p'))

    class Meta:
        model = Activity
        fields = ('id', "user__first_name", "user__last_name", "activity", "date", "time",)


@admin.register(Activity)
class UserActivity(ImportExportModelAdmin):
    list_display = ['id', "first_name", "last_name", "activity", "date", "time"]
    list_filter = ["activity", "activity_at"]
    resource_classes = [ActivityResource]

    def date(self, obj):
        return obj.activity_at.strftime("%d %B %Y")

    def time(self, obj):
        return obj.activity_at.strftime("%H:%M %p")

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

