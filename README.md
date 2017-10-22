# No Need for Receipt

![title](https://github.com/jphacks/KB_1712/blob/master/presentation/origin.jpeg)

## 製品概要
### Receipt Tech

### 背景（製品開発のきっかけ、課題等）
![background](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.001.jpeg)
学生（や社会人）はお金の余裕がない．自分のお財布の紐をしっかり締め，有意義にお金を使いたい．
現状，人は自分のお金の支出をきちんと管理できていない
家計簿を付けることはできるが，いちいちレシートを貯めてメモしたくない
レシートを自動で認識し，スマートフォンアプリで管理できるシステムを開発

### 製品説明（具体的な製品の説明）
![detail1](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.002.jpeg)
デバイスにレシートを入れると、デバイスが内蔵したカメラからレシートを撮影し、レシートを保管
![detail2](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.003.jpeg)
撮影したレシートの写真から、含まれている情報を取得
![detail3](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.004.jpeg)
取得した情報はデーテベース格納される
![detail4](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.005.jpeg)
得られたデータベースの情報は、企業側や利用者側に関わらず、様々な形で再利用が可能
![detail5](https://github.com/jphacks/KB_1712/blob/master/presentation/nnfr.006.jpeg)
レシートから得られる情報の例

### 特長
#### 1. 不要レシート箱のハック
ユーザが自分で写真を撮ることなく，買い物をして店頭で捨てた瞬間に自分のアプリで管理できる
#### 2. どこでも簡単に設置・利用
レジやポイントカードなどといった店のシステムに組み込まなくても，設置するのみで導入可能
#### 3. レシート情報の可能性
認識したレシートデータを整形し，綺麗なまとまりとして出力しているため，解析，可視化が容易

### 解決出来ること
* ユーザが手間なく自分の総支出を管理し，無駄遣いを防止
* レシートという情報の塊の有効活用

### 今後の展望
* 端末の小型化（RasberryPiとArduinoの統合，RasberryPiZeroW・ArduinoNanoへの置き換え，カメラモジュールの小型化）
* スマートフォンアプリの実装（管理・可視化アプリ）
* 店頭のユーザと受け取ったレシートの紐付け（Beacon，GPS）

## 開発内容・開発技術
### 活用した技術
#### API・データ
* Google Cloud Vision API（レシート画像から文字認識・解析）
* レシートの画像データ(自作)

#### フレームワーク・ライブラリ・モジュール
* OpenCV, Pillow
* Numpy, scikit-learn

#### デバイス
*　RaspberryPi 3
*　rduino UNO
*　サーボモータ
*　DCモータ
*　広角カメラ

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* 機械学習を用いたレシートからの情報分類
* Arduinoを用いたCemara/motorなどの複数のモジュールの制御
