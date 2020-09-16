from django.contrib import admin
from users.models import (ReplyTask,ReplyTiket,Task,Tiket)
admin.site.site_header = 'مدیریت تیکت ها '
admin.site.register((ReplyTask, ReplyTiket, Task, Tiket))

