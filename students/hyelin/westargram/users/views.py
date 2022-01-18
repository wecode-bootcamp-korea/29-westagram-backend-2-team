import json 
import re 
##View
from django.views import View
##Model
from .models import User
##Http
from django.http import JsonResponse


class SignUpView (View):
    def post(self, request):
        
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

        