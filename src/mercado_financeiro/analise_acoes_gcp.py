#%%
import os
from dotenv import load_dotenv
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.cloud import bigquery

#%%
#============================Congiguração do GCP============================
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
TABLE_ID = os.getenv("TABLE_ID")