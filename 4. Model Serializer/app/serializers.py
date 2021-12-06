
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # ! validator
    # def start_with_s(value):
    #     if value['0'].lower() != 's':
    #         raise serializers.ValidationError('Name Should Start with S')
    # name = serializers.CharField(validators=[start_with_s])

    # * for specific fields
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        # fields = ['id', 'name', 'roll', 'city']
        # * here we don't need to create create() and update() it will create automatically
        # * if we want all field then we can also use __all__
        fields = '__all__'
        # * if we want ignore any field then put it on exclude it will print whole field expect roll
        # * you have to must use this bracket in exclude
        # exclude = ['roll']

        # * for multiple fields
        # read_only_fields = ['name', 'roll']
        # * more then one validation to specific fields
        # extra_kwargs = {'name': {'read_only': True, 'required': True}}

        # ! Field Level Validation
        # def validate_roll(self, value):
        #     if value >= 200:
        #         raise serializers.ValidationError('seat full')
        #     return value

        # ! Object Level Validation

        # def validate(self, data):
        #     nm = data.get('name')
        #     ct = data.get('city')
        #     if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
        #         raise serializers.ValidationError('City must be ranchi')
        #     return data
