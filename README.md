# テーマ

## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
* ローグライクゲーム

## ゲームの実装
### 共通基本機能
* 背景、主人公と、敵の描画
* 敵を倒すことで、スコアを獲得
* 自身が倒されるまでのスコアを競う
* スコアや倒した敵の数に応じて、ゲームの難易度が上昇する
* スコアや倒した敵の数に応じて、強い攻撃手段を獲得する

### 担当追加機能
* main関数(担当：高橋)
* オブジェクト同士の距離算出関数(担当：高橋)
* フィールド内判定関数(担当：高橋)
* 主人公
* 武器（自動）
* 武器（手動）
* 敵
* 中ボス
* ラスボス
* 音声エフェクトの実装

### メモ

### クラス名
#### 主人公: Hero
##### メソッド・インスタンス
* updateメソッド

#### 武器: Weapon
##### メソッド・インスタンス
* updateメソッド

#### 敵: Enemy
##### メソッド・インスタンス
* updateメソッド
