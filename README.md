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
- `FontAwesome`（ビデオ・マイクアイコンなどUI向け）

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

### 連携プロジェクト

📁[VR_Interaction_API(Django)](https://github.com/NK-kimiya/VR_Interaction_API)　

-Reactでカウントの作成、ログイン処理のAPI　

-VRでユーザーIDを通したログイン処理のAPI　

📁[VR_Interaction_UnityOpenXR(Unity)](https://github.com/NK-kimiya/VR_Interaction_UnityOpenXR)　

-MetaQuest2を使用したVR空間のアバター操作　

📁 [VR_Interaction_signallingserver(Express)](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　　

-ReactプロジェクトでWebRTCを実装する際のシグナリングサーバー
