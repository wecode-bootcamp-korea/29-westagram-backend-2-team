import json

from django.view  import view
from django.http  import JsonResponse

from .models      import posting
from users.models import User

# Create your views here.
class PostingView(View):
    def post(self, request) :

        """
        1. 목적 : 클라이언트로부터 받은 데이터를 입력
        2. input :
        {
            "user_id" : 1
            "img_url" : "주소"
            "content" : "안녕하세요!"
        }
        3. output :
        성공
        {
        "message" : "success, status=201"

        }
        실패
        {
        "message" : "fail, status=400"
        }
        """

        data = json.loads(request.body)

        try:
            user_id = data['user_id']
            img_url = data['img_url']
        except KeyError:
            return JsonResponse({'message' : 'KeyError'}, status=400)

        if not User.objects.filter(id=data['user_id']).exists():
            return JsonResponse({'message' : '아이디가 존재하지않습니다'}, status=400)

        Posting.objects.create(
            user_id = user_id,
            img_url = img_url
            content = data['content']
        )

        return JsonResponse({'message' : "등록완료!"}, status=201)

        def get(self, request):
            """
            1. 목적
            데이터베이스의 저장된 내용을 가져와서 보여줌
            2. input
            없음
            3. output
            "name" : "나지현"
            "img_url" : "이미지 주소
            "content" : "안녕하세요"
            "created_at" : "생성된 시간"
            """

            posts = posting.objects.all()
            results = []

            for post in posts:
                user = User.objects.get(id=post.user_id)
                post_dict = {
                    'name'   : user_name,
                    'img_url' : post.img_url,
                    'content' : post.content,
                    'created_at' : post.created_at
                }
                results.append(post_dict)

            return JsonResponse({"posts" : results}, status = 200)
