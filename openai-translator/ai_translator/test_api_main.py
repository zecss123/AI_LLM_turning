# import sys
# import os

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from utils import ArgumentParser, ConfigLoader, LOG
# from model import GLMModel, OpenAIModel
# from translator import PDFTranslator
# # 在 main.py 中
# def run_translator(model_type=OpenAIModel, openai_api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123", file_format='markdown', book='tests/test.pdf', openai_model='gpt-3.5-turbo'):
#     # 在这里运行你的主程序，并返回结果
#     argument_parser = ArgumentParser()
#     args = argument_parser.parse_arguments()
#     config_loader = ConfigLoader(args.config)

#     config = config_loader.load_config()

#     model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
#     api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
#     model = OpenAIModel(model=model_name, api_key=api_key)


#     pdf_file_path = args.book if args.book else config['common']['book']
#     file_format = args.file_format if args.file_format else config['common']['file_format']

#     # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
#     translator = PDFTranslator(model)
#     translator.translate_pdf(pdf_file_path, file_format)
# # 在 main.py 中
#这里是改完后的可以用api调用的main方法,但是其返回结果由于是日志信息所以是null
from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

def run_translator(model_type=OpenAIModel, openai_api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123", file_format='markdown', book='tests/test.pdf', openai_model='gpt-3.5-turbo', config_file='/root/openai-quickstart/openai-quickstart/openai-translator/config.yaml'):
    # 加载配置
    config_loader = ConfigLoader(config_file)
    config = config_loader.load_config()

    # 设置参数
    model_name = openai_model if openai_model else config['OpenAIModel']['model']
    api_key = openai_api_key if openai_api_key else config['OpenAIModel']['api_key']
    pdf_file_path = book if book else config['common']['book']
    file_format = file_format if file_format else config['common']['file_format']

    # 创建模型和翻译器
    model = OpenAIModel(model=model_name, api_key=api_key)
    translator = PDFTranslator(model)

    # 运行翻译器并返回结果
    return translator.translate_pdf(pdf_file_path, file_format)
if __name__ == "__main__":
    print(run_translator())
#    curl -X POST http://127.0.0.1:5000/translate -H "Content-Type: application/json" -d '{    "model_type": "OpenAIModel",    "openai_api_key": "sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123",    "file_format": 'markdown',    "book": 'tests/test.pdf',    "openai_model": 'gpt-3.5-turbo',   "config_file": '/root/openai-quickstart/openai-quickstart/openai-translator/config.yaml'}'