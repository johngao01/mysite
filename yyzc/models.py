from django.db import models


class Statistics(models.Model):
    month = models.IntegerField(primary_key=True)
    total_num = models.IntegerField(null=True)
    reject = models.IntegerField(null=True)
    arrive = models.IntegerField(null=True)
    reject_rating = models.FloatField(null=True)
    times = models.FloatField(null=True)

    class Meta:
        db_table = 'statistics'  # 指定数据库表的名称
