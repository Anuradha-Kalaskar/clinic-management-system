from django.contrib import admin
from clinicapp.models import UserRegistration, User, patient, appointment,diagnosis, medicine, history, bill,MR, Staff, ClientRegistration

# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id','patient_name','age','gender','weight','address')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'date', 'doctor_name', 'symtomps', 'patient_id')


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('dignosis_id', 'patient_id', 'dignosis_type', 'dignosis_name')


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'diagnosis_id')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'medicine_id')


class BillAdmin(admin.ModelAdmin):
    list_display = ('date', 'medicine_id','patient_id','amount')

class MRAdmin(admin.ModelAdmin):
    list_display = ('mr_id','mr_name','company','medicine','date')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'staff_type', 'salary')


admin.site.register(UserRegistration)
admin.site.register(patient, PatientAdmin)
admin.site.register(appointment, AppointmentAdmin)
admin.site.register(diagnosis, DiagnosisAdmin)
admin.site.register(medicine, MedicineAdmin)
admin.site.register(history, HistoryAdmin)
admin.site.register(bill, BillAdmin)
admin.site.register(MR, MRAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(ClientRegistration)