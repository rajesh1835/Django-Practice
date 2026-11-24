from rest_framework import serializers
from .models import Bank, Branch

class BankModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BranchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"