import time
from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)
# 셀러리 인스턴스 하나 만들고


# 작업으로 붙여놈
# 이 작업을 브로커에 전달할 수 있고
# 작업자를 실행시키면 작업자도 등록된 작업자를 처리할 수 있어요.
# 지금은 레디스 서버가 있으니까. 그걸 실행.
# 레디스 슬거면 이렇게.
# 우리가 설정한게 뭐냐면
# 태슼크 브로커 뭐할지도 써놓고
# 작업자 서버도 키면되요.
# 작업자 서버 다른곳에 둘 수도 잇어요.
# task.py가 ㅣㅇㅆ는고세어

@app.task
def add(x, y):
    time.sleep(5)
    return x + y