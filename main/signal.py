
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Staff , Contact
from .views import auto_assign


@receiver(post_save, sender=Staff)
def assign_pending(sender, instance, **kwargs):

    if instance.busy == False:
        current_tsk = Contact.objects.filter(
            assign = instance,
            status ="assigned"
        ).first()
        if current_tsk:
            current_tsk.status = "complete"
            current_tsk.save()

        auto_assign(instance)

