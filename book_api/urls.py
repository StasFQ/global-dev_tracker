from django.urls import path

from book_api.views import BookCreateView, BookDetailView, BookListView, EndReadingSession, StartReadingSession, \
    ReadingStatistics

urlpatterns = [
    path('book/', BookCreateView.as_view(), name='BookCreateView'),
    path('book_detail/<int:id>/', BookDetailView.as_view(), name='BookDetailView'),
    path('book_detail_list/', BookListView.as_view(), name='BookListView'),
    path('start-reading/', StartReadingSession.as_view(), name='start-reading-session'),
    path('end-reading/<int:pk>/', EndReadingSession.as_view(), name='end-reading-session'),
    path('reading-statistics/', ReadingStatistics.as_view(), name='ReadingStatistics')
]
