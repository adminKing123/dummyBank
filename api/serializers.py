from rest_framework import serializers
from .models import Record, Total
from rest_framework.exceptions import ValidationError

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'transaction_date', 'amount', 'is_deposited', 'description']

    def create(self, validated_data):
        TotalObj = Total.objects.first()
        dep = validated_data.get("is_deposited")
        amount = validated_data.get("amount")
        if (dep):
            TotalObj.total += amount
        else:
            if (amount > TotalObj.total):
                raise ValidationError("Insufficient Balance")
            TotalObj.total -= amount
        TotalObj.save()
        return super().create(validated_data)