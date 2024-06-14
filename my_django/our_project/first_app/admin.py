from django.contrib import admin
from first_app.models import AccessRecord, Webapage, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webapage)
admin.site.register(AccessRecord)
