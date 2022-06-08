import time
import os
from rest_framework.response import Response
from rest_framework.views import APIView

from agora.agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee


class AgoraToken(APIView):
    def get(self, request):
        appID = os.environ.get('AGORA_APP_ID')
        appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
        channelName = 'first channel'
        userAccount = "email"
        expireTimeInSeconds = 3600
        currentTimestamp = int(time.time())
        privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

        token = RtcTokenBuilder.buildTokenWithAccount(
            appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

        # return token

        return Response({'token': token, 'appID': appID})
