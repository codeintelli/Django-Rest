from rest_framework import serializers
from .models import Student


# validator 
def start_with_s(value):
       if value[0].lower() != 's':
           raise serializers.ValidationError('Name Should Start with S')


class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators=[start_with_s])
    # here validator = [start_with_s] is put when we are define validator class
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    # field level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object level validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sankar' and ct.lower() != 'somnath':
            raise serializers.ValidationError('City must be Somnath')
        return data