from helpers import myclerk
from django.conf import settings
from django.http import JsonResponse

CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY


def hello_world_api_view(request):
    clerk_user_id = myclerk.get_clerk_user_id_from_request(request)
    if not clerk_user_id:
        return JsonResponse({"message": "Unauthorized"}, status=401)
    user, created = myclerk.get_clerk_user(clerk_user_id)

    return JsonResponse(
        {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "created": created,
            "message": "Hello World!",
        }
    )
