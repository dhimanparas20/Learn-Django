from django.http import JsonResponse
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User 
from .serializers import UserSerializer,UserSerializer2


#creating class based  viewsets
#Viewsets save or time in making APIS for CRUD operations
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    # use this if want to use http://127.0.0.1:5000/api/users/<custom data>/custom_method/<value filed>/
    # @action(detail=True,methods=['GET'],url_path='custom_method/(?P<value>[^/.]+)')
    # def custom_method(self,request,value,pk):
    #     data = {"custom value":value}
    #     return Response(data)
    
    @action(detail=False,methods=['GET'],url_path='custom_method/(?P<value>[^/.]+)')
    def custom_method(self,request,value):
        data = {"custom value":value}
        return Response(data)
        
    
# APPPLY CRUD operations
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def index(request):
    if request.method == "GET":
        objs = User.objects.all()
        serializer = UserSerializer2(objs,many=True, context={"request": request})
        return Response(serializer.data) 
    elif request.method == "POST":
        data = request.data
        serializer = UserSerializer2(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT": #No partial update support 
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer2(user,data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH": #Partial Update support 
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer2(user,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  
    elif request.method == "DELETE":
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
            user.delete()
            return Response({"message": f"User {user} deleted successfully"}, status=204)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)   
    
@api_view(['GET'])
def name(request):
    data = {"location": "Inside API"}
    return JsonResponse(data)    

class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
