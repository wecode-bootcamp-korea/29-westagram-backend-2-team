import json
from telnetlib import STATUS
#view  class import
from django.views import View
# user Model import 
from user.models import User
#Http
from django.http import HttpResponse
# http response return 
from urllib import response
#from django.shortcuts import render
## login시 인증을 위한 패키지 
from django.contrib.auth import authenticate,login

def sign_up(request, user_info):
    # 이름 
    # 이메일 없을 시 400 error @하나와 . 하나씩만 반드시 포함되어야 한다
    # PASSWORD 없을 시 400 error 8글자 이상 문자 숫자 특수문자의 조합 
    # 휴대폰 그 외
    if request.method == 'POST':
        user = User.object.all()
        print(f"sign_up user info :: {user}")
        result = []
        for info in user :
            result.append(
                {
                    "name"  : info.name,
                    "email" : info.email,
                    "password" : info.password,
                    "phone" : info.phone
                }
            )
        print(f"results :: object :: {result}")
    return JsonResponse({"user ::" : result}, status=200)

def sign_in(request, user_info):
    # 1. 아이디는 맞는데 비번 틀림 -> 틀린 정보
    # 2. 아이디없 , 비번 틀린지 아닌지 검사 필요X -> 가입하지 않은 회원
    # 3. 아이디 맞 비번  맞 -> 로그인 성공
    if request.method == "POST":
        name = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username = name, password = password)
        if user is not None :
            print ("로그인 성공")
            login(request, user) #이 뒤로는 로그인 상태!
        else:
            print("로그인 실패")
    return HttpResponse("로그인 기능 구현")
def logout (request,user_info):
    # 이미 로그인 세션이 있는 상태니 -> 일반 비회원으로 전환하는 토큰을 발행
    # 안전하게 로그아웃 성공시 성공 반환 실패시에도 억지로 반환? 
    return HttpResponse("로그아웃 완료")