# ✅ 1. 공식 Python 이미지 사용
FROM python:3.10

# ✅ 2. 작업 디렉토리 설정
WORKDIR /api

# ✅ 3. 필요한 파일 복사
COPY requirements.txt .

# ✅ 4. 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# ✅ 5. 앱 코드 복사
COPY . .

# ✅ 6. FastAPI 실행 (Uvicorn 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
