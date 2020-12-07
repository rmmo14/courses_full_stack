from django.db import models

# Create your models here.
class myManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Name must be more than 5 characters"
        if len(postData['description']) < 16:
            errors['description'] = "Description must be more than 15 characters"
        return errors

class theCourse(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = myManager()