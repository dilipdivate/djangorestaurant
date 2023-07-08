from rest_framework import serializers
from table_top.models import TableTop


class TableTopSerializer(serializers.ModelSerializer):

    class Meta:
        model = TableTop
        fields = '__all__'

