# import email
# import os
# import time
# import json
# from urllib import request

# from django.contrib.auth import (
#     get_user_model,
#     authenticate,
# )
# from rest_framework import status
# from rest_framework.response import Response

# from django.utils.translation import gettext as _

# from rest_framework import serializers
# from django.http.response import JsonResponse
# from agora.agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
# from core.models import Talk2meUser


# class AgoraTokenSerializer(serializers.Serializer):
#     # email = serializers.EmailField()

#     def create(self, request):
#         email = request.get('email')
#         # appID = os.environ.get('AGORA_APP_ID')
#         appID = '6f2b971c2c1f4edc83e2700f955986e6'
#         appCertificate = 'a4748997278c40ab8cf2fbc008397588'
#         # appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
#         channelName = 'first channel'
#         userAccount = email
#         expireTimeInSeconds = 3600
#         currentTimestamp = int(time.time())
#         privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

#         token = RtcTokenBuilder.buildTokenWithAccount(
#             appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

#         # return token

#         return Response({'token': token, 'appID': appID})
