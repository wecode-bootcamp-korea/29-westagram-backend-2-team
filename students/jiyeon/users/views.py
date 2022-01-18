import json
import re

from django.views import View
from django.http  import JsonResponse
import bcrypt
import jwt

from .models import User
from my_settings import ALGORITHM, SECRET_KEY

class SignupView(View):
    def post(self, request):
        # POST 127.0.0.1:8000/signup
        """
        1. 목적 : 클라이언트로부터 받은 사용자 데이터
        (이름, 이메일, 비밀번호, 연락처, 그외 개인정보)를 데이터베이스에 등록하기 위함
        2. INPUT : 
        {
            "name"         : "김지연",
            "email"        : "jiyeon@email.com",
            "password"     : "jiyeon_KIM_pw^^",
            "phone_number" : "01012345678"
        }
        3. OUTPUT : 
        성공 시
        {
            "message" : "사용자 등록 성공, jiyeon@email.com", status=201
        }
        실패 시
        {
            "message" : "E-mail Error": "양식에 맞는 메일 주소를 입력해주세요.", status=400
        }
        """
        data = json.loads(request.body)

        REGEX_EMAIL    = r'^[a-zA-Z0-9][a-zA-Z0-9._]+[@][a-zA-Z][A-Za-z.]+[.]\w{2,}'
        REGEX_PASSWORD = r'^(?=.*\w)(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if 'email' not in data:

            return JsonResponse({'message': 'email을 입력해주세요.'}, status=400)

        if 'password' not in data:

            return JsonResponse({'message': 'password를 입력해주세요.'}, status=400)
        
        if not re.fullmatch(REGEX_EMAIL, data['email']): # 이메일 양식에 맞게 입력 되었는지 확인
            
            return JsonResponse({"E-mail Error": "양식에 맞는 메일 주소를 입력해주세요."}, status=400)
        
        if not re.fullmatch(REGEX_PASSWORD, data['password']): # 비밀번호 조건에 맞게 입력되었는지 확인
            
            return JsonResponse(
                {"Password Error": "8자리 이상의 알파벳, 숫자, 특수문자(@$!%*?&)를 포함한 비밀번호를 입력해주세요."}
                ,status=400)

        if not User.objects.filter(email=data['email']).exists():
            password        = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = hashed_password.decode('utf-8'),
                phone_number  = data['phone_number']
            )
            return JsonResponse({"message" : f"사용자 등록 성공, {data['email']}"}, status=201)

        return JsonResponse({"E-mail Error": "이미 가입된 회원입니다."}, status=401)

class LoginView(View):
    def post(self, request):
        # POST 127.0.0.1:8000/login
        """
        1. 목적 : 클라이언트로부터 받은 사용자 데이터(이메일, 비밀번호)를 데이터베이스와 대조하여
                 인증하는 용도
        2. INPUT : 
        {
            "email"        : "jiyeon@email.com",
            "password"     : "jiyeon_KIM_pw^^"
        }
        3. OUTPUT : 
        성공 시
        {
            "message" : "사용자 로그인 성공, jiyeon@email.com", status=200
        }
        실패 시
        {
            "message" : 사용자 로그인 실패, 이메일 혹은 비밀번호를 확인해주세요.", status=401
        }
        """
        data = json.loads(request.body)

        if 'email' not in data:

            return JsonResponse({'message': 'email을 입력해주세요.'}, status=400)

        if 'password' not in data:

            return JsonResponse({'message': 'password를 입력해주세요.'}, status=400)

        if not User.objects.filter(email=data['email']).exists():

            return JsonResponse({'message': '존재하지 않는 이메일입니다.'}, status=401)
        
        password        = data['password'].encode('utf-8')
        user            = User.objects.get(email=data['email'])
        hashed_password = user.password.encode('utf-8')

        if not bcrypt.checkpw(password, hashed_password):
             
            return JsonResponse({'message': '비밀번호를 확인해주세요.'}, status=401)

        token = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm=ALGORITHM)

        return JsonResponse({'message': '로그인 성공', 'token': token}, status=200)