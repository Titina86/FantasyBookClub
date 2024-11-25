from django.urls import path, include

from journal import views

urlpatterns = [
    path('create/', views.ReadingJournalCreateView.as_view, name='journal-create'),
]