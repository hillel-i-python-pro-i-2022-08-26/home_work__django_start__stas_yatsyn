from django.http import HttpRequest, HttpResponse

from apps.base.services.get_random_user import get_random_user


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Hello {get_random_user()}')


def create(request: HttpRequest, name='<name>'):
    return HttpResponse(f'Hallo {name}')
