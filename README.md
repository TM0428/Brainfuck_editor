# Brainfuck_editor

## 仕様書
```bf
#変数設定
Var a b ...
#変数代入
Set a 2
Set b t
#変数消去
Free a
#四則演算
Inc a
Dec a
Add a b c
Sub a b
Mul a b
Div a b
Mod a b
#入出力
Input a 4
Output a
#比較,if
Com > a b
Com < a b
Com = a b
And a b
Or a b
Not a
if(Com > a b)
...
elif(Com < a b)
...
else
...
Endif

```
## 関数使用方法
### Var
変数の作成。複数を引数として置いておくことが可能。
予約変数として"Res"を追加予定なので、この変数の使用は不許可。
また、初期値は全て0とする。
また、最初の文字に記号'('を置くことを禁止する。
### Set
変数に対して、値を代入する。数字(256未満)、~~または1文字のchar()~~(現状仕様は決めている途中)、別の変数を入れることが可能。
### Free
今のところあまり作る気がない。変数の削除(メモリ使用を減らすため)。
### Inc
引数(変数名)を一つとり、インクリメントを行う。
### Dec
引数(変数名)を一つとり、デクリメントを行う。
### Add
引数(変数名)を複数とり、Resに対して値を保存する。
### Sub
引数(変数名)を二つとり、減算を行う
Resに対して値を保存する。
### Mul
引数(変数名)を二つとり、掛算を行う
Resに対して値を保存する。
### Div
引数(変数名)を二つとり、除算を行う
Resに対して値(int型の割った結果)を保存する。
### Mod
引数(変数名)を二つとり、余りを出力する
Resに対して値を保存する。




関数から出力されるデータを変数に対して
Set a (Add a b c)
の場合、変数aにAdd関数の返り値を与える
Add a b c
の場合、予約変数"Res"に代入される

演算終了時は、必ず改行をすること(仕様)

## メモリ使用方法
変数に対して、保存メモリとキャッシュメモリの2つを用意する
データ保存領域より右側を計算領域とする







