from rest_framework import serializers
from .models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if instance:
            instance.save()
        return instance
        