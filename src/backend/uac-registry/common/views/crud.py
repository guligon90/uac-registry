# DRF imports
from rest_framework import status
from rest_framework.response import Response

# Project imports
from common.exceptions import response_from_exception


def get_instance_from_db(instance_id, db_model):
    try:
        return db_model.objects.get(pk=instance_id)
    except db_model.DoesNotExist:
        return None


def update_instance(data, instance, serializer):
    serialized = serializer(instance, data=data, partial=True)

    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)

    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


def retrieve_instance(instance, serializer):
    serialized = serializer(instance)
    return Response(serialized.data, status=status.HTTP_200_OK)


def delete_instance(instance):
    instance.delete()
    payload = {'message': f'{instance.__class__.__name__} removed successfully.'}
    return Response(payload, status=status.HTTP_204_NO_CONTENT)


def list_instances(request, serializer, db_model):
    """Lists all instances."""
    try:
        instances = db_model.objects.all()
        serialized = serializer(instances, many=True)
        return Response(serialized.data)
    except Exception as e:
        return response_from_exception('instance.views.list_instance', e)


def create_instance(request, serializer):
    """Creates a new instance."""
    try:
        serialized = serializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('instance.views.create_instance', e)


def instance_detail(request, instance_id, db_model, serializer):
    """Retrieves, update or delete a instance."""
    try:
        instance = get_instance_from_db(instance_id, db_model)

        if instance:
            method_switcher = {
                'DELETE': delete_instance(instance),
                'GET': retrieve_instance(instance, serializer),
                'PATCH': update_instance(request.data, instance, serializer),
            }

            return method_switcher.get(request.method)

        return Response(status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return response_from_exception('instance.views.instance_detail', e)
