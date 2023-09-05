import json
from tqdm import tqdm
import os
import random
import numpy as np
import pandas as pd
# import torch

def dump_jsonl(output_path, data, append=False, progress=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        if progress:
            data = tqdm(data)
            
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))

def load_jsonl(input_path, verbose=True, progress=False) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        if progress:
            f = tqdm(f)
            
        for line in f:
                data.append(json.loads(line.rstrip('\n|\r')))
    
    if verbose:
        print('Loaded {} records from {}'.format(len(data), input_path))
        
    return data

def set_random_seed(seed=42):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)    
    np.random.seed(seed)
    np.random.RandomState(seed)

    # torch.manual_seed(seed) 
    # torch.cuda.manual_seed(seed)
    # torch.cuda.manual_seed_all(seed) #seed all gpus    
    # torch.backends.cudnn.deterministic = True
    # torch.backends.cudnn.enabled = False  
    # torch.backends.cudnn.benchmark = False

CLOSENESS_LABELS = ['1. Close', '2. Know each other', "3. Don't know each other", "4. Don't like each other"]
AUTHORITY_LABELS = ['0. Very respect', '1. Respect',  '2. Normal', '3. Not respect']