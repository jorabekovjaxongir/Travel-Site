from django.db import models



from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='image/about')

    def __str__(self) -> str:
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title


class Guide(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/guide')
    job_name = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name