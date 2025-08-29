from .models import Collection


def user_collections(request):
    if request.user.is_authenticated:
        return {'collections': Collection.objects.filter(owner=request.user)}
    return {'collections': []}


def current_collection_from_url(request):
    rm = getattr(request, "resolver_match", None)
    if not rm:
        return {}

    raw_pk = (
            rm.kwargs.get("pk")
            or rm.kwargs.get("collection_pk")
            or rm.kwargs.get("collection_id")
    )
    if not raw_pk:
        return {}

    try:
        pk = int(raw_pk)
    except (TypeError, ValueError):
        return {}

    qs = Collection.objects.only("id", "name")
    if request.user.is_authenticated:
        qs = qs.filter(owner=request.user)
    collection = qs.filter(pk=pk).first()

    ctx = {"current_collection_id": pk}
    if collection:
        ctx["collection"] = collection
    return ctx
