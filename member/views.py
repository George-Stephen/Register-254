from rest_framework.response import Response
from rest_framework import status,generics,filters
from rest_framework.views import APIView
from .models import Member,Order
from .serializers import MemberSerializers,OrderSerializers

class Member_list(APIView):
    def get(self,request,format=None):
        all_members = Member.objects.all()
        serializers = MemberSerializers(all_members,many=True)
        return Response(serializers.data)

class New_members(APIView):
    def post(self,request,format=None):
        serializers = MemberSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class Search_member(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ["member_number"]

class Order_List(APIView):
    def get(self,request,format=None):
        all_orders = Order.objects.all()
        serializers = OrderSerializers(all_orders,many=True)
        return Response(serializers.data)

class New_Order(APIView):
    def post(self,request,format=None):
        serializers = OrderSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
