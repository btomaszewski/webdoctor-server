from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from login.serializers import NewUserSerializer


class Register(APIView):
    """
    Register a new user.
    """
    serializer_class = NewUserSerializer

    def post(self, request):
        pass
        

class ObtainAuthToken(APIView):
    """
    API to obtain authentication tokens after authenticating via a username and
    password combination.
    """
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ValidateDoctorLicense(APIView):
    """
    This view validates a doctor's license.
    """
    # TODO: This is currently unimplemented and I have no idea how to actually
    #       verify this information.

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        return Response()


class AuthTest(APIView):
    """
    Use this view to test if your auth token is still valid. If you receive
    response code 200 you should be good. If you receive code 401 (Unauthorized)
    then your authentication method is no longer valid and you need a new auth
    token. If your auth succeeds then you will get a response of {"success": true}.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # We simply return success as true because if auth fails
        # they will get error code
        return Response({"success": True})