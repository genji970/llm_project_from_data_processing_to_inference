## if len(word) is too short, delete ##
def exclude_if_length_is_too_short(MIN_WORDS : int , lines : []) -> []:

# 특정 단어 수 미만인 줄 필터링
filtered_lines = []
for line_number, line in enumerate(lines, start=1):
    # 줄의 앞뒤 공백 제거 후 단어로 분리
    words = line.strip().split()
    word_count = len(words)
    
    # 단어 수가 기준 이상인 경우에만 추가
    if word_count >= MIN_WORDS:
        filtered_lines.append(line)
    return filtered_lines

## deleting title , author name , reference , etc except main text words ##
import re

def clean_text(self, text : 'text') -> 'text' :
        """
        텍스트 클리닝 함수: 저자, 제목, 그래프/차트, 참고 문헌 제거
        :param text: 원본 텍스트
        :return: 정제된 텍스트
        """
        # 1. 저자 및 제목 제거
        # 일반적으로 첫 페이지에 위치, 'Abstract' 또는 'Introduction' 전에 끝남
        # 정규 표현식을 사용하여 첫 번째 'Abstract' 또는 'Introduction'까지 제거
        abstract_pattern = re.compile(r'\b(Abstract|INTRODUCTION)\b', re.IGNORECASE)
        match = abstract_pattern.search(text)
        if match:
            text = text[match.start():]
        else:
            # 'Abstract'나 'Introduction'가 없을 경우 첫 1000자만 유지
            text = text[:1000] + text[1000:]

        # 2. 그래프 및 차트 제거
        # 'Figure'나 'Table' 등의 키워드가 포함된 줄 제거
        lines = text.split('\n')
        cleaned_lines = []
        figure_pattern = re.compile(r'\b(Figure|Table)\s+\d+', re.IGNORECASE)
        for line in lines:
            if not figure_pattern.search(line):
                cleaned_lines.append(line)
        text = '\n'.join(cleaned_lines)

        # 3. 참고 문헌 제거
        # 'References' 또는 'Bibliography' 이후의 모든 내용 제거
        references_pattern = re.compile(r'\b(References|Bibliography)\b', re.IGNORECASE)
        match = references_pattern.search(text)
        if match:
            text = text[:match.start()]

        # 4. 추가 클리닝 (필요 시)
        # 중복 공백 제거, 특수 문자 제거 등
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()

        return text
