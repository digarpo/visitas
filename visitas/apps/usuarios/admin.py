from django.contrib import admin
from .models import User, UserCompany, UserWorkers, UserDepartment
from .actions import export_as_excel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name','email')
    search_fields = ('username', 'email')
    list_filter = ('is_superuser',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]


    fieldsets = (
        ('Usuarios', {'fields': ('username', 'password')}),
        ('Informacion personal',{'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Permissions',{'fields': (
                                  'is_active',
                                   'is_staff',
                                  'is_superuser',
                                  'is_company',
                                  'is_worker',
                                  'is_usuario',
                                  'is_centralita',
                                  'is_coordinador',
                                  'groups',
                                  'user_permissions',
                                    )}),



    )
@admin.register(UserCompany)
class Company(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name','email')
    search_fields = ('username', 'email')
    list_filter = ('is_company',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]


    fieldsets = (
        ('Usuario', {'fields': ('username', 'password')}),
        ('Informacion personal',{'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Empresa',{'fields': (
            'name',
            'contact',
            'address',
            'phone',
            'mobile',
            'CIF',
            'activity',
            'revision',
            'subcontrate',
        )}),

        ('Permissions',{'fields': (
                                  'is_active',
                                   'is_staff',
                                  'is_superuser',
                                  'is_company',
                                  'is_worker',
                                  'is_usuario',
                                  'is_centralita',
                                  'is_coordinador',
                                  'groups',
                                  'user_permissions',
                                    )}),



    )
@admin.register(UserWorkers)
class UserWorker(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name','email')
    search_fields = ('username', 'email')
    list_filter = ('is_superuser',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]


    fieldsets = (
        ('Usuario', {'fields': ('username', 'password')}),
        ('Informacion personal',{'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Empresa',{'fields': (
            'name',
        )}),
        ('Trabajadores',{'fields': (
            'nameWorker',
            'TA2_date',
            'TA2_doc',
            'medical',
            'information',
            'formation_date',
            'EPI_date',
            'EPI_doc',
            'medical_doc',
            'information_doc',
            'skill_doc',
        )}),

        ('Permissions',{'fields': (
                                  'is_active',
                                   'is_staff',
                                  'is_superuser',
                                  'is_company',
                                  'is_worker',
                                  'is_usuario',
                                  'is_centralita',
                                  'is_coordinador',
                                  'groups',
                                  'user_permissions',
                                    )}),



    )

@admin.register(UserDepartment)
class UserDepartments(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name','email')
    search_fields = ('username', 'email')
    list_filter = ('is_company',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]


    fieldsets = (
            ('Departamento',{'fields': (
            'department',
        )}),


        ('Permissions',{'fields': (
                                  'is_active',
                                   'is_staff',
                                  'is_superuser',
                                  'is_company',
                                  'is_worker',
                                  'is_usuario',
                                  'is_centralita',
                                  'is_coordinador',
                                  'groups',
                                  'user_permissions',
                                    )}),



    )
