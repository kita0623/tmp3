import pandas as pd

# サンプルのSeries
series = pd.Series(['123abc', '456def', '789ghi', '10jklm'])

# 各要素の整数部分を抽出する関数
def extract_integer(value):
    # 先頭3文字を取得
    prefix = value[:3]
    # 先頭3文字が整数であれば整数部分として返す
    if prefix.isdigit():
        return int(prefix)
    else:
        return None  # 整数でない場合はNoneを返す

# 各要素に関数を適用して整数部分を抽出する
result = series.apply(extract_integer)

print(result)
