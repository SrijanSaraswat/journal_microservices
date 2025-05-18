
from django.urls import path
from .views import JournalCreate, JournalUpdate, JournalDelete, JournalPublish, JournalFeed

urlpatterns = [
    path('journals/', JournalCreate.as_view()),
    path('journals/<int:pk>/', JournalUpdate.as_view()),
    path('journals/<int:pk>/delete/', JournalDelete.as_view()),
    path('journals/<int:pk>/publish/', JournalPublish.as_view()),
    path('journals/feed/', JournalFeed.as_view()),
]
