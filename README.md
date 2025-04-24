## 開発したもの 

目的：仮想空間(メタバース)上で音声通話をしながらコミュニケーションができるアプリで、「病気や障がいなどがきっかけで感じる孤独感を軽減したい」という目的でミニマムで開発を進めました。

[紹介記事](https://kimikou-blog.jp/prototypes/vr%e3%82%a2%e3%83%97%e3%83%aa/)

## 利用ツール：Unity、Django、Express、React

 [VR_Interaction_UnityOpenXR(Unity)](https://github.com/NK-kimiya/VR_Interaction_UnityOpenXR)　

 [VR_Interaction_API(Django)](https://github.com/NK-kimiya/VR_Interaction_API)　

 [VR_Interaction_signallingserver(Express)](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　

 [VR_Interaction_WebRTC(React)](https://github.com/NK-kimiya/VR_Interaction_WebRTC)　

 ※下記の方法での実行を試しました。　
 
 Django、Express、Reactはホスティングサービス(RenderやHerokuなど)でホスティングを行い、Unityはビルドし、MetaQuest2に実行ファイルを送信　

---

## 🎛 Reactフロントエンドの機能概要

このReactアプリは、DjangoとExpressのサーバーと連携して動作し、  
ユーザー認証、アバター選択、ビデオチャット機能を提供する**リアルタイム対応のフロントエンドUI**です。

### ✅ 主な機能

#### 🔐 ログイン＆アバター選択（Login.js）

- ユーザー名とパスワードでのログイン／アカウント作成
- パスワードの表示切り替え（チェックボックス）
- アバター画像の選択（番号付きUI）
- Djangoサーバーと通信してアカウント情報を取得

#### 📹 ビデオチャット（VideoChat.js）

- `socket.io` を使ったリアルタイム通信
- `PeerJS` を用いたカメラ＆音声ストリーミングの接続／切断
- ユーザー名の表示と、マルチユーザー接続の対応
- 通信エラー時の再接続処理、UI操作（ミュート・カメラ切替・退出）

---

### 🔧 使用ライブラリ（技術スタック）

- `React`, `socket.io-client`, `peerjs`
- `FontAwesome`（ビデオ・マイクアイコンなどUI向け)

#### クライアント側（React + PeerJS）　

・`Peer` インスタンスを作成し、自分のIDを **シグナリングサーバーに登録**　

・**ICEサーバー（STUN/TURN）** を使って通信経路候補（IP, ポート, NAT状況など）を取得　

・通信相手に自分の接続情報（SDP + ICE候補）を送信　

・シグナリングサーバーで、相手からも同様の情報を受信し、**P2P接続**を確立　

・P2P接続できない場合は **TURNサーバーを通じた通信**に自動切り替え　

・映像・音声ストリームを **直接やり取り（MediaStream）**

### 🔧デプロイ時の注意(APIエンドポイントの切り替え)

#### Login.js

以下のコードの１```https://django-login-yggs.onrender.com```をDjangoプロジェクトをデプロイしたURLに変更してください。　

[Djangoプロジェクト](https://github.com/NK-kimiya/VR_Interaction_API)　

※現在```https://django-login-yggs.onrender.com/api/users/```では、ホスティングされていません。

```
const response = await axios.post('https://django-login-yggs.onrender.com/api/users/', {
                username: name,
                password: password,
                avatart_number: avatar_number
            });
```

#### VideoChat.js 

以下のコード```https://trial-app-comu.onrender.com/```をExpressプロジェクトをデプロイしたURLに変更してください。　

※現在```https://trial-app-comu.onrender.com/```では、ホスティングされていません。
```
const socket = io('https://trial-app-comu.onrender.com/video_chat_socket');
```

[Expressプロジェクト](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　

## WebRTCの実装のための記述　

### VideoChat.js　

ファイルの下記のコードの箇所に、契約したICEサーバーの情報を記載して下さい。　

```
myPeer = new Peer({
                config: {
                    //iceServers: [
                    //{ urls: 'stun:stun.l.google.com:19302' }
                    //]
                    iceServers: [{
                        urls: [""]
                    }, {
                        username: "",
                        credential: "",
                        urls: [
       
                        ]
                    }]
                }
            });
```

開発時に仕様を試すために使用したICEサーバー：[xirsys](https://xirsys.com/)


### 連携プロジェクト

📁[VR_Interaction_API(Django)](https://github.com/NK-kimiya/VR_Interaction_API)　

-Reactでカウントの作成、ログイン処理のAPI　

-VRでユーザーIDを通したログイン処理のAPI　

📁[VR_Interaction_UnityOpenXR(Unity)](https://github.com/NK-kimiya/VR_Interaction_UnityOpenXR)　

-MetaQuest2を使用したVR空間のアバター操作　

📁 [VR_Interaction_signallingserver(Express)](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　　

-ReactプロジェクトでWebRTCを実装する際のシグナリングサーバー
