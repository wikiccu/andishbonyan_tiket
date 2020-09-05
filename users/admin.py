from django.contrib import admin
from users.models import Inqueries,Reply
admin.site.site_header = 'مدیریت تیکت ها '
admin.site.register(Inqueries)
admin.site.register(Reply)
