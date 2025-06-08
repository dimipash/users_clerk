from helpers import myclerk
from django.http import JsonResponse


CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY


@myclerk.api_login_required
def hello_world_api_view(request):
    user = request.user
    return JsonResponse(
        {
            "first_name": user.first_name,
            "id": user.id,
        }
    )
