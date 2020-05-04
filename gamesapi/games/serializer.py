from games.models import Game
from rest_framework import serializers

class GameSerializer(serializers.Serializers):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.ChardField(max_lenght=200)
    release_date = serializers.DateTimeField()
    game_category = serializers.ChardField(max_lenght=200)
    played = serializers.BooleandField(requiered=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance