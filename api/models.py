
from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    ROLE_CHOICES = (('teacher', 'Teacher'), ('student', 'Student'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Journal(models.Model):
    ATTACHMENT_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('url', 'URL'),
        ('pdf', 'PDF'),
    )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
    description = models.TextField()
    attachment_type = models.CharField(max_length=10, choices=ATTACHMENT_CHOICES, null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    tagged_students = models.ManyToManyField(User, related_name='tagged_journals')
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Journal by {self.teacher.username} at {self.published_at}"
