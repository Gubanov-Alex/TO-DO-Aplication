from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import serializers,status,viewsets
from rest_framework.decorators import action

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    attachment = serializers.FileField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("attachment",)

        def validate_attachment(self, value):
            # to do some validation logic
            return value

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def create(self, request: Request):
        """create a task without attachment"""
        serializer = self.get_serializer(data= request.data, context={"request": request} )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=True)
    def attachment(self, request: Request,pk: str)-> Response:
        """HTTP/tasks/2/attachment/"""

        serializer = TaskAttachmentSerializer(data= request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance: Task = self.get_object()
        instance.attachment = serializer.validated_data["attachment"]
        instance.save()

        return Response(TaskSerializer(instance).data, status= status.HTTP_200_OK)

    @action(methods=["POST"], detail=True)
    def toggle(self, request: Request, pk: str) -> Response:
        """HTTP/tasks/2/toggle/"""

        instance: Task = self.get_object()
        instance.finished = not instance.finished
        instance.save()

        return Response(TaskSerializer(instance).data, status=status.HTTP_200_OK)


