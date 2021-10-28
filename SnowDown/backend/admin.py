from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import Animal_Table, SubAnimal_Table, Animal_Characteristics_Table, Incident_Photos_Table, Incident_Table, Incident_Before_Photos_Table,\
    Incident_After_Photos_Table, Group_Incident_Table, TokenIssued

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name', 'Last_name', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'Last_name', 'Picture')}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'Last_name', 'Picture', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(SubAnimal_Table)
admin.site.register(Animal_Table)
admin.site.register(Animal_Characteristics_Table)
admin.site.register(Incident_Photos_Table)
admin.site.register(TokenIssued)
admin.site.register(Incident_Table)
admin.site.register(Group_Incident_Table)
admin.site.register(Incident_Before_Photos_Table)
admin.site.register(Incident_After_Photos_Table)