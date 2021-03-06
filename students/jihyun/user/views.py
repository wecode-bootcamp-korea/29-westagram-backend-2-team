import json

from django.views import View
from django.http import JsonResponse
# Create your views here.

from user.models import user

class UserView(View) :

    def post(self, request):
        """
        1. 함수의 목적 - 사용자 정보를 데이터베이스의 테이블에 저장, 맞게 넣었는지 판단
        2. input - 이름 이메일 비밀번호 폰넘버
            {
            "name" : "나지현",
            "email" : "pathfinderk7@gmail.com"
            "password" : "1234!@#$"
            "phonenumber" : "010-1111-1111"
            "other_information" : "다른 정보 넣기"
            }

            """
            try :
                data = json.loads(request.body)

                if User.objects.filter(email=data['email']).exists():
                    return JsonResponse({'message' : 'ERROR_EMAIL_ALREADYEXISRT'}, status=400)

                if not data['email'] or not data['password']:
                    return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

                if not re.match(r"^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data['email']):
                    return JsonResponse({'message' : 'INVALID_EMAIL'}, status=404)

                if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data['password']):
                    return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=404)

                User.objects.create(
                        name = data['name']
                        email = data['email']
                        password = data['password']
                        phonenumber = data['phonenumber']
                        other_information = data.get['other_information']
                        )
                return JsonResponse({'message' : 'SUCCESS'}, status = 201)

            except Exception:
                return JsonResponse({'message' : 'FAILED'}, status=400)
