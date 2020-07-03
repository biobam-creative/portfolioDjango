from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    mockup1 = models.ImageField(upload_to='portfolio/images/')
    mockup2 = models.ImageField(upload_to='portfolio/images/')
    mockup3 = models.ImageField(upload_to='portfolio/images/')

    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
