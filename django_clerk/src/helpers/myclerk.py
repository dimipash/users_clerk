import json
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

from django.conf import settings
from django.contrib.auth import get_user_model


CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY

User = get_user_model()


def get_clerk_user_id_from_request(request):
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(authorized_parties=["http://localhost:3002"]),
    )
    payload = request_state.payload
    if payload is None:
        return None
    clerk_user_id = payload.get("sub")
    print(clerk_user_id, request_state.is_signed_in)
    if not request_state.is_signed_in:
        return None
    return clerk_user_id


def update_or_create_clerk_user(clerk_user_id):
    if not clerk_user_id:
        return None
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    clerk_user = sdk.users.get(user_id=clerk_user_id)
    if not clerk_user:
        return None
    primary_email_address_id = clerk_user.primary_email_address_id
    primary_email = None
    if primary_email_address_id:
        clerk_email_addresses = clerk_user.email_addresses
        for email_data in clerk_email_addresses:
            _email_id = email_data.get("id")
            if _email_id == primary_email_address_id:
                primary_email = email_data.get("email_address")
                break
    django_user_data = {
        "username": clerk_user.username,
        "first_name": clerk_user.first_name,
        "last_name": clerk_user.last_name,
        "email": primary_email,
    }
    user_obj, created = User.objects.update_or_create(
        clerk_user_id=clerk_user_id,
        defaults=djago_user_data,
    )
    return user_obj, created
