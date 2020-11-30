# Django Rest Framework
from rest_framework import viewsets
from rest_framework import filters

# Third Party
from url_filter.integrations.drf import DjangoFilterBackend

# chium
from backend.modules.core.paginations import SmallResultsSetPagination, StandardResultsSetPagination, LargeResultsSetPagination


# Main Section


class ModelViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = '__all__'
