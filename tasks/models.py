from typing import Any
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files import File
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
import boto3
from botocore.exceptions import ClientError

User = get_user_model()


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])


class Photo(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.image.name

    @property
    def image_url(self):
        return self.image.url


# Delete image from S3 when Photo object is deleted
@receiver(post_delete, sender=Photo)
def submission_delete(sender: Photo, instance: Any, **kwargs: Any) -> Any:
    delete_object_from_r2(
        settings.AWS_STORAGE_BUCKET_NAME, instance.image.name)


def delete_object_from_r2(bucket_name, object_key):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        verify=False
    )
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f'{object_key} deleted from {bucket_name} bucket')
    except ClientError as e:
        print(f'Error deleting {object_key} from {bucket_name} bucket: {e}')
