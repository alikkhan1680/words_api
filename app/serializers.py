from rest_framework import serializers
from .models import Grammar, GrammarDescriptions, GrammarExemple, GrammarImg, Iregulars


class IregularSerializers(serializers.ModelSerializer):
    class Meta:
        model = Iregulars
        fields = "__all__"


class GrammarDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarDescriptions
        fields = ['descriptions']  # faqat matn


class GrammarExempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarExemple
        fields = ['exemple']  # faqat matn


class GrammarImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarImg
        fields = ['image']  # faqat rasm


class GrammarSerializer(serializers.ModelSerializer):
    descriptions = GrammarDescriptionsSerializer(many=True, read_only=True)
    exemple = GrammarExempleSerializer(many=True, read_only=True)
    picture = GrammarImgSerializer(many=True, read_only=True)

    class Meta:
        model = Grammar
        fields = ['id', 'title', 'level', 'descriptions', 'exemple', 'picture']