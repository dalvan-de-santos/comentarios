from django.contrib import admin
from .models import comentario

@admin.register(comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'texto', 'data_criacao')
    search_fields = ('user__username', 'texto')
    list_filter = ('data_criacao',)

    
