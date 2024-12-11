import argparse

# ArgumentParser 객체 생성
parser = argparse.ArgumentParser(description="이 프로그램은 명령줄 옵션을 처리합니다.")

# 명령줄 옵션 추가
parser.add_argument("run_mode", type=str, choices=["app_execution", "chat_execution"],
                    help="Run mode: 'app_execution' for app or 'chat_execution' for chatbot.")