from django.db import models
from django.contrib.auth.models import User
# for customer 
class Tiket(models.Model):
  title = models.CharField(max_length=100, verbose_name="عنوان")
  description = models.TextField(verbose_name="توضیحات")
  olaviat = models.CharField(max_length=20, verbose_name="اولویت")
  vaziat = models.CharField(max_length=20, default="باز", verbose_name="وضعیت")
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name="کاربر")

  def __str__(self):
    return f'{self.title}'

  class Meta:
      verbose_name = 'تیکت'
      verbose_name_plural = 'تیکت ها'
      ordering = ['-vaziat']

class ReplyTiket(models.Model):
  tiket = models.ForeignKey(
      Tiket, on_delete=models.DO_NOTHING, verbose_name=" پاسخ به", default=None)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="پاسخ دهنده")
  reply_message = models.TextField(verbose_name="پاسخ")

  class Meta:
      verbose_name = 'پاسخ به تیکت'
      verbose_name_plural = 'پاسخ ها به تیکت ها'
      ordering = ['user']

  def __str__(self):
    return f'{self.reply_to}'


  def __str__(self):
    return f'{self.reply_to}'

class Task(models.Model):
  tiket = models.ForeignKey(Tiket, on_delete=models.DO_NOTHING, verbose_name="مربوط به", default=None)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="انجام دهنده")
  creator = models.CharField(max_length=150, verbose_name="ایجاد کننده")
  task_message = models.TextField(verbose_name="پاسخ")

  class Meta:
      verbose_name = 'وظیفه'
      verbose_name_plural = 'وظایف'
      ordering = ['user']

  def __str__(self):
    return f'{self.tiket}'


class ReplyTask(models.Model):
  Task = models.ForeignKey(
      Task, on_delete=models.DO_NOTHING, verbose_name=" پاسخ به", default=None)
  user = models.ForeignKey(
      User, on_delete=models.DO_NOTHING, verbose_name="پاسخ دهنده")
  reply_message = models.TextField(verbose_name="پاسخ")

  class Meta:
      verbose_name = 'پاسخ به وظیفه'
      verbose_name_plural = 'پاسخ ها به وظایف'
      ordering = ['user']

