from django.db import models

class cost_report (models.Model):
    report_id= models.CharField(max_length=100)
    report_desc= models.CharField(max_length=200)
    report_date=models.DateField('date of report')
    