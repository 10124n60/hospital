from django.db import models


class Spetiality(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=10, choices=[('Male','Male'),('Female','Female')])
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Medic(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=11)
    spetiality = models.ForeignKey(Spetiality,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Service(models.Model):
    name = models.CharField(max_length=256)
    description= models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMLETED = 'COMLETED'
    CANCELED = 'CANCELED'

    STATUS_CHOICES = [
        (PLANNED,PLANNED),
        (COMLETED,COMLETED),
        (CANCELED,CANCELED)
    ]



    medic = models.ForeignKey(Medic,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True)
    planned_date = models.DateTimeField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.medic} * {self.patient} * {self.planned_date}"

