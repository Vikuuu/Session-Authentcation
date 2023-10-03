from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib import auth
from .models import UserProfile
from .serializer import UserProfileSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            user = User.objects.get(id=user.id)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({"profile": user_profile.data, "username": str(user.username)})
        except:
            return Response({"error" : "Something went wrong while retrieving user profile"})


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data

            first_name = data["first_name"]
            last_name = data["last_name"]
            phone = data["phone"]
            city = data["city"]

            user = User.objects.get(id=user.id)

            UserProfile.objects.filter(user=user).update(
                first_name=first_name, last_name=last_name, phone=phone, city=city
            )

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({"profile": user_profile.data, "username": str(user.username)})
        except:
            return Response({"error" : "Something went wrong while updating the user profile"})
