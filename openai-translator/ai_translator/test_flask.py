from flask import Flask, request, jsonify
from test_api_main import run_translator  # 导入你的函数

app = Flask(__name__)

# @app.route('/translate', methods=['POST'])
# def translate():
#     #model_type=OpenAIModel, openai_api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123", file_format='markdown', book='tests/test.pdf', openai_model='gpt-3.5-turbo', config_file='/root/openai-quickstart/openai-quickstart/openai-translator/config.yaml'
#     data = request.get_json()
#     model_type = data.get('model_type')
#     openai_api_key = data.get('openai_api_key')
#     file_format = data.get('file_format')
#     book = data.get('book')
#     openai_model = data.get('openai_model')
#     config_file = data.get('config_file')  # 如果你的配置文件路径是可变的，你也可以将其作为参数
#     result = run_translator(model_type='OpenAIModel', openai_api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123", file_format='markdown', book='tests/test.pdf', openai_model='gpt-3.5-turbo', config_file='/root/openai-quickstart/openai-quickstart/openai-translator/config.yaml')
#     return jsonify({'result': result})
@app.route('/translate', methods=['GET'])
def translate():
    model_type = request.args.get('model_type')
    openai_api_key = request.args.get('openai_api_key')
    file_format = request.args.get('file_format')
    book = request.args.get('book')
    openai_model = request.args.get('openai_model')
    config_file = request.args.get('config_file')
    result = run_translator(model_type='OpenAIModel', openai_api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123", file_format='markdown', book='tests/test.pdf', openai_model='gpt-3.5-turbo', config_file='/root/openai-quickstart/openai-quickstart/openai-translator/config.yaml')
    return jsonify({'result': result})
@app.route('/favicon.ico')
def favicon():
    return ''
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)