from django.db.models import QuerySet
from rest_framework import serializers, viewsets,permissions
from users.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password',]

        read_only_fields = ["id",]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self,validated_data:dict):
         user = User(**validated_data)
         user.set_password(validated_data["password"])
         user.save()
         return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]

    def get_queryset(self)-> QuerySet[User]:
        user = self.request.user
        return User.objects.filter(id=user.pk)

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]

