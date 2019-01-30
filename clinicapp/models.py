from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserRegistration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)



def __str__(self):
    return self.user.username


class patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=64)
    weight = models.FloatField()
    address = models.TextField()
    contact_no = models.CharField(max_length=12)
    email_id = models.EmailField()

class appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    doctor_name = models.CharField(max_length=64)
    symtomps = models.TextField()
    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)


class diagnosis(models.Model):
    dignosis_id = models.IntegerField(primary_key=True)
    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    dignosis_type = models.TextField()
    dignosis_name = models.CharField(max_length=64)

class medicine(models.Model):
    medicine_id = models.IntegerField(primary_key=True)
    medicine_name = models.CharField(max_length=64)
    diagnosis_id = models.ForeignKey(diagnosis, on_delete=models.CASCADE)

class history(models.Model):
    history_id = models.IntegerField(primary_key=True)
    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicine, on_delete=models.CASCADE)
class bill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    medicine_id = models.ForeignKey(medicine,on_delete=models.CASCADE)
    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    amount = models.IntegerField()

class MR(models.Model):
    mr_id=models.IntegerField(primary_key=True)
    mr_name=models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    medicine = models.CharField(max_length=64)
    date= models.DateField()

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=64)
    staff_type = models.CharField(max_length=64)
    salary = models.CharField(max_length=64)

class ClientRegistration(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=64)
    client_Address= models.CharField(max_length=64)
    contact = models.CharField(max_length=12)
    email = models.EmailField()