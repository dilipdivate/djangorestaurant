
from rest_framework import serializers

from menu.models import Menu

class MenusSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")  # new

    class Meta:
        model = Menu
        fields = '__all__'
