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
    Use this view to test if your auth token is still valid. The response
    is a JSON object with "result" which will be true if your authentication
    is valid and false otherwise.
    """
    
    def get(self, request):
        return Response({"result": request.user and request.user.is_authenticated()})