from rest_framework import serializers 
from student.models import Students
  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = (
            'id',
            'roll_no',
            'name',
            'age',
            'marks'
        )