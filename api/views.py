
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Journal, UserRole
from .serializers import JournalSerializer, FeedSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404

def get_user_role(user):
    try:
        return user.userrole.role
    except UserRole.DoesNotExist:
        return None

class JournalCreate(APIView):
    def post(self, request):
        if get_user_role(request.user) != 'teacher':
            return Response({"error": "Only teachers can create journals."}, status=403)
        data = request.data.copy()
        data['teacher'] = request.user.id
        serializer = JournalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class JournalUpdate(APIView):
    def put(self, request, pk):
        journal = get_object_or_404(Journal, pk=pk)
        if journal.teacher != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        serializer = JournalSerializer(journal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class JournalDelete(APIView):
    def delete(self, request, pk):
        journal = get_object_or_404(Journal, pk=pk)
        if journal.teacher != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        journal.delete()
        return Response(status=204)

class JournalPublish(APIView):
    def post(self, request, pk):
        journal = get_object_or_404(Journal, pk=pk)
        if journal.teacher != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        journal.is_published = True
        journal.save()
        return Response({"message": "Journal published."})

class JournalFeed(APIView):
    def get(self, request):
        role = get_user_role(request.user)
        if role == 'teacher':
            journals = Journal.objects.filter(teacher=request.user)
        elif role == 'student':
            journals = request.user.tagged_journals.filter(
                is_published=True, published_at__lte=timezone.now())
        else:
            return Response({"error": "Role not defined"}, status=403)
        serializer = FeedSerializer(journals, many=True)
        return Response(serializer.data)
