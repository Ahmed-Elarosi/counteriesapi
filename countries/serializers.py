from rest_framework import serializers

from countries.models import Countries


class CountriesSerializer(serializers.ModelSerializers):

    class Meta:
        model= Countries
        fields = ("id", "name", "capital")
