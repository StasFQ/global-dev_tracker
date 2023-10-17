from django.db.models import Sum, ExpressionWrapper, F, fields
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from book_manager.models import Book, ReadingSession
from .serializers import BookSerializer, BookListSerializer, ReadingSessionSerializer


class BookCreateView(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class StartReadingSession(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user')
        book_id = request.data.get('book_id')

        # Перевірка та автоматичне завершення попередньої активної сесії
        try:
            previous_session = ReadingSession.objects.get(user=user_id, end_time__isnull=True)
            if previous_session.book_id != book_id:
                previous_session.end_time = timezone.now()
                previous_session.save()
            else:
                return Response({'error': 'Reading session with this user and book already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except ReadingSession.DoesNotExist:
            pass

        session_data = {'user': user_id, 'book': book_id}
        serializer = ReadingSessionSerializer(data=session_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EndReadingSession(APIView):
    def put(self, request, pk, format=None):
        try:
            session = ReadingSession.objects.get(pk=pk, user=request.data['user'], end_time__isnull=True)
        except ReadingSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadingSessionSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(end_time=timezone.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadingStatistics(APIView):
    def get(self, request, format=None):
        user = request.user

        total_reading_time_per_book = ReadingSession.objects.filter(user=user).values('book__title').annotate(
            total_time=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField()))
        )

        total_reading_time_user = ReadingSession.objects.filter(user=user).aggregate(
            total_time=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField()))
        )

        return Response({'total_reading_time_per_book': total_reading_time_per_book, 'total_reading_time_user': total_reading_time_user})
