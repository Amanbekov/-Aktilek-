from django.contrib import admin
from main.models import (
     School, Teacher, Gallery,
      Review, New,
)

admin.site.register(School)
admin.site.register (Teacher)
admin.site.register (Gallery)
admin.site.register (Review)
admin.site.register (New)



