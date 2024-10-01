from rest_framework import viewsets, permissions
from .models import Kitten, Breed, Rating
from .serializers import KittenSerializer, BreedSerializer, RatingSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend

class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('breed',)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = (IsOwner, )
        else:
            self.permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

        return super().get_permissions()

class KittenRatingListAPIView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer


    def get_queryset(self):
        kitten_id = self.kwargs['kitten_id']
        return Rating.objects.filter(kitten_id=kitten_id)

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (permissions.AllowAny, )
