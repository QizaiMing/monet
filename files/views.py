from files.serializers import FileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ControlFile


@api_view(["GET"])
def api_detail_file(request, id_):
    try:
        file = ControlFile.objects.get(id=id_)

    except ControlFile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not file:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FileSerializer(file)
    return Response(serializer.data)