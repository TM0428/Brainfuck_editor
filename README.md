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
関数から出力されるデータを変数に対して
Set a (Add a b c)
の場合、変数aにAdd関数の返り値を与える
Add a b c
の場合、予約変数"Res"に代入される

演算終了時は、必ず改行をすること(仕様)

## メモリ使用方法
変数に対して、保存メモリとキャッシュメモリの2つを用意する
データ保存領域より右側を計算領域とする







