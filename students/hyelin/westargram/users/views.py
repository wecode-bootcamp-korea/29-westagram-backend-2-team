import json #json형태의 객체용
import re #정규식 연산용
import bcrypt #암호화
##View
from django.views import View
##Model
from .models import User
##Http
from django.http import JsonResponse


class SignUpView (View):
    def post(self, request):
        
        user_data   = json.loads(request.body)
        
        REX_EMAIL   = r'^[0-9A-Za-z][0-9A-Za-z._]+[@][A-Za-z][A-Za-z.]+[.]\w{2,}'
        REX_PASS    = r'^(?=.*\w)(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        
        ## 1. name누락 
        if 'name' not in user_data :
            return JsonResponse({'message' : '이름을 입력해 주세요'}, status=400)
        ## 2. email 누락 
        if 'email' not in user_data :
            return JsonResponse({'message' : '이메일은 필수입니다'}, status=400)
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
            password    = user_data['password'].encode('utf-8')
            hash_pass   = bcrypt.hashpw(password, bcrypt.getsalt())
            User.objects.create(
                name = user_data['name'],
                password = hashed_password,
                email = user_data['email'],
                phone = user_data['phone']        
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        
        return JsonResponse({'message' : '이미 가입된 회원 입니다'}, status=401)

        
        

class LoginView (View):    
    ## 이메일 입력 누락시 
    ## PW입력 누락시
    ## email맞, pw틀
    ## email 존재 X 
    ##  올바른 email과 pw

    def post(self,request):
        
        return JsonResponse({'message' : '이메일을 입력해 주세요'}, status=400)
        
 
class LogoutView (View):
    ## 세션이 들어오면 :expired 처리하기
    def post(self, request):
        return JsonResponse({'message' : '로그아웃처리 완료'}, status=200)