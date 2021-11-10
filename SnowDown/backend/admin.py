from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import Animal_Table, SubAnimal_Table, Incident_Photos_Table, Incident_Table,\
    Group_Incident_Table, TokenIssued, Ticket_Type, Observer_Type, Sector, SealSize, Sex,\
        TagSide, TagColor, Status, Death, FAST, Location, How_ID, Island

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
admin.site.register(Incident_Photos_Table)
admin.site.register(TokenIssued)
admin.site.register(Incident_Table)
admin.site.register(Group_Incident_Table)
admin.site.register(Ticket_Type)
admin.site.register(Observer_Type)
admin.site.register(Sector)
admin.site.register(SealSize)
admin.site.register(Sex)
admin.site.register(TagSide)
admin.site.register(TagColor)
admin.site.register(Status)
admin.site.register(Death)
admin.site.register(FAST)
admin.site.register(Location)
admin.site.register(How_ID)
admin.site.register(Island)