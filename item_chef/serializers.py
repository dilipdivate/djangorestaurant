from rest_framework import serializers
from item_chef.models import ItemChef


class ItemChefSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemChef
        fields = '__all__'

