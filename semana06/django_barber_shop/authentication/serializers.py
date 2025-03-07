from rest_framework import serializers
from .models import (
    RoleModel,
    UserModel,
)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=True,
    )
    status = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserModel
        exclude = ('is_staff', 'is_superuser', 'last_login')
        extra_kwargs = {
            'status': {
                'required': False
            }
        }

    def save(self):
        instance = self.instance
        validated_data = self.validated_data

        if instance:
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.role = validated_data.get('role', instance.role)

            if 'password' in validated_data:
                instance.set_password(validated_data.get('password'))

            instance.save()
            
            return instance
        else:
            user = UserModel(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
