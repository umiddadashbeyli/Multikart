from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login


from account.api.serializers import RegistrationSerializer
from account.views import User


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Succesfully registered'
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error' : 'Please fill all fields'}, status=status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email = email).exists()
        if check_user == False:
            return Response({'error' : 'Email does not exits'}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=request.user)
            data = {
                'token' : token.key,
                'user_id' : request.user.pk,
                'username' : request.user.username
            }
            return Response({'success' : 'Successfully login', 'data' : data}, status=status.HTTP_200_OK)
        else:
            return Response({'error' : 'Invalid login details'}, status=status.HTTP_400_BAD_REQUEST)

