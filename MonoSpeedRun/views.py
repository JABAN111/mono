from rest_framework.response import Response
from rest_framework.views import APIView


class Data(APIView):


    def get(request):
        #username = request.user.username
#        data = {
 #           'username': username,
  #          'flood': 'flood',
   #         '2+2': 2+2,
    #        21: 32,
     #       "config": username,
      #  }
       # return Response(data)
        #if(username != ' '):
         #   return Response(username)
        return Response('Пользователь не авторизирован')