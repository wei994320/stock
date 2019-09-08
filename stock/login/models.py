from django.db import models


# Create your models here.
class Focus(models.Model):
    # 创建字段，字段类型...
    note_info = models.CharField(max_length=200, default='')

    class Meta:
        db_table = 'focus'  # 指明数据库表名
        verbose_name = '股票'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.note_info


# 准备人物列表信息的模型类
class Info(models.Model):
    # GENDER_CHOICES = (
    #     (0, 'male'),
    #     (1, 'female')
    # )
    # 异常?
    code = models.CharField(max_length=10, null=False, verbose_name='股票代码')
    short = models.CharField(max_length=20, verbose_name='股票简称')
    chg = models.CharField(max_length=20, verbose_name='涨跌幅')
    turnover = models.CharField(max_length=255, verbose_name='换手率')
    price = models.FloatField(max_length=20, verbose_name='最新价')
    highs = models.FloatField(max_length=20, verbose_name='前期高点')
    time = models.DateField(null=False)

    class Meta:
        db_table = 'info'
        verbose_name = '股票'

    def __str__(self):
        return self.code
