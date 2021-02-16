from django.contrib import admin
from app.models import AccessRecord,Topic, Webpage, User
from app.forms import NewUserForm

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
