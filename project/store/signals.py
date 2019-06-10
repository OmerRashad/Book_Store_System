from django.db.models.signals import post_save
from store.models import Book
from django.dispatch import receiver
from store.models import Book_Profile


@receiver(post_save, sender=Book)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Book_Profile.objects.create(book = instance)


@receiver(post_save, sender=Book)
def save_profile(sender, instance, **kwargs):
    instance.book_profile.save()