from unicodedata import name
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
import rest_framework.status as status
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticated(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        try:
            is_authenticated = request.user.is_authenticated

            if is_authenticated:
                return Response(
                    {'isAuthenticated': 'succees'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'isAuthenticated': 'error'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except:
            return Response(
                {'error': 'Something went wrong when authenticatin check'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            data = self.request.data

            username = data['username']
            password = data['password']
            password2 = data['password2']

            if password == password2:
                if User.objects.filter(username=username).exists():
                    return Response(
                        {'error': 'User already exists'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
                else:
                    user = User.objects.create_user(
                        username=username, password=password)
                    user.save()

                    new_user = User.objects.get(username=username)
                    print(new_user.password)

                    user_profile = UserProfile.objects.create(user=new_user)
                    user_profile.save()

                    return Response(
                        {'success': 'Successfully created'},
                        status=status.HTTP_200_OK
                    )

            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except:
            return Response(
                {'error': 'Something went wrong when User Registration'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            data = self.request.data

            username = data['username']
            password = data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return Response(
                    {'susscess': 'User Authenticated', 'username': username},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Error User Authentication'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except:
            return Response(
                {'error': 'Something went wrong when User Loggin'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LogoutnView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            logout(request)
            return Response(
                {'susscess': 'User Logged out'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when User Loggin out'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'susscess': 'CSRF Cookie set'}, status=status.HTTP_200_OK)
