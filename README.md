# 找不到寶可夢？用它來找！

這是一個 Python 專案，可以從官方網站和 SQLite 資料庫中尋找寶可夢。此外，該專案還提供了 LINE Bot 的功能，可以輸入`中文寶可夢名稱`並回傳相關的 Flex 訊息。

- [中文寶可夢 wiki list](https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89)
  - [參考檔案(python)](https://github.com/louis70109/find-your-pokemon/blob/main/pokemon_crawler.py)
- 寶可夢 API:
  - [JSON](https://play.pokemonshowdown.com/data/pokedex.json)
  - [來源](https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md)
- [招式對應清單](https://pokemon.fantasticmao.cn/pokemon/list)
  - [GitHub 清單](https://github.com/fantasticmao/pokemon-wiki/blob/master/apiDoc/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E7%9B%B8%E5%85%B3%E6%8E%A5%E5%8F%A3.md)

## 加入好友

<a href="https://lin.ee/hEm5lEq"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/zh-Hant.png" alt="加入好友" height="36" border="0"></a>

## 操作流程

[操作流程](https://raw.githubusercontent.com/louis70109/find-your-pokemon/main/bot-flow.png)

## 開發環境

在開始使用專案之前，需要確認您已經安裝了以下工具和套件:

- Python 3.6 或以上版本
- pip
- LINE 7.13

## 如何開發

```sh
mv .env.sample .env // fill the LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET
pip3 install -r requirements.txt
python3 main.py
```

### 環境變數

- API_ENV=develop
  - develop -> reload
- LINE_CHANNEL_ACCESS_TOKEN=
- LINE_CHANNEL_SECRET=
  - LINE Bot Key
- SERIES=gen9vgc2023series1
  - 寶可夢賽季，從[這邊找賽季](https://www.pikalytics.com/pokedex)

## 建立暫時的 https

1. 開第一個終端機

```
ngrok http 8080
```

2. 開另一個終端機

```shell
sh change_bot_url.sh LINE_BOT_TOKEN https://NGROK_URL/webhooks/line
```

## 健康檢查

```shell
curl http://localhost:5000/
```

## 部署部署！！

```shell
gcloud run deploy nijia-cloud-run-example-1 --source .
```

## 想做還不知道怎麼做

- [ ] [引入計算機 LIFF](https://github.com/smogon/damage-calc)

## 想加入開發！

感謝您有興趣參與我們的專案開發！

以下是參與開發並提交 Pull Request 的步驟：

### Fork 專案

在專案頁面右上角點擊「Fork」，即可將本專案複製到您的帳戶下。

### Clone 專案

在您的 GitHub 下的專案中，點擊「Clone or download」並複製該專案的 URL。然後在終端機中執行以下命令：

```
git clone https://github.com/louis70109/find-your-pokemon.git
```

在您的本地環境中安裝必要的套件

```
pip install -r requirements.txt
```

在修改程式碼之前，創建一個新的分支

```
git checkout -b my_new_feature
```

在您的本地開發環境中進行修改

使用您熟悉的編輯器或 IDE 開始編輯。

### 提交修改

當您完成編輯並且確信修改代碼無誤後，使用以下命令提交您的修改：

```
git add .
git commit -m "Add my feature"
```

### 推送分支

使用以下命令將您的分支推送到 GitHub 上：

```
git push origin my-feature
```

### 提交 Pull Request

當您的分支推送到您的 GitHub 帳戶後，請在專案頁面中點擊「Compare & pull request」，然後填寫必要的訊息以提交 Pull Request。我們會盡快審核您的修改，並在必要時與您進行討論。

感謝您的貢獻！如果您有任何問題，請隨時在 Pull Request 中進行提問，我將盡快回答您的問題。

## LICENSE

MIT
