from django.contrib import admin
from . models import GolfCourse, Hole

class HoleInline (admin.TabularInline):
    model = Hole
    max_num = 18
    can_delete = False
    exclude = ['hole_id']
    
    def has_delete_permission(self, request, obj=None):
        return False

class GolfCourseAdmin (admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['course_name']}),
        ('Course Total Par', {'fields': ['course_total_par']}),]
    inlines = [HoleInline]
    exclude = ['course_id']
    actions_on_top = False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register (GolfCourse, GolfCourseAdmin)
