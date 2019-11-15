from django.contrib import admin

# Register your models here.

# 生成ADMIN后台可操作的表项

from app01.models import User,Role,Permission

class RoleConfig(admin.ModelAdmin):
    list_display = ["pk","title"]
    ordering = ["pk"]
admin.site.register(Role,RoleConfig)

class UserConfig(admin.ModelAdmin):
    list_display = ["name","pwd"]
    ordering = ["pk"]
admin.site.register(User,UserConfig)

# 自定义后台显示的字段等信息
class PermissionConfig(admin.ModelAdmin):
    list_display = ["pk","title","url"]
    ordering = ["pk"]
admin.site.register(Permission,PermissionConfig)