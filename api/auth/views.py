from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializer import LoginSerializer, UserSerializer, RegisterUserSerializer, ChangePasswordSerializer
from accounts.models import User


class LoginGenericAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0]
    
            print(Token.objects.get_or_create(user=user)[0])
            print(Token.objects.get_or_create(user=user)[1])

            user_serializer = UserSerializer(instance=user, context={'request': request})
            return Response({
                **user_serializer.data,
                'token_key': token.key
            })
        return Response({'massage': 'Пользователь не найден или неверный пароль'},
                        status=status.HTTP_400_BAD_REQUEST)
    

class RegisterGenericApiView(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        user_serializer = UserSerializer(instance=user, context={'request': request})
        return Response({
            **user_serializer.data,
            'token': token.key,
        })
    

class ChangePasswordApiView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (AllowAny,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if self.object.check_password(serializer.data.get("old_password")):
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Пароль успешно обновлен',
                    'data': []
                }
                return Response(response)
            else:
                return Response({"old_password": ['Неверный пароль']}, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)