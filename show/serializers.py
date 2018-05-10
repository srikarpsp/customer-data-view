from rest_framework import serializers

from show.models import enter


class enterSerializer(serializers.ModelSerializer):

    class Meta:
        model = enter
        fields = ('name', 'contact_number')