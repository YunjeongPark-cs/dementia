import pandas as pd
import numpy as np

from eunjeon import Mecab

import torch
from torch import nn, Tensor
import torch.nn.functional as F
from torch.nn import TransformerEncoder, TransformerEncoderLayer
from torch.optim import AdamW
from torch.utils.data import dataset

import torchtext.transforms as T
from torchtext.nn import MultiheadAttentionContainer, InProjContainer, ScaledDotProduct
from torchtext.data import get_tokenizer
from torchtext.vocab import vocab
from torchtext.transoforms import VocabTransform, ToTensor
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

from collections import Counter, OrderedDict

import math


dataset = pd.read_csv('dataset')

dataset_k = dataset[:1000]
dataset_k = dataset_k.set_index("Unnamed: 0")
dataset_k.columns = ["input", "label"]
dataset_k = dataset_k.astype({label':'int'})

df_x = dataset_k['input']
df_y = dataset_k['label']

tokenizer = get_tokenizer(Mecab().morphs, language='ko')


