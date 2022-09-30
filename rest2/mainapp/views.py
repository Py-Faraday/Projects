from rest_framework.viewsets import ModelViewSet
from mainapp.models import Shop, Ticket
from mainapp.serializer import ShopSerializer, TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.paginations import StandardResultsSetPagination


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['addres',]
    ordering_fields = ['date_start','time_end',]
    search_fields = ['name', ]
    pagination_class = StandardResultsSetPagination

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class= TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['shop',]
    search_fields = ['shop_name', ]



