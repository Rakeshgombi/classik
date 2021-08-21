from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(
        max_length=300, blank=True, null=True, default="")
    courseSection = models.CharField(
        max_length=300, blank=True, null=True, default="")
    courseDesc = models.TextField(blank=True, null=True, default="")
    courseRefNo = models.CharField(max_length=6)
    courseCreator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Creator")
    courseStudent = models.ManyToManyField(
        User, blank=True, related_name="Disciples")
    theme = models.CharField(default="", max_length=10)
    def __str__(self):
        return self.courseName


class Announcemet(models.Model):
    annMaterial = models.ForeignKey(
        Course, on_delete=models.CASCADE,  related_name='Announcements')
    annTitle = models.CharField(
        max_length=1000, null=True, blank=True, default="")
    annFile = models.FileField(upload_to="files/", blank=True, null=True)
    annContent = models.TextField(blank=True, null=True, default="")
    annTimestamp = models.DateTimeField(auto_now_add=True)
    annCreator = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", null=True, related_name="AnnouncementCreator")

    def __str__(self):
        if len(self.annTitle) > 20:
            return f"{self.annTitle[:20]}..."
        else:
            return self.annTitle[:20]
