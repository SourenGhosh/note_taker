from rest_framework import serializers
from api_app.models import Note


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'body']
    

    def create(self, validated_data):
        return super(NoteSerializers, self).create(validated_data)
    def update(self, instance, validated_data):
        return super(NoteSerializers, self).update(instance, validated_data)
    def save(self):
        return super(NoteSerializers, self).save()
    
    