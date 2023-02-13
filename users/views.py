from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
