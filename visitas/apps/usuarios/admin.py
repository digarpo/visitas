from django.contrib import admin
from .models import User, UserCompany, UserWorkers, UserDepartment, UserCentral, UserDocs, UserAnexoTrobajo, UserAnexoParque
from .actions import export_as_excel


class DocsEnLinea(admin.StackedInline):
    model = UserAnexoTrobajo

class DocsEnLineaParque(admin.StackedInline):
    model = UserAnexoParque

class DocsEnLineaUser(admin.StackedInline):
    model = UserDocs



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_superuser',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]

    fieldsets = (
        ('Usuarios', {'fields': ('username', 'password')}),
        ('Informacion personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Permissions', {'fields': (
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
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_company',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]
    inlines = [DocsEnLinea,DocsEnLineaParque ]

    fieldsets = (
        ('Usuario', {'fields': ('username', 'password')}),
        ('Informacion personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Empresa', {'fields': (
            'name',
            'contact',
            'address',
            'phone',
            'mobile',
            'CIF',
            'activity',
           # 'revision',
            'subcontrate',

        )}),

        ('Permissions', {'fields': (
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
   # list_display = ('username', 'first_name', 'last_name', 'email','TC2')

  #  def get_TC2(self, instance):
   #     return instance.UserDocs.TC2

    search_fields = ('username', 'email')
   # list_filter = ('is_superuser',)

    actions = [export_as_excel]
    inlines = [DocsEnLineaUser]
    def author_name(self, instance):
        return instance.author.name



    fieldsets = (
        ('Usuario', {'fields': ('username', 'password')}),
        ('Informacion personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),
        ('Empresa', {'fields': (
            'name',
        )}),
        ('Trabajadores', {'fields': (
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




        ('Permissions', {'fields': (
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
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]

    fieldsets = (

        ('Usuarios', {'fields': ('username', 'password')}),
        ('Informacion personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),

        ('Departamento', {'fields': (
            'departament',
        )}),


        ('Permissions', {'fields': (
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


@admin.register(UserCentral)
class UserCentralita(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    actions = [export_as_excel]

    fieldsets = (

        ('Usuarios', {'fields': ('username', 'password')}),
        ('Informacion personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )}),

        ('Planta', {'fields': (
            'plant',
        )}),


        ('Permissions', {'fields': (
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
