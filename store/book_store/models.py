from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):

    def get_queryset(self):
        return (
            super(PublishedManager, self)
            .get_queryset()
            .filter(status='published')
        )


class DraftManager(models.Manager):

    def get_queryset(self):
        return (
            super(DraftManager, self)
            .get_queryset()
            .filter(status='draft')
        )


class Book(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        User,
        related_name='books',
        on_delete=models.DO_NOTHING,
    )
    authors_info = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    objects = models.Manager()
    published = PublishedManager()
    draft = DraftManager()

    def is_published(self):
        return self.status == 'published'

    def change_status(self, status):
        self.status = status
        self.save()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class WebRequest(models.Model):
    method = models.CharField(max_length=50)
    host = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    uri = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    user_agent = models.CharField(max_length=1000,blank=True,null=True)
    remote_addr = models.GenericIPAddressField()
    remote_addr_fwd = models.GenericIPAddressField(blank=True,null=True)
    meta = models.TextField()
    cookies = models.TextField(blank=True,null=True)
    get = models.TextField(blank=True,null=True)
    post = models.TextField(blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    is_secure = models.BooleanField()
    is_ajax = models.BooleanField()
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    objects = models.Manager()

