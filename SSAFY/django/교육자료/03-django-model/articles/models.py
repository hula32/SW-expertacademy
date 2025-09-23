# 내장된 django 패키지 안에 db 서브 패키지 안에 models.py라는 모듈을 사용 
from django.db import models

# Create your models here.
class Article(models.Model):
    # 이름이 파스칼 케이스 -> 이 친구들 클래스구나! -> 클래스로 인스턴스(title, content)를 만든 것 
    title = models.CharField(max_length=10) # 생성자 함수일 경우 초기값 제공해야함 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간을 표현 
    updated_at = models.DateTimeField(auto_now=True)
