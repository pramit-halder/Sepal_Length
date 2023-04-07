import numpy as np
import seaborn as sb

def calculate(s):
    df = sb.load_dataset("iris")
    # print(df.head(10))
    X = np.array(df.iloc[:, 0])
    y = np.array(df.iloc[:, 1])
    r_t_bar = np.mean(X * y)
    r_bar = np.mean(y)
    t_bar = np.mean(X)
    t_sq_bar = np.mean(X * X)
    a = (r_t_bar - r_bar * t_bar) / (t_sq_bar - t_bar * t_bar)
    b = (r_t_bar * t_bar - r_bar * t_sq_bar) / (t_bar * t_bar - t_sq_bar)
    return a * s + b

def getsepal(S):
    r = calculate(S)
    return r
