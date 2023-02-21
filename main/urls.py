from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from main.views import (
    SchoolView,
    TeacherView,
    GalleryView,
    ReviewView,
    NewView,
    
)

router=DR()

router.register('school', SchoolView, basename='school')
router.register('teacher', TeacherView, basename='teacher')
router.register('gallery', GalleryView, basename='gallery')
router.register('review', ReviewView, basename='review')
router.register('New', NewView, basename='New')


urlpatterns = []

urlpatterns += router.urls



