from rest_framework import serializers
from .models import Member,Order


class MemberSerializers(serializers.ModelSerializer):
    class Meta :
        model = Member
        fields = ('id_number','full_name','date_birth','gender','phone_number','county','sub_county')


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('number_of_cards','destination','ordered_by')