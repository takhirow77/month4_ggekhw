from django.contrib import admin

from apps.base.models import Settings
from apps.secondary.models import Services,Projects,Education,Skills,Parfolio,Review,Blog
# Register your models here.

admin.site.register(Settings)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Parfolio)
admin.site.register(Review)
admin.site.register(Blog)