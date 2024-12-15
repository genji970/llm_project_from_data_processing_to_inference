
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
