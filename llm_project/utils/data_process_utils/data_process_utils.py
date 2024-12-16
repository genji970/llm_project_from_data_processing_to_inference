## if len(word) is too short, delete ##
def exclude_if_length_is_too_short(lines : [] , MIN_WORDS : int) -> []:

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

def clean_text(text: str, page_num: int, total_pages: int) -> tuple:
    """
    텍스트 클리닝 함수: 참고 문헌이 시작된 페이지 이후의 모든 내용 제거
    :param text: 현재 페이지의 텍스트
    :param page_num: 현재 페이지 번호
    :param total_pages: 전체 페이지 수
    :return: 정제된 텍스트와 제거 여부 플래그
    """
    # 참고 문헌 키워드가 있는지 확인
    for keyword in ["References"]:
        idx = text.find(keyword)
        if idx != -1:
            # 키워드 발견 시 해당 페이지 이후는 모두 제거
            return text[:idx], True  # 현재 페이지는 키워드 이전까지만 남김

    return text, False
