import sys
sys.path.append('..')
import pandas as pd
from utils import load_jsonl, dump_jsonl
from utils import authority_to_eng, closeness_to_eng
import numpy as np

in_dir = "../Task1/"
conversations = load_jsonl(f"{in_dir}/annotated_conersations.jsonl")
for conv in conversations[0:50]:
    print("ROOM ID", conv["room_id"])

    A = None
    for m in conv["messages"]:
        if A is None:
            A = m["user_id"]
            print(m["user_id"])
            break
    #     if m["user_id"]==A:
    #         print(m["user_id"], m["text"])
    #     else:
    #         print("                  ", m["user_id"], m["text"])
        
    # print("=======================")