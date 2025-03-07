from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AppointmentCreateView(APIView):
    def post(self, request):
        data = request.data
        print(data)

        return Response({"Ok": True}, status=status.HTTP_200_OK)
