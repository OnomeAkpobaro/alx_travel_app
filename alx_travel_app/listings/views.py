from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Save the user who created the listing."""
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active listings."""
        active_listings = self.queryset.filter(is_active=True)
        serializer = self.get_serializer(active_listings, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_listings(self, request):
        """Get listings created by the current user."""
        if request.user.is_authenticated:
            user_listings = self.queryset.filter(created_by=request.user)
            serializer = self.get_serializer(user_listings, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Authentication required.'}, status=401)