from django.contrib import admin
from .models import Camp, CampInstance, ChildrenCamp, CampReview, Profilis, Reservation, AdultCamp, Package

class CampInstanceInline(admin.TabularInline):
    model =CampInstance
    readonly_fields = ('id',)
    can_delete = False
    extra = 0

class CampAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary')
    inlines = [CampInstanceInline]
    
class ChildrensAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'capacity')

class AdultCampAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'capacity')

class CampInstanceAdmin(admin.ModelAdmin):
    list_display = ('camp','due_back','unavailable', 'status', 'consumer')

class CampReviewAdmin(admin.ModelAdmin):
    list_display = ('camp', 'date_created', 'reviewer', 'content')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'campsite', 'check_in', 'check_out' )

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

admin.site.register(CampReview, CampReviewAdmin)
admin.site.register(Camp, CampAdmin)
admin.site.register(CampInstance, CampInstanceAdmin)
admin.site.register(ChildrenCamp, ChildrensAdmin)
admin.site.register(Profilis)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(AdultCamp, AdultCampAdmin)
admin.site.register(Package, PackageAdmin)

# Register your models here.
