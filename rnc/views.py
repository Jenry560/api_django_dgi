from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from rnc.models import DrRnc
from rnc.serializers import RncSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

load_dotenv()


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def consultar_rnc(request, rnc):
    try:

        # validando si el rnc esta repetido para que lo envie como un arrelgo
        validate_duplicate_or_unique = DrRnc.objects.filter(rnc=rnc)
        if len(validate_duplicate_or_unique) > 1:
            serializer = RncSerializer(validate_duplicate_or_unique, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        # Enviando el dato unique
        serializer = RncSerializer(validate_duplicate_or_unique[0])
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except:

        return JsonResponse(
            {"error": "No se encontró ningún registro con ese RNC"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def consultar_nombre(request, name):
    try:

        names_found = DrRnc.objects.filter(nombre__icontains=name)
        serializer = RncSerializer(names_found, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except:

        return JsonResponse(
            {"error": "No se encontró ningún registro con ese nombre"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
def crear_token(request, contrasena, persona):
    try:

        contra_env = os.getenv("CONTRA")

        contrasena_is_valid = contrasena == contra_env

        if not contrasena_is_valid:
            return JsonResponse(
                {"error": "token no se genero por error de credenciales"}
            )

        user_iscreated = User.objects.filter(username=persona).first()

        if not user_iscreated:
            new_user = User.objects.create_user(username=persona)
            new_user.save()

        # Si el usuario esta creado el token va buscar el usuario creado de lo contrario buscara el nuevo user
        token_for_search = user_iscreated if user_iscreated else new_user

        token, create = Token.objects.get_or_create(user=token_for_search)

        return JsonResponse({"token": token.key})

    except Exception as e:
        raise e
