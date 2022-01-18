from email import message
import json 
import re
from urllib import response 
##View
from django.views import View
##Model
from .models import User
##Http
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
        
        ## 1. name누락 
        if 'name' not in user_data :
            return JsonResponse({'message' : '이름을 입력해 주세요'}, status=400)
        ## 2. email 누락 
        if 'email' not in user_data :
            return JsonResponse({'message' : '이메일을 입력해 주세요'}, status=400)
        ## 3. password 누락 
        if 'password' not in user_data :
            return JsonResponse({'message': '비밀번호를 입력해 주세요'}, status=400)
        ## 4. 이메일 양식 비충족
        if not re.fullmatch(REX_EMAIL, user_data['email']) :
            return JsonResponse({'message' : '유효하지 않은 이메일입니다'})
        ## 5. password 양식 비충족 
        if not re.fullmatch(REX_PASS, user_data['password']) :
            return JsonResponse({'message' : '잘못된 형식의 비밀번호 입니다'}, status=401)
        ## 6. 이메일 중복시 -> 이미 가입된 email입니다
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
        data = json.loads(request.body)

        if 'email' not in data  or 'password' not in data :
            return JsonResponse( {"message": "KEY_ERROR"}, status=400)
        ##2. email이나 password 어떤 하나라도 잘못된 입력시 401  {"message": "INVALID_USER"},  {"message": "INVALID_Email"}
        #존재하지 않는 이메일인 겨우
        #이메일은 맞지만 비번이 잘못된 경우
        if User.objects.get(headline__exact=data['email']).exists() :
            if data['password'] == User.objects.get(headline__exact=data['email'])['password'] :
                return JsonResponse({'message' : 'SUCCESS'}, status=201)
            else :
                return JsonResponse({"message": "INVALID_USER"}, status = 401)        
        ##3. 올바른 입력인 경우 -> {'message' : 'SUCCESS'} 로그인 성공 200
        else :
            return JsonResponse({"message": "INVALID_EMAIL"}, status = 401)