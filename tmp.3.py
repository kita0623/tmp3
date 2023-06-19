
# DataFrame1の例
df1 = pd.DataFrame({
    'JANcode': ['111', '222', '333', '444', '555'],
})
display(df1)

# DataFrame2の例
df2 = pd.DataFrame({
    'JANcode_fm': ['111', '333', '555'],
    'JANcode_to': ['XXX', 'YYY', 'ZZZ']
})
display(df2)

# DataFrame1の'JANcode'のユニーク値を取得
unique_jancode = df1['JANcode'].unique()

# DataFrame2の'JANcode_fm'のユニーク値を取得
unique_jancode_fm = df2['JANcode_fm'].unique()

# DataFrame1の'JANcode'を置換処理
df1.loc[df1['JANcode'].isin(unique_jancode_fm), 'JANcode'] = df1['JANcode'].map(
    df2.set_index('JANcode_fm')['JANcode_to']
)

# 置換後のDataFrame1を表示
display(df1)




df_corr = df_X.corr() 
plt.figure(figsize=(25, 10))
sns.heatmap(df_corr, vmax=1, vmin=-1, center=0, annot=True, fmt=".2f", cmap='jet')


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



# DataFrameから特定のユニーク値（リストで指定）を持つレコードを抽出する

data = {
    '名前': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],
    '年齢': [25, 30, 35, 40, 25],
    '性別': ['女性', '男性', '男性', '男性', '女性']
}

df = pd.DataFrame(data)
display(df)

print()

target_values = ['Alice', 'Charlie']  # リストで指定 
filtered_df = df[df['名前'].isin(target_values)]
display(filtered_df)




import time
start_time = time.time()

def elapsed_time(t):
    elapsed_time = int(time.time() - t)

    elapsed_hour = elapsed_time // 3600
    elapsed_minute = (elapsed_time % 3600) // 60
    elapsed_second = (elapsed_time % 3600 % 60)

    print(str(elapsed_hour).zfill(2) + ":" + str(elapsed_minute).zfill(2) + ":" + str(elapsed_second).zfill(2))

t_ = time.time()
elapsed_time(t_)



# 決定木モデルの作成とフィット
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# 特徴量の重要度の取得
importance = model.feature_importances_

# 重要度を降順にソート
feature_importance = pd.Series(importance, index=X.columns).sort_values(ascending=False)

# 特徴量の重要度の可視化
plt.figure(figsize=(10, 6))
feature_importance.plot(kind='bar')
plt.title('Feature Importance')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.show()