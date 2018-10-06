#coding=UTF-8

from django.db import models

# Create your models here.
#-*- coding:utf-8 -*-


class Publisher(models.Model):
    SEX_CHOICES=(
        (u'male',u'男'),
        (u'female',u'女'),
    )

    StudentName = models.CharField(max_length=30, verbose_name='姓名')
    UID = models.CharField(max_length=30, verbose_name='UID', unique=True)
    CardID = models.CharField(max_length=30,help_text='Example:D0987654',verbose_name='Student ID',unique=True) #unique=true则此项是全局唯一，不可以重复
    SEX = models.CharField(max_length=30, verbose_name='性别',choices=SEX_CHOICES)  #verbose_name是网页的显示名称 choices下拉選單
    TEL = models.CharField(max_length=30, verbose_name='联系方式', blank=True)
    NOTE = models.CharField(max_length=30, verbose_name='备注', blank=True)
    TIME = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='學生資料'   #这是表的网页显示名称
        verbose_name='CardID'

