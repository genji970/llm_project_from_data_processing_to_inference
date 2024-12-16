def clean_response(response):
    """
    첫 번째 A: 응답만 남기고 이후 A:, Q:, An:을 포함한 모든 반복 제거
    """
    # 줄 단위로 분리
    lines = response.splitlines()

    # 첫 번째 A:만 남기기
    cleaned_response = []
    first_a_found = False
    for line in lines:
        # 첫 번째 A:만 추가
        if line.startswith("A:") and not first_a_found:
            parts = line.split("A:")
            if len(parts) > 2:
                line = parts[2:]
            cleaned_response.append(line)
            first_a_found = True

    # 줄 단위로 결합
    return "\n".join(cleaned_response)