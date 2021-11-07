from rest_framework import serializers
from datetime import datetime
import random


def generate_default_seed():
    return [random.randint(0, 65536)]


class GeneratorRequestSerializer(serializers.Serializer):
    NETWORK_CHOICES = (
        ('universe_generator', 'Universe Generator'),
        ('backgrounds_generator', 'Backgrounds Generator'),
    )
    NOISE_CHOICES = (
        ('const', 'Constant Noise'),
        ('random', 'Random Noise'),
        ('none', 'No noise'),
    )

    network = serializers.ChoiceField(choices=NETWORK_CHOICES)
    seeds = serializers.ListField(
        default=generate_default_seed,
        child=serializers.IntegerField(min_value=0, max_value=65536),
        required=False,
        allow_null=False
    )
    truncation_psi = serializers.FloatField(min_value=-3.0, max_value=3.0)
    noise_mode = serializers.ChoiceField(choices=NOISE_CHOICES, default='none')
    class_idx = serializers.IntegerField(required=False, min_value=0, max_value=2, allow_null=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
