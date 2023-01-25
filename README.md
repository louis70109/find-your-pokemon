# 找不到寶可夢？用它來找！

- [中文寶可夢 wiki list](https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89)
  - [參考檔案(python)](https://github.com/louis70109/find-your-pokemon/blob/main/pokemon_crawler.py)
- 寶可夢 API:
  - [JSON](https://play.pokemonshowdown.com/data/pokedex.json)
  - [來源](https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md)
- [招式對應清單](https://pokemon.fantasticmao.cn/pokemon/list)
  - [GitHub 清單](https://github.com/fantasticmao/pokemon-wiki/blob/master/apiDoc/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E7%9B%B8%E5%85%B3%E6%8E%A5%E5%8F%A3.md)

## 加入好友

<a href="https://lin.ee/hEm5lEq"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/zh-Hant.png" alt="加入好友" height="36" border="0"></a>

<img src="https://qr-official.line.me/gs/M_059tnxqg_GW.png">

## 開發環境

- Mac 12.5 (M2)
- Python 3.10
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
sh change_bot_url.sh BOT_TOKEN https://NGROK_URL/webhooks/line
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

## LICENSE

MIT
