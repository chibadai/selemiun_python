import os # osモジュールのインポート
# os.listdir('パス')
# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
files = os.listdir(os.getcwd())
movieNameArray = []
for file in files:
    print(file)
    print(file[0:len(file)-4])
    if(file[-4:] == '.mp4'):
        print(file)
        movieNameArray.append(file[0:len(file)-4])
