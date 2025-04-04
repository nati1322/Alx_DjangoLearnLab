from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year','created_by')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'library_card_number', 'date_of_birth', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'library_card_number', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'library_card_number', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

def create_groups():
    content_type = ContentType.objects.get_for_model(Book)

    # Define or get permissions
    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
    }

    # Create or get groups
    editors_group, _ = Group.objects.get_or_create(name="Editors")
    viewers_group, _ = Group.objects.get_or_create(name="Viewers")
    admins_group, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    editors_group.permissions.set([permissions["can_create"], permissions["can_edit"]])
    viewers_group.permissions.set([permissions["can_view"]])
    admins_group.permissions.set(list(permissions.values()))

    print("Groups and permissions set up successfully.")

# Run the function when the app loads
create_groups()