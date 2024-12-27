import fitz
import os
import requests
import json
import ray

from llm_project_train.utils.data_process_utils.data_process_utils import *

@ray.remote
def data_processing(pdf_path , output_dir):
    """
    단일 PDF 파일을 처리하여 각 페이지를 JSON으로 저장.
    :param pdf_path: 처리할 PDF 파일의 경로
    :param output_dir: JSON 파일을 저장할 디렉토리
    """
    try:
        # PDF 파일 열기
        doc = fitz.open(pdf_path)
        # 모든 텍스트를 저장할 리스트
        extracted_texts = []
        reference_found = False  # 참고 문헌 발견 여부
        # 각 페이지 처리
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")  # 텍스트만 추출

            # 참고 문헌 이후의 페이지는 무시
            if reference_found:
                break

            cleaned_text, reference_found = clean_text(text, page_num, len(doc))

            # 텍스트를 줄 단위로 나눠 필터링
            lines = cleaned_text.split('\n')
            filtered_lines = exclude_if_length_is_too_short(lines , MIN_WORDS=5)

            # 필터링된 텍스트를 저장
            extracted_texts.append(f"Page {page_num + 1}:\n" + "\n".join(filtered_lines) + "\n")

            # 텍스트 파일로 저장
            file_name = os.path.splitext(os.path.basename(pdf_path))[0]
            output_file = os.path.join(output_dir, f"{file_name}.txt")
            with open(output_file, "w", encoding="utf-8") as f:
              f.writelines(extracted_texts)
        doc.close()
        return f"Processed {pdf_path}"
    except Exception as e:
        return f"Error processing {pdf_path}: {e}"

def process_all_pdfs(input_dir , output_dir):
    """
    여러 PDF 파일을 병렬로 처리.
    :param input_dir: PDF 파일들이 위치한 디렉토리
    :param output_dir: 처리 결과를 저장할 디렉토리
    """
    # PDF 파일 목록 가져오기
    pdf_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    if not pdf_files:
        print("No PDF files found in the input directory.")
        return

    # Ray로 병렬 처리
    print("Starting parallel processing...")
    futures = [data_processing.remote(pdf, output_dir) for pdf in pdf_files]

    # 결과 수집
    results = ray.get(futures)

    return results