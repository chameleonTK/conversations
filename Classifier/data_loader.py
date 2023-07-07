import sys
sys.path.append('..')

import pandas as pd
from utils import load_jsonl, dump_jsonl, set_random_seed
import numpy as np
import random


def run_preprocess(train, val, test):
    train["text"] = train["text"].apply(preprocess)
    val["text"] = val["text"].apply(preprocess)
    test["text"] = test["text"].apply(preprocess)

    # print(train["label"].unique())
    # print(val["label"].unique())
    # print(test["label"].unique())

    return train, val, test

def get_task1_conver(in_dir, col_label, skips=[], seed=None, only_user=True):
    conversations = load_jsonl(f"{in_dir}")

    def to_message_str(messages, users):
        s = ""
        for m in messages:
            if only_user and users[m['user_id']]!="USR":
                continue
            s += f"{users[m['user_id']]} {m['text']} \n"
        return s
        
    newdata = []
    for row in conversations:
        row["messages"].sort(key=lambda x: x["date_created"], reverse=False)
        
        users = {}
        for m in row["messages"]:
            if m["user_id"] not in users:
#                 username = "USR"+str(len(users)+1) if len(users.keys())==0 else "SYS"
                username = "USR" if len(users.keys())==0 else "SYS"
                users[m["user_id"]] = username
                
#         if len(users)>2:
#             print("More than 1 users", len(users))
        
        
        messages = row["messages"]
        chunk_size = 100
        for i in range(0, len(messages), chunk_size):
            sub_messages = messages[i:i+chunk_size]
            s = to_message_str(sub_messages, users)
            
            if pd.isna(row[col_label]):
                continue
            
            if row[col_label] in skips:
                continue

            label = row[col_label]

            newdata.append({
                "text": s,
                "label": label
            })
        
    n_val = int(len(newdata)*0.05)
    n_test = n_val

    if seed is not None:
        random.seed(seed)
        random.shuffle(newdata)
    
    test = newdata[0:n_test]
    val = newdata[n_test:n_test+n_val]
    train = newdata[n_test+n_val:]
    
    print("N", len(train), len(val), len(test))
    return pd.DataFrame(train), pd.DataFrame(val), pd.DataFrame(test)


def get_task2_conver(in_dir, col_label, skips=[], only_user=True):
    conversations = load_jsonl(f"{in_dir}")
    # print(len(conversations))
    newdata = []
    for row in conversations:
        row["messages"].sort(key=lambda x: x["created_at"], reverse=False)
        
        users = {}
        for m in row["messages"]:
            if m["user_id"] not in users:
#                 username = "USR"+str(len(users)+1) if len(users.keys())==0 else "SYS"
                username = "USR" if len(users.keys())!=0 else "SYS"
                users[m["user_id"]] = username
                
        if len(users)>2:
            print("More than 1 users", len(users))
        
        
        
        messages = row["messages"]
        s = ""
        for m in messages:
            text = m['text'].replace("[USR]", "").replace("[URL]", "URL")
            if only_user and users[m['user_id']]!="USR":
                continue
            
            s += f"{users[m['user_id']]} {text} \n"
        
        label = row[col_label]
            
        if pd.isna(label):
            continue
        
        if label in skips:
            continue
                
        newdata.append({
            "text": s,
            "label": label
        })
                
            
    n_val = int(len(newdata)*0.1)
    n_test = n_val
    
    test = newdata[0:n_test]
    val = newdata[n_test:n_test+n_val]
    train = newdata[n_test+n_val:]
    
    print("N", len(train), len(val), len(test))
    return pd.DataFrame(train), pd.DataFrame(val), pd.DataFrame(test)


from itertools import groupby
def preprocess(text):
    text = text.lower()

    # handle repeted charecters
    s = ""
    for k,v in groupby(text):
        n = len(list(v))
        s += k*min(n, 4)
        if n >= 4:
          s += " rep "

    text = s
    
    return text