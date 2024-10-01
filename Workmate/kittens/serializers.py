from rest_framework import serializers
from .models import Kitten, Breed, Rating

class KittenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kitten
        fields = ('id', 'color', 'age', 'breed', 'description')



class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ('title',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['score']

    def create(self, validated_data):
        request = self.context.get('request')
        kitten_id = request.parser_context['kwargs']['kitten_id']
        validated_data['user'] = request.user
        validated_data['kitten'] = Kitten.objects.get(id=kitten_id)
        return super().create(validated_data)


