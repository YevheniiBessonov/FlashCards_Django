from .models import Collection


def user_collections(request):
    if request.user.is_authenticated:
        return {'collections': Collection.objects.filter(owner=request.user)}
    return {'collections': []}
