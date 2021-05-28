from celery import shared_task
import pickle
from .models import Collections

# @shared_task
# def perform_create_task(task_data):
#     task_data = pickle.loads(task_data)
#     new_self = task_data['my_class'](task_data['request']())
#     serializer = new_self.get_serializer(data=task_data['request_data'])
#     serializer.is_valid(raise_exception=True)
#     new_self.perform_create(serializer)

@shared_task
def serialize_create_task(data):
    validated_data = pickle.loads(data)
    Collections.objects.create(**validated_data)

