from faker import Faker
from django.http import HttpRequest, HttpResponse
from .services.get_random_user import get_random_user


def index(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = get_random_user()
    return HttpResponse(f"Hello,  {name} ")
