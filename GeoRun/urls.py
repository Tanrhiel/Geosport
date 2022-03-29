from django.urls import path, include
from GeoRun.views import *
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('runners', RunnerView.as_view()),
    path('runners/<int:pk>', RunnerDetailView.as_view()),
    path('defis', DefiView.as_view()),
    path('defis/<int:pk>', DefiDetailView.as_view()),
    path('participations', ParticipationView.as_view()),
    path('participations/<int:pk>', ParticipationDetailView.as_view())
    #path('participations/<slug:name>/resultats', ParticipationView.get_result),
    #path('runners/api', include(router.urls))
]