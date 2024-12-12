import os
import fitz
import nltk
from nltk.tokenize import sent_tokenize
import logging
import ray

# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@ray.remote
class DataParsing:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def txt_search(self):
        """Returns a list of TXT files in the input directory."""
        return [f for f in os.listdir(self.input_dir) if f.endswith(".txt")]

    def txt_parsing(self):
        """Processes the TXT files and tokenizes their content."""
        txt_files = self.txt_search()
        if not txt_files:
            logging.warning("No TXT files found in the input directory.")
            return []

        results = []
        for txt_file in txt_files:
            txt_path = os.path.join(self.input_dir, txt_file)
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    text = f.read()

                # Tokenize sentences
                sentences = sent_tokenize(text)

                # Save tokenized sentences to a new text file
                output_file_path = os.path.join(
                    self.output_dir, f"{os.path.splitext(txt_file)[0]}_tokenized.txt"
                )
                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(sentences))

                logging.info(f"File saved: {output_file_path}")
                results.append(output_file_path)

            except Exception as e:
                logging.error(f"Error processing file {txt_file}: {e}")

        return results