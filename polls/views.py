from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. 실습중입니다.")

def coffee(request):
    return HttpResponse("아메리카노, 에스프레소, 카페라떼, 초코라떼, 카푸치노, 모카, 콜드브루, 드립커피, 마끼아또, 아인슈페너, 프렌치 프레스, 콘 파냐, 아이리쉬 커피")

def Korean_food(request):
    return HttpResponse("비빔밥, 간장게장, 불고기, 국밥, 제육볶음, 김치, 삼겹살, 야채곱창")
