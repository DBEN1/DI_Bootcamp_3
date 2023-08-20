from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, created, **kwargs):
    if created:  # This ensures the signal is only executed for newly created instances
        print(f"New profile created: Name - {instance.name}, Email - {instance.email}")

@receiver2(pre_delete, sender=Profile)
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print(f"Warning: You are about to delete an active profile: Name - {instance.name}, Email - {instance.email}")
