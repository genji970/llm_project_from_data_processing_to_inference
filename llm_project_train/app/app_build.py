from flask import Flask, request, jsonify
from langchain import OpenAI, LLMChain, PromptTemplate

from agent.agent_main import *

import os

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "질문을 입력해주세요."}), 400
    response = chain.run({"question": question})
    return jsonify({"answer": response})


