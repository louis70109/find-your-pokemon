# Can't find Pokemon? Use it to find!!

This is a Python project that can search for Pokemon from the official website and SQLite database. In addition, the project also provides LINE Bot functionality, which can enter `Chinese` || `English` || `Japanese` Pokemon name and return related Flex messages.


## Add LINE Bot friends

<a href="https://lin.ee/hEm5lEq"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/zh-Hant.png" alt="Add friends" height="36" border="0"></a>

### Instructions

- `heal`: Health check
- `top`: Find the most used Pokemon in doubles
- `vgc`: Find team information
- `自爆磁怪` || `ジバコイル` || `Magnezone`: Manually enter the name of the Pokemon you want to find and find its individual value
-  [`屬性`, `type`, `タイプ`]: Attribute restraint table
- `find Magnezone`: Find battle details
- `show`: Pokemon Showdown website
- `show name`: Battle record on Pokemon Showdown

## Operation process

![Operation process](https://raw.githubusercontent.com/louis70109/find-your-pokemon/main/statics/communcation.png)

## Development environment

Before you start using the project, you need to make sure you have installed the following tools and packages:

- Python 3.6 or above
- pip
- LINE 7.13

## How to develop

```sh
mv .env.sample .env // fill the LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET
pip3 install -r requirements.txt
python3 main.py
```

### Environment variables

- API_ENV=develop
  - develop -> reload
- LINE_CHANNEL_ACCESS_TOKEN=
- LINE_CHANNEL_SECRET=
  - LINE Bot Key
- SERIES=gen9vgc2023series1
  - Pokemon season, find the season from [here](https://www.pikalytics.com/pokedex)

## Create temporary https

1. Open the first terminal

```
ngrok http 8080
```

2. Open another terminal

```shell
sh change_bot_url.sh LINE_BOT_TOKEN https://NGROK_URL/webhooks/line
```

## Health check

```shell
curl http://localhost:5000/
```

## Deploy deploy!!

```shell
gcloud run deploy nijia-cloud-run-example-1 --source .
```

## GitHub Actions settings

The following three secrets need to be set in the project:

> Path: Project > Settings > Left side Secrets and Variables > Actions > Repository secrets

- SERVICE_URI: Periodic check season use, GCP || Other deployed Domain + /season
  - e.g. https://example.com/season
- LINE_ADMIN: Who to push to which administrator
- LINE_CHANNEL_ACCESS_TOKEN: Chatbot key

## Want to join development!

Thank you for your interest in participating in our project development!

The following are the steps to participate in development and submit a Pull Request:

### Fork project

Click "Fork" in the upper right corner of the project page to copy this project to your account.

### Clone project

In your GitHub project, click "Clone or download" and copy the URL of the project. Then execute the following command in the terminal:

```
git clone https://github.com/louis70109/find-your-pokemon.git
```

Install the necessary packages in your local environment

```
pip install -r requirements.txt
```

Create a new branch before modifying the code

```
git checkout -b my_new_feature
```

Make modifications in your local development environment

Start editing with your familiar editor or IDE.

### Submit modifications

When you have finished editing and are sure that the modified code is error-free, use the following command to submit your modifications:

```
git add .
git commit -m "Add my feature"
```

### Push branch

Use the following command to push your branch to GitHub:

```
git push origin my-feature
```

### Submit Pull Request

After pushing your branch to your GitHub account, please click "Compare & pull request" on the project page and fill in the necessary information to submit a Pull Request. We will review your modifications as soon as possible and discuss with you if necessary.

Thank you for your contribution! If you have any questions, please feel free to ask them in the Pull Request and I will answer them as soon as possible.

## References

- [Chinese Pokemon wiki list](https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89)
  - [Reference file (python)](https://github.com/louis70109/find-your-pokemon/blob/main/pokemon_crawler.py)
- Pokemon API:
  - [JSON](https://play.pokemonshowdown.com/data/pokedex.json)
  - [Source](https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md)
- [Move correspondence list](https://pokemon.fantasticmao.cn/pokemon/list)
  - [GitHub list](https://github.com/fantasticmao/pokemon-wiki/blob/master/apiDoc/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E7%9B%B8%E5%85%B3%E6%8E%A5%E5%8F%A3.md)
- [Pokemon traditional style photo library](https://play.pokemonshowdown.com/sprites/gen5/)
- [Pokemon GIF from Showdown](https://pkmn.github.io/ps/img/)

## LICENSE

MIT
