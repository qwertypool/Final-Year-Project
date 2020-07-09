from django.contrib import admin
from home.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','time','content']


# Register your models here.




admin.site.register(Contact,ContactAdmin)