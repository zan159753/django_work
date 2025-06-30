# tasks.py
import logging
import random
import string
from time import sleep

from celery import shared_task


from celery import shared_task
import subprocess
import platform

from demo.models import Host


@shared_task
def rotate_host_passwords():
    print("Rotating passwords...")
    hosts = Host.objects.all()
    for host in hosts:
        host.change_password()


from collections import defaultdict
from .models import HostStat
import pytz
from datetime import datetime

@shared_task
def daily_host_stats():
    stats = defaultdict(lambda: defaultdict(int))

    # # 获取当前日期（东八区）
    from django.utils import timezone

    shanghai_tz = pytz.timezone('Asia/Shanghai')

    today = datetime.now(shanghai_tz).date()

    # 按城市和机房统计
    for host in Host.objects.select_related('room__city'):
        city = host.room.city.name
        room = host.room.name
        stats[city][room] += 1

    # 批量创建或更新统计数据
    stat_objects = []
    for city, rooms in stats.items():
        for room, count in rooms.items():
            stat_objects.append(
                HostStat(
                    city=city,
                    room=room,
                    host_count=count,
                    date=today
                )
            )

    # 批量插入前先删除当天已有数据（防止重复）
    HostStat.objects.filter(date=today).delete()

    # 批量插入新数据
    HostStat.objects.bulk_create(stat_objects)

