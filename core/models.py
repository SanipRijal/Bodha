from django.db import models


class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.email


EVENT_CHOICES = (
    (1, 'Upcoming'),
    (2, 'Ongoing'),
    (3, 'Successful'),
)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=500)
    status = models.IntegerField(choices=EVENT_CHOICES)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/images')

    def __str__(self):
        return self.event.title


class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='events/videos/')

    def __str__(self):
        return self.event.title


class Header(models.Model):
    description = models.TextField()


class OurCause(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class OurReach(models.Model):
    active_members = models.IntegerField()
    villages_covered = models.IntegerField()
    completed_campaigns = models.IntegerField()
    students = models.IntegerField()


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner/')


