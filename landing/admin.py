from django.contrib import admin
from landing.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('CIN','nom','prenom')
    def CIN(self, x):
    	return x.user.username

admin.site.register(Person, PersonAdmin)