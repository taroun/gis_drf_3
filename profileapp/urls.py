from django.urls import path

from profileapp.views import ProfileCreateAPIView, ProfileCreateTemplateView, ProfileUpdateAPIView, \
    ProfileUpdateTemplateView

urlpatterns = [
    path('create_template/', ProfileCreateTemplateView.as_view(), name='create_template'),
    path('update_template/<int:pk>', ProfileUpdateTemplateView.as_view(), name='update_template'),

    path('', ProfileCreateAPIView.as_view(), name='create'),
    path('<int:pk>', ProfileUpdateAPIView.as_view(), name='update'),
]
