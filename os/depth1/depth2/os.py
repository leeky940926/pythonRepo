import os

# 현재 위치를 절대경로로 나타냄
r1 = os.path.abspath(__file__)

# 현재 위치(파일명)
r2 = os.path.basename(__file__)

# 공통 경로
r3 = os.path.commonprefix(['/usr/lib', '/usr/link/lib'])

# 현재 디렉토리
r4 = os.path.dirname(__file__)

# 첫 번째 파라미터로 설정된 경로에 두 번째 파라미터 경로를 합침
r5 = os.path.join(__file__, 'foo')

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
