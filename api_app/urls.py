from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_app import views

urlpatterns = [
    path('notes/', views.NoteService.as_view()),
    path('notes/<str:pk>', views.NoteDetailService.as_view())
    #path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

