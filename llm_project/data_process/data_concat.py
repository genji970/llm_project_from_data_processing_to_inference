import os
import logging
import shutil
import requests
import ray
from functools import partial


# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PDF 파일을 처리하는 함수 (Ray에서 실행될 작업)
@ray.remote
def process_subdir_ray(subdir, output_dir):
    # 서브 폴더 내 모든 파일 필터링 (PDF만 포함)
    pdf_files = [f for f in os.listdir(subdir)]

    # PDF 파일이 없으면 건너뛰기
    if not pdf_files:
        logger.info(f"Subfolder '{os.path.basename(subdir)}' contains no PDF files. Skipping.")
        return []

    # PDF 파일 복사
    copied_files = []
    for file_name in pdf_files:
        source_path = os.path.join(subdir, file_name)
        destination_path = os.path.join(output_dir, file_name)

        shutil.copy(source_path, destination_path)
        logger.info(f"Copied '{file_name}' from '{os.path.basename(subdir)}' to '{output_dir}'.")
        copied_files.append(file_name)

    return copied_files


class Data_Concat:

    def __init__(self, input_url, input_dir, output_dir):
        self.input_url = input_url

        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        self.input_dir = input_dir
        self.output_dir = output_dir

        self.file_name = os.path.basename(input_url)
        self.file_path = os.path.join(input_dir, self.file_name)

    def download_file(self):
        # Ensure the file name ends with .pdf
        if not self.file_path.endswith('.pdf'):
            self.file_path = os.path.splitext(self.file_path)[0] + '.pdf'

        response = requests.get(self.input_url)
        if response.status_code == 200:
            with open(self.file_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded and saved to {self.file_path}")
        else:
            raise Exception(f"Failed to download file: {self.input_url} (status code: {response.status_code})")

    def gather_files(self):
        """
        :param self.input_dir: 상위 디렉토리(서브 폴더를 검색)
        :param self.output_dir: PDF 파일을 모을 디렉토리
        """
        try:
            # URL 파일 다운로드
            if self.input_url is not None:
                self.download_file()

            # 출력 디렉토리 생성
            if self.output_dir is not None:
                logger.info(f"Output directory '{self.output_dir}' is ready.")

            # 상위 디렉토리에서 서브 폴더 찾기
            subdirs = [os.path.join(self.input_dir, d) for d in os.listdir(self.input_dir) if
                       os.path.isdir(os.path.join(self.input_dir, d))]

            if not subdirs:
                logger.info("No subdirectories found in the input directory.")
                return

            # Ray 병렬 처리
            futures = [process_subdir_ray.remote(subdir, self.output_dir) for subdir in subdirs]
            results = ray.get(futures)

            # 결과 출력
            copied_files = [file for result in results for file in result]
            if not copied_files:
                logger.info("No PDF files were copied.")
            else:
                logger.info(f"Processing complete. Total PDF files copied: {len(copied_files)}")

        except Exception as e:
            logger.exception(f"An error occurred while processing directories with Ray: {e}")
