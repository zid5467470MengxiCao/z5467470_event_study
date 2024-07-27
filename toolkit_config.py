import os

# 项目根目录
PRJDIR = os.path.dirname(os.path.abspath(__file__))

# 数据目录
DATA_DIR = os.path.join(PRJDIR, "project2", "data")

# 股票代码映射
TICKERS = [
    "aal", "aapl", "abbv", "baba", "bac", "csco", "dal", "dis", "fb", "ba",
    "intc", "jnj", "ko", "msft", "nvda", "orcl", "pg", "pypl", "t", "tsla", "tsm"
]

# 数据文件映射
DATA_FILES = {
    "aal": "aal_prc.csv",
    "aapl": "aapl_prc.csv",
    "abbv": "abbv_prc.csv",
    "baba": "baba_prc.csv",
    "bac": "bac_prc.csv",
    "csco": "csco_prc.csv",
    "dal": "dal_prc.csv",
    "dis": "dis_prc.csv",
    "fb": "fb_prc.csv",
    "ba": "ba_prc.csv",
    "intc": "intc_prc.csv",
    "jnj": "jnj_prc.csv",
    "ko": "ko_prc.csv",
    "msft": "msft_prc.csv",
    "nvda": "nvda_prc.csv",
    "orcl": "orcl_prc.csv",
    "pg": "pg_prc.csv",
    "pypl": "pypl_prc.csv",
    "t": "t_prc.csv",
    "tsla": "tsla_prc.csv",
    "tsm": "tsm_prc.csv"
}
