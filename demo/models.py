from django.db import models
import secrets
import string
from django.utils import timezone

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('city', 'name')

    def __str__(self):
        return f"{self.city.name} - {self.name}"

class Host(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(unique=True)
    root_password = models.CharField(max_length=255)  # 加密存储密码
    last_password_change = models.DateTimeField(auto_now_add=True)

    def change_password(self):
        self.root_password = generate_random_password()
        self.last_password_change = timezone.now()
        self.save()

class HostStat(models.Model):
    city = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    host_count = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
