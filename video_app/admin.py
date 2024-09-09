from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin
 
# Register your models here.
class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass



admin.site.register(Video)