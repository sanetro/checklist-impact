from django.urls import path
from . import views

urlpatterns = [
    path('artifacts/', views.showArtifacts),
    path('bossMaterial/', views.showBossMaterial),
    path('characterAscension/', views.showCharacterAscension),
    path('characters/', views.showCharacters),
    path('commonAscension/', views.showCommonAscension),
    path('materialsTalentBook/', views.showMaterialsTalentBook),
    path('weapons/', views.showWeapons),
]