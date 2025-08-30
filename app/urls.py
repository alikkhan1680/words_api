from django.urls import path
from django.contrib import admin
from.views import GrammarView, GrammarTitleView, IregularsView
urlpatterns = [
    path("grammarlist/", GrammarView.as_view(), name="grammar"),
    path('grammartitle/', GrammarTitleView.as_view(), name="grammartitle"),
    path("iregulars/", IregularsView.as_view(), name="iregular"),
]