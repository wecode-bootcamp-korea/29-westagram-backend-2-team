import json
import re

from django.views import View
from django.http  import JsonResponse

from .models import User

class UserView(View):
    def post(self, request):
        # POST 127.0.0.1:8000/user
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
            "message" : "KEY_ERROR", status=400
        }1
        """
        data = json.loads(request.body)

        regex_email    = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._]+[@][a-zA-Z][A-Za-z.]+[.]\w{2,}')
        regex_password = re.compile(r'^(?=.*\w)(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

        try:
            filtered_query = User.objects.get(email=data['email'])
            return JsonResponse({"Duplicate Email" : "이메일이 중복되었습니다."})   
        except User.DoesNotExist:
            pass
   

        if re.fullmatch(regex_email, data['email']) == None: # 이메일 양식에 맞게 입력 되었는지 확인
            
            return JsonResponse({"E-mail Error": "양식에 맞는 메일 주소를 입력해주세요."})
        
        if re.fullmatch(regex_password, data['password']) == None: # 비밀번호 조건에 맞게 입력되었는지 확인
            
            return JsonResponse(
                {"Password Error": "8자리 이상의 알파벳, 숫자, 특수문자(@$!%*?&)를 포함한 비밀번호를 입력해주세요."}
                )

        user = User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = data['password']
        )

        return JsonResponse({"message" : f"사용자 등록 성공, {data['email']}"}, status=201)