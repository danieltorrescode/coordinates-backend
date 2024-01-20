from rest_framework import viewsets

from django.contrib.auth import get_user_model

from rest_framework.response import Response

from .serializers import UsersSerializer

User = get_user_model()


class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all().order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # import ipdb;ipdb.set_trace()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
