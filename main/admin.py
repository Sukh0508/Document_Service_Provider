from django.contrib import admin
from .models import Coreservices , Logo , Document_img , Contact

admin.site.site_header = "Document Service Provider"
admin.site.site_title = "Admin Login"
admin.site.index_title = "Welcome to Admin Panel"

admin.site.register(Coreservices)
admin.site.register(Logo) 
admin.site.register(Contact)
admin.site.register(Document_img)

# Register your models here.
