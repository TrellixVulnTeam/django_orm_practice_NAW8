from django.http import JsonResponse
from django.shortcuts import render
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
