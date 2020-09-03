from django.db import models
from django.contrib.auth.models import User
# for customer 
def Inqueries():
  title=models.CharField(max_length=100)
  description = models.TextField()
  olaviat = models.TextField()
  vaziat = models.TextField()
  erja = models.ForeignKey(User,on_delete=models.DO_NOTHING,nullable=True,blank=True)
  

#for admin



#for admin-programmer


#for programmer 
