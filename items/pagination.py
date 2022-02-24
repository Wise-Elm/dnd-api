from rest_framework.pagination import PageNumberPagination


DEFAULT_OBJECTS_PER_PAGE = 10


class DefaultPagination(PageNumberPagination):
    page_size = DEFAULT_OBJECTS_PER_PAGE
