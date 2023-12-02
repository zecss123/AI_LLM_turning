#我是在远程服务器上写的这段GUI无法测试其是否能正常工作，下面给出执行程序使用的命令行参数，
#另外，我在这段代码中的openai_model中更换了URL 由于我的key是中转的。。。所以在代码上和老师有细微区别 但是如果使用老师的命令行指令可以正常解析和运行
import sys
import os
import tkinter as tk
from tkinter import filedialog
from utils import ArgumentParser, ConfigLoader
from model import OpenAIModel
from translator import PDFTranslator

def browse_files():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.pdf*"), ("all files", "*.*")))
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, filename)

def translate():
    model_name = model_name_entry.get()
    api_key = api_key_entry.get()
    model = OpenAIModel(model=model_name, api_key=api_key)

    pdf_file_path = file_path_entry.get()
    file_format = file_format_entry.get()

    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    root = tk.Tk()

    model_name_entry = tk.Entry(root, width=50)
    model_name_entry.pack()
    model_name_entry.insert(0, args.openai_model)

    api_key_entry = tk.Entry(root, width=50)
    api_key_entry.pack()
    api_key_entry.insert(0, args.openai_api_key)

    file_path_entry = tk.Entry(root, width=50)
    file_path_entry.pack()
    file_path_entry.insert(0, args.book)

    file_format_entry = tk.Entry(root, width=50)
    file_format_entry.pack()
    file_format_entry.insert(0, args.file_format)

    browse_button = tk.Button(root, text="Browse files", command=browse_files)
    browse_button.pack()

    translate_button = tk.Button(root, text="Translate", command=translate)
    translate_button.pack()

    root.mainloop()
    #export OPENAI_API_KEY="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123"
    #python ai_translator/test_main.py --model_type OpenAIModel --openai_model gpt-3.5-turbo --openai_api_key "sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123" --book tests/test.pdf --file_format markdown