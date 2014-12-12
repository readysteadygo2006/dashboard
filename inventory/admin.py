from django.contrib import admin

# Register your models here.
from .models import Inventory, Machine, Playbook, Role, RoleStatus, PlaybookStatus

admin.site.register(Inventory)
admin.site.register(Machine)
admin.site.register(Playbook)
admin.site.register(Role)
admin.site.register(RoleStatus)
admin.site.register(PlaybookStatus)
