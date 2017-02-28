from django.db import models
from catalog.models import Tool
from accounts.models import TempCarpenter


# Create your models here.
class LentTool(models.Model):
    tool = models.ForeignKey(Tool)
    temp_carpenter = models.ForeignKey(TempCarpenter)
    lend_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    lending_fee = models.FloatField()
    damage_fee = models.FloatField(null=True)

    def __str__(self):
        return self.tool+"<->"+self.temp_carpenter
