from django.contrib import admin
from app.models import Facility, State,City, Hospitals , Availablity 
# Register your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save , sender=Hospitals)
def afterHospitalSave(signal , instance , **kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
       availability =  Availablity(hospital=instance , facility = facility)
       availability.save()


@receiver(post_save , sender=Facility)
def afterFacilitySave(signal , instance , **kwargs):
    hospitals = Hospitals.objects.all()
    for hospital in hospitals:
       availability =  Availablity(hospital=hospital , facility = instance)
       availability.save()

class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display = ['title']
class HospitalAdmin(admin.ModelAdmin):
    model=Hospitals
    list_display=['name' , 'phone' , 'address' , 'city']
class CityAdmin(admin.ModelAdmin):
    model=City
    list_display=['name' , 'state']
class StateAdmin(admin.ModelAdmin):
    model=State
    list_display=['name']
class AvailablityAdmin(admin.ModelAdmin):
    model=Availablity
    list_display=['hospital' , 'facility' , 'total' , 'available' , 'updated_at']
    list_editable=['available','total']
admin.site.register(State , StateAdmin)
admin.site.register(City , CityAdmin)
admin.site.register(Hospitals , HospitalAdmin)
admin.site.register(Facility , FacilityAdmin)
admin.site.register(Availablity , AvailablityAdmin)

