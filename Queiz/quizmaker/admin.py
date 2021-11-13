from django.contrib import admin

from .models import Q,A,U,Quiz
# Register your models here.
admin.site.register(Q)
admin.site.register(A)
admin.site.register(U)
admin.site.register(Quiz)



class Qinline(admin.TabularInline):
    fields = ("choice","category")
    model = Q

class AAdmin(admin.ModelAdmin):
    inlines = [
        Qinline,
    ]




