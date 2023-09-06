import json
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avatar
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class SignUpView(APIView):

    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        # no returned name = request_data.get('name')
        username = request_data.get('username')
        password = request_data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=password)
        user.save()
        login(request, user)
        return Response({"message": "successful operation"}, status=status.HTTP_200_OK)


class SignInView(APIView):
    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        print(request_data)
        username = request_data.get('username')
        password = request_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "successful operation"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "error operation"}, status=status.HTTP_401_UNAUTHORIZED)


class SignOutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'message': 'successful operation'}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        user_data = request.data
        serializer = UserSerializer(user, data=user_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordUpdateView(APIView):
    def post(self, request):
        password = request.data.get('password')
        print(password)
        if password:
            user = request.user
            user.set_password(password)
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Password field is required'}, status=status.HTTP_400_BAD_REQUEST)


class AvatarUploadView(APIView):

    def post(self, request):
        user = request.user
        avatar = request.FILES.get('avatar')

        if avatar:
            avatar_obj = Avatar(src=avatar)
            avatar_obj.save()
            user.avatar = avatar_obj
            user.save()
            return Response({'message': 'Avatar updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Avatar file is required'}, status=status.HTTP_400_BAD_REQUEST)
