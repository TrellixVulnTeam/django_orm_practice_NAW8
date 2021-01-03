from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import F
from .models import *


# N+1 문제
def user_list(request):
    # N+1이 발생하는 쿼리셋
    # users = User.objects.all()

    # N+1은 select_related(), prefetch_related()라는 메서드로 Eager Loading하여 방지할 수 있다.
    # select_related() : 정방향 참조 필드
    # prefetch_related() : 역방향 참조 필드
    users = User.objects.select_related('userinfo')

    for user in users:
        user.userinfo

    return render(request, 'index.html')


# F()
def age_for_f(request):
    userinfo_hong = Userinfo.objects.get(first_name='hong')

    # not used F()
    #userinfo_hong.age += 1

    # use F()
    userinfo_hong.age = F('age') + 1
    userinfo_hong.save()

    # F() 사용시 주의점 => 모델 필드에 할당된 F() 객체는 저장 후에도 유지된다.
    # userinfo_hong.age = F('age') + 1
    # userinfo_hong.save()
    #
    # userinfo_hong.first_name = 'hooong'
    # userinfo_hong.save()    # 'hong'을 가지고 있던 userinfo는 age가 2만큼 증가하게 된다.

    return render(request, 'index.html')
