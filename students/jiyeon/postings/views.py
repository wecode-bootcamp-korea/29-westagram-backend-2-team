import json

from django.views import View
from django.http import JsonResponse

from .models import Posting
from users.models import User

class PostingView(View):
    def post(self, request):
        # POST 127.0.0.1:8000/post
        """
        1. 목적 : 클라이언트로부터 받은 사용자 데이터(User id, image_url)를 데이터 베이스에 등록하기 위함
        2. INPUT : 
        {
            "user_id" : 1,
            "img_url" : "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?201812022340",
            "content" : "반갑습니다~~~~"
        }
        3. OUTPUT :
        성공 시
        {
            "message" : "이미지 등록 성공, status=201"
        }
        실패 시
        {
            "message" : "invalid user id", status=400"
        }
        """
        data = json.loads(request.body)

        try:
            img_url = data['img_url']
            user_id = data['user_id']
        except KeyError:
            return JsonResponse({'message' : 'KEY ERROR'}, status=400)
            
        if not User.objects.filter(id=data['user_id']).exists():
            return JsonResponse({"message": f"user_id가 존재하지 않습니다."}, status=400)
    
        Posting.objects.create(
            user_id = user_id,
            img_url = img_url,
            content = data['content']
        )

        return JsonResponse({"message": "url 등록 성공"}, status=201)

    def get(self, request):
        # GET 127.0.0.1:8000/post
        """
        1. 목적 : 데이터베이스에 저장된 내역을 불러와 보여주기 위함
        2. INPUT : X
        3. OUTPUT :
        {
            "name" : "김지연",
            "img_url" : "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?201812022340",
            "content" : "반갑습니다~~~"
            "created_at" "2022-01-19T04:35:12.061Z"
            ""
        }
        """
        posts = Posting.objects.all()
        results = []

        for post in posts:
            user = User.objects.get(id=post.user_id)
            user_name = user.name
            post_dict = {
                'name'       : user_name,
                'img_url'    : post.img_url,
                'content'    : post.content,
                'created_at' : post.created_at
            }
            results.append(post_dict)

        return JsonResponse({"posts" : results}, status=200)
