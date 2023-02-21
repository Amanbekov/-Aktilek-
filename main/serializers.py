from rest_framework import serializers
from main.models import (
    School, Teacher, Gallery,
      Review, New, )


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id', 'logo', 'whatsapp', 'twitter', 'facebook',
            'name', 'description', 'admissiontouniversity',
            'staff ', 'students', 'successworkyear', 
            'mail', 'address',
        )

class TeacherSerializer(serializers.ModelSerializer):
   class Meta:
    model = Teacher
    fields = ( 
         'id', ' position', 'name', 'photo',

    )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
     model = Gallery
     fields = (
        'photos', 'name',
     )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
     model = Review
     fields = ( 'photo', 'name', 
     'gender', ' description',

     )
    

class NewSerializer(serializers.ModelSerializer):
    class Meta:
     model = New
     fields = ('author ', 'photo', 
     'created_at', 'description',

     )


     read_only_fields = (
        'School',
        
     )


    


     

