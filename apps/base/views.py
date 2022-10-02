from django.http import HttpRequest, HttpResponse

from apps.base.services.get_random_user import get_random_user


def index(request: HttpRequest, name=None) -> HttpResponse:
    if name is None:
        return HttpResponse(f'Hello {get_random_user()}')
    else:
        return HttpResponse(f'Hallo {name}')
