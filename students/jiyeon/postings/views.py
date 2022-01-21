import json

from django.views import View
from django.http import JsonResponse

from .models import Posting
from users.models import User

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            img_url = data['img_url']
            user_id = data['user_id']
            content = data['content']
        except KeyError:
            return JsonResponse({'message' : 'KEY ERROR'}, status=400)
            
        if not User.objects.filter(id=data['user_id']).exists():
            return JsonResponse({'message': f'user_id가 존재하지 않습니다.'}, status=400)
    
        Posting.objects.create(
            user_id = user_id,
            img_url = img_url,
            content = content
        )

        return JsonResponse({'message': 'url 등록 성공'}, status=201)

    def get(self, request):
        posts = Posting.objects.all()

        results = [ 
            {
                'user'       : User.objects.get(id=post.user_id).name,
                'img_url'    : post.img_url,
                'content'    : post.content,
                'created_at' : post.created_at,
                'updated_at' : post.updated_at
            }
            for post in posts]

        return JsonResponse({"posts" : results}, status=200)