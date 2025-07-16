from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyCVfm4a6E6LZU8tkvEkBeybT7kATbjXVQw"

# Gemini 1.5 Flash モデルのインスタンスを作成
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# プロンプトのテンプレート文章を定義
template = """
次の文章を簡潔な英語に翻訳してください。
{sentences_before_check}
"""

# テンプレート文章にあるチェック対象の単語を変数化
prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたは優秀な翻訳者です。"),
    ("user", template)
])

# チャットメッセージを文字列に変換するための出力解析インスタンスを作成
output_parser = StrOutputParser()

# Gemini APIにこのプロンプトを送信するためのチェーンを作成
chain = prompt | llm | output_parser

# チェーンを実行し、結果を表示
print(chain.invoke({"sentences_before_check": "私が誰だかわかりますか？"}))