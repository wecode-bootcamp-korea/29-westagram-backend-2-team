import json
from logging import exception 
import re

from django.views import View
from .models import User

from django.http import JsonResponse


class SignUpView (View):
    def post(self, request):

        """
        1. 목적 : 클라이언트로부터 받은 사용자 데이터
        (이름, 이메일, 비밀번호, 연락처, 그외 개인정보)를 데이터베이스에 등록하기 위함
        2. INPUT : 
        {
            "name"         : "hyelin",
            "email"        : "rlafls9596@gamil.com",
            "password"     : "rlagPFls95@",
            "phone_number" : "01049093501"
        }
        3. OUTPUT : 
        성공 시
        {
            "message" : "SUCCESS" , status=201
        }
        """
        user_data   = json.loads(request.body)
        REX_EMAIL   = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REX_PASS    = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
        
        if 'name' not in user_data :
            return JsonResponse({'message' : '이름을 입력해 주세요'}, status=400)

        if 'email' not in user_data :
            return JsonResponse({'message' : '이메일을 입력해 주세요'}, status=400)

        if 'password' not in user_data :
            return JsonResponse({'message': '비밀번호를 입력해 주세요'}, status=400)

        if not re.fullmatch(REX_EMAIL, user_data['email']) :
            return JsonResponse({'message' : '유효하지 않은 이메일입니다'})

        if not re.fullmatch(REX_PASS, user_data['password']) :
            return JsonResponse({'message' : '잘못된 형식의 비밀번호 입니다'}, status=401)

        if not User.objects.filter(email = user_data['email']).exists() :
            
            User.objects.create(
                name = user_data['name'],
                password = user_data['password'],
                email = user_data['email'],
                phone = user_data['phone']  
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        
        return JsonResponse({'message' : '이미 가입된 회원 입니다'}, status=401)

class LoginView(View):
    def post(self, request):

        """
        1. 목적 : 클라이언트로부터 받은 로그인 목적의 사용자 데이터
        (이메일과 비밀번호를 데이터베이스에 조회하여 일치하는지 확인하고  
        일치 여부에 따라 로그인 성공/실패를 결정)
        2. INPUT : 
        {
            "email"        : "rlafls9596@gamil.com",
            "password"     : "rlagPFls95@"
        }
        3. OUTPUT : 
        성공 시
        {
            "message" : "SUCCESS" , status=201
        }
        """
        try :
            data = json.loads(request.body)
            user = User.objects.get(email__exact=data['email'])
            if user.password == data['password']:
                return JsonResponse({'message' : 'SUCCESS'}, status = 201)
            else :
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
        
        except KeyError :
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError :
            return JsonResponse({"message": "INVALID_USER"}, status = 401)