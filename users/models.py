from django.db import models
from django.contrib.auth.models import User
# for customer 
class Inqueries(models.Model):
  title = models.CharField(max_length=100, verbose_name="عنوان")
  description = models.TextField(verbose_name="توضیحات")
  olaviat = models.CharField(max_length=20, verbose_name="اولویت")
  vaziat = models.CharField(max_length=20, default="باز", verbose_name="وضعیت")
  cuser = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name="کاربر")
  erja = models.IntegerField(max_length=100, default=0, verbose_name="ارجاع به")

  def __str__(self):
    return f'{self.title}'

  class Meta:
      verbose_name = 'تیکت'
      verbose_name_plural = 'تیکت ها'
      ordering = ['-vaziat']

class Reply(models.Model):
  reply_to = models.ForeignKey(Inqueries, on_delete=models.DO_NOTHING, verbose_name=" پاسخ به")
  wuser = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="پاسخ دهنده")
  reply_message = models.TextField(verbose_name="پاسخ")

  class Meta:
      verbose_name = 'پاسخ'
      verbose_name_plural = 'پاسخ ها'
      ordering = ['wuser']

  def __str__(self):
    return f'{self.reply_to}'

#for admin-programmer


#for programmer 
