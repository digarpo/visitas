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

