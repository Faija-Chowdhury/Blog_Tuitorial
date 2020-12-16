from django.contrib import admin
from .models import about
from .models import slider
from .models import privacy
from .models import term

admin.site.register(about)
admin.site.register(slider)
admin.site.register(privacy)
admin.site.register(term)