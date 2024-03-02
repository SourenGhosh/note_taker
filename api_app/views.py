from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from api_app.models import Note
from api_app.serializers import NoteSerializers

class NoteService(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = NoteSerializers
    def get_queryset(self):
        return Note.objects.filter(title=self.request.query_params.get("title"))

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('title', openapi.IN_QUERY,
                             description="get notes by title",
                             type=openapi.TYPE_STRING)
    ])
    def get(self, request, *args, **kwargs):
        print(request, args, kwargs)
        return self.list(request, *args, **kwargs)
    @swagger_auto_schema(operation_description="description", request_body=NoteSerializers)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class NoteDetailService(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    serializer_class = NoteSerializers
    queryset = Note.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
