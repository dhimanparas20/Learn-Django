from rest_framework import serializers
from .models import *
  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id=serializers.ReadOnlyField()
        model=User
        fields="__all__"
        # exclude= ['added_date']
        # fields=["name","age","contact"]
       
       
class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        id=serializers.ReadOnlyField()
        model=User
        fields="__all__"
        # depth = 1b    --> sends data of the foreign key if included
        #if dont wana use depth as it returns all data then use below
        # obj = thatserializerclass()
        
        # exclude= ['added_date']
        # fields=["name","age","contact"]        
    
    #for add validators    
    # def validate(self, data): #helpful in validating passwords etc
    #     if data['age']<5:
    #         raise serializers.ValidationError('age should be above 5')
    #     return data
    
    #for specific age validator
    def validate_age(self, data): #helpful in validating passwords etc
        if data<5:
            raise serializers.ValidationError('age should be above 5')
        return data 
        