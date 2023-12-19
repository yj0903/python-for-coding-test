# boj10930 SHA-256
# 난이도 하. 단순 해시라이브러리 사용법

import hashlib

input_data = input()
encode_str = input_data.encode() # 인코드해서 바이트객체 변환
result = hashlib.sha256(encode_str).hexdigest() # sha256 이용해 해시 객체 생성
print(result)

