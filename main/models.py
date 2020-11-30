from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=20)
    release_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"{self.title}-{self.release_date}"

class NetworkManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Title cannot be less than 2 characters"
        if len(post_data['release_date']) < 2:
            errors['release_date'] = "Date cannot be less than 2 characters"
        return errors


class Network(models.Model):
    name = models.CharField(max_length=20)
    shows = models.ManyToManyField(Show, related_name = "networks")
    objects = NetworkManager ()
    def __repr__(self):
        return f"{self.name}"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

