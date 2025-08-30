from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GrammarSerializer, IregularSerializers
from .models import Grammar, Iregulars




class IregularsView(APIView):
    def get(self, request):
        iregulars = Iregulars.objects.all()
        serializers = IregularSerializers(iregulars, many=True)
        return Response(serializers.data)


class GrammarTitleView(APIView):
    def get(self, request):
        title = Grammar.objects.values_list("title", flat=True).distinct()
        return Response(list(title))


class GrammarView(APIView):
    def post(self, request):
        title = request.data.get('title', None)
        if not title:
            return Response({"error": "title parameter is required"}, status=400)

        grammar = Grammar.objects.filter(title__iexact=title)
        serializer = GrammarSerializer(grammar, many=True)
        return Response(serializer.data)