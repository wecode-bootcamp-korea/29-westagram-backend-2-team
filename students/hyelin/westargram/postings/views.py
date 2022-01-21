from django.views import View

from .models import Board
from users.models import User

from django.http import JsonResponse

class WritePostView(View) :
    #게시글을 작성하는 뷰
    def post(self, request) :
        """
        목적 : post 등록하기
        1. email검사로 유저가 존재하는 경우만 등록가능 
        2. 단, content나 이미지 둘다 공란이 되면 안됨
        보내는 데이터 
        {
            user_data = {
                email = "rlafls9596@gamil.com"
            },
            post_data = {
                writer = 1 ## 이메일의 PK index,
                content = 'blablablablablablablablablablabla'
                image_url = ''
            }
        }
        성공시
            최대 둘 중 나만 공란이면서 가입한 유저인 경우 
        실패시 
            둘다 공란인 경우
            {'message': 'EMPTY_CONTENT'}, status= 400
            없는 유저인 경우
            {'message': 'SUCCESS'} status = 400
            유저 이메일이 공란인 경우
            {'message': 'KEY_ERROR'} status = 400
        """
        try :
            data = json.loads(request.body)
            user = User.objects.get(email__exact=data['email'])
            post_data = data.board

            if post_data.content == '' and post_data.image_url == '' :
                return JsonResponse({'message': 'EMPTY_CONTENT'}, status= 400)
            if User.objects.filter(email = user['email']).exists() :
                Board.objects.create(
                    writer      = user['id'],
                    content     = post_data['content'],
                    image_url   = post_data['image_url']
                )
                return JsonResponse({'message': 'SUCCESS'}, status= 200)
        except KeyError :
            return JsonResponse({'message': 'KEY_ERROR'},   status= 400)
        except ValueError :
            return JsonResponse({'message': 'INVALID_USER'}, status= 400) 
        except DoesNotExist :
            return JsonResponse({'message': 'INVALID_USER'}, status= 400)