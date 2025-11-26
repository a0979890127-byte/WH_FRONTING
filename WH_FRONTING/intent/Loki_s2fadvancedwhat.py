#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for s2fadvancedwhat

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
from random import sample
import json
import os

INTENT_NAME = "s2fadvancedwhat"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULE_DICT = {
    "Account": import_from_path("WH_FRONTING_lib_Account", os.path.join(os.path.dirname(CWD_PATH), "lib/Account.py")),
    "LLM": import_from_path("WH_FRONTING_lib_LLM", os.path.join(os.path.dirname(CWD_PATH), "lib/LLM.py"))
}
"""
Account 變數清單
[變數] BASE_PATH         => 根目錄位置
[變數] LIB_PATH          => lib 目錄位置
[變數] INTENT_PATH       => intent 目錄位置
[變數] REPLY_PATH        => reply 目錄位置
[變數] ACCOUNT_DICT      => account.info 內容
[變數] ARTICUT           => ArticutAPI (用法：ARTICUT.parse()。 #需安裝 ArticutAPI.)
[變數] USER_DEFINED_FILE => 使用者自定詞典的檔案路徑
[變數] USER_DEFINED_DICT => 使用者自定詞典內容
"""
REPLY_PATH = MODULE_DICT["Account"].REPLY_PATH
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
ARTICUT = MODULE_DICT["Account"].ARTICUT
USER_DEFINED_FILE = MODULE_DICT["Account"].USER_DEFINED_FILE
USER_DEFINED_DICT = MODULE_DICT["Account"].USER_DEFINED_DICT
getLLM = MODULE_DICT["LLM"].getLLM

# userDefinedDICT (Deprecated)
# 請使用 Account 變數 USER_DEFINED_DICT 代替
#userDefinedDICT = {}
#try:
#    userDefinedDICT = json.load(open(os.path.join(CWD_PATH, "USER_DEFINED.json"), encoding="utf-8"))
#except:
#    pass

replyDICT = {}
replyPathSTR = os.path.join(REPLY_PATH, "reply_{}.json".format(INTENT_NAME))
if os.path.exists(replyPathSTR):
    try:
        replyDICT = json.load(open(replyPathSTR, encoding="utf-8"))
    except Exception as e:
        print("[ERROR] reply_{}.json => {}".format(INTENT_NAME, str(e)))
CHATBOT = True if replyDICT else False

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if ACCOUNT_DICT["debug"]:
        print("[{}] {} ===> {}".format(INTENT_NAME, inputSTR, utterance))

def getReply(utterance, args):
    replySTR = ""
    try:
        replySTR = sample(replyDICT[utterance], 1)[0]
        if args:
            replySTR = replySTR.format(*args)
    except:
        pass

    return replySTR

getResponse = getReply

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    debugInfo(inputSTR, utterance)

    # 確保 resultDICT["FT"] 存在
    if "FT" not in resultDICT:
        resultDICT["FT"] = []

    if utterance == "李四特別喜歡那本書":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "李四讀完文件後就丟掉了":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "每個人都會買帽子":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            # 這句沒有明確人名，args 可能為空，需要避免錯誤
            if args:
                resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))
            else:
                resultDICT["FT"].append("誰會買帽子")

    if utterance == "這朵花馬莉最喜歡":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "那份文件，他拿去丟掉了":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            # args[0] 會是「他」
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "那本書非常暢銷":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            # 自然語意：詢問「什麼非常暢銷」→ 不是問「誰」
            # 但照老師規則仍採用 "誰" 模式，如果 args 可能為空需處理
            if args:
                resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))
            else:
                resultDICT["FT"].append("什麼非常暢銷")

    if utterance == "那篇文章，李四從不看":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "馬莉一定會買帽子":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    if utterance == "馬莉買了書":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["FT"].append("誰" + inputSTR.replace(args[0], ""))

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("馬莉買了書", "馬莉買了書", ["馬莉"], {"FT": []}, {})
    pprint(resultDICT)
