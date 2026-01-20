from rest_framework import viewsets, permissions
from .models import Offer
from .serializers import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):

    # Required for DRF Router
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_permissions(self):
        """
        GET  -> Public access
        POST/PUT/DELETE -> Admin only
        """
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        """
        Return only active offers.
        Optional filter by category (?category=mobile/internet/fibre)
        """
        queryset = Offer.objects.filter(is_active=True)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)

        return queryset
