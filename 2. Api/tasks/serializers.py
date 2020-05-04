from rest_framework import serializers
from tasks.models import User, UserTask


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    # user_task = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save() 
        return instance 


class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=100)
    state = serializers.BooleanField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return UserTask.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save() 
        return instance 