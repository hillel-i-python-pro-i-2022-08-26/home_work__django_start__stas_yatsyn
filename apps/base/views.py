from faker import Faker
from django.http import HttpRequest, HttpResponse

faker = Faker()


def index(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = faker.first_name()
    return HttpResponse(f"Hello,  {name} ")
