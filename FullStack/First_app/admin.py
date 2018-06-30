from django.contrib import admin
from First_app.models import Topic ,AccessRecord, Webpage,UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)
