from .models import Pet

def pet_stats(request):
    total_public_pets = Pet.objects.filter(is_public=True).count()
    return {'total_public_pets': total_public_pets}