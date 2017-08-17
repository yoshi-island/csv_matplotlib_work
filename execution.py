#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import linecache
import re

# ===========================

# vars
# optional(comment out)
#file_name = "test.csv" # 分析するファイル（カレントパス）
#header_count = 2 # 見出しの行数（データでないところ）
#y_cols = [0, 2]

# ===========================

# グラフの種類
sns.set_style("whitegrid")

# filepath
try:
  file_name
except NameError:
  print("=================")
  print("file name? [ex. test.csv]")
  filepath = "./" + sys.stdin.readline()
  filepath = filepath.replace("\n", "")
else:
  filepath = "./" + file_name

# ファイルを開く
data = open(filepath, "rU")


# 見出し行の処理
try:
  header_count
except NameError:
  i = 1
  while i <= 10:
    print(str(i) + ": " + linecache.getline(filepath, i))
    i += 1
  print("=================")
  print("how many header line? [ex. 2]")
  header_line = sys.stdin.readline()
  header_line = int(header_line)
else:
  header_line = header_count # ヘッダの行数
c = 1 + header_line # ヘッダの行数の次の行からデータ取るか
header_list = []
header_list = re.split(",",linecache.getline(filepath, header_line)) # ヘッダの見出し取得


# 何列目の項目を分析するか
try:
  y_cols
except NameError:
  i = 0
  for h in header_list:
    print(str(i) + ": " + h)
    i += 1
  print("=================")
  print("which want you to analyze? [ex. 0, 2]")
  y_cols = sys.stdin.readline()
  y_cols = y_cols.replace(" ","").replace("\n", "").split(",")
  for n in y_cols: n = int(n)
y_cols_len = len(y_cols)

# リストの初期化
x = []
y = []
i = 0
while i < y_cols_len:
  y.append([])
  i += 1

# リスト作成
while len(linecache.getline(filepath, c)) != 0:
   row = linecache.getline(filepath, c)
   row = re.split(",", row)
   x.append(c)
   print(row)

   i = 0
   while i < y_cols_len:
     if row[int(y_cols[i])] == "": row[int(y_cols[i])] = 0 # convert blank cell(type string) to num
     y[i].append(float(row[int(y_cols[i])]))
     i += 1
   print(c)
   c += 1

# ラベル指定
plt.xlabel("count")

# 凡例作成
i = 0
while i < y_cols_len:
  plt.plot(x,y[i], label=header_list[int(y_cols[i])])
  i += 1

# plot label
plt.legend()

# plot graph
plt.show()

