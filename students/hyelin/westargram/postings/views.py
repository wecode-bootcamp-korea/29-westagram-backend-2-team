from django.views import View
from .models import Post

from django.http import JsonResponse

class WritePostView(View) :
    #게시글을 작성하는 뷰
    def post(self, request) :
        ## 1. 필수 있어야 하는 것  :제목. 내용 작성자(email)
        ## 2. 사용자의 이메일로 아이디 조회하여 
        ## 3. 누락 부분이 있는지 확인하고
        ## 4. 게시글 등록하기 
        return 0
    def get (self, request) :
        return 0