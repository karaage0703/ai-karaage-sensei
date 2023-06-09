# ai-karaage-sensei
AI Assistant with ChatGPT API

[日本語のセットアップ記事](https://zenn.dev/karaage0703/articles/ca086022abdd70)

## Dependency
- Ubuntu 22.04
- Python 3.8

## Setup
Install git and curl
```sh
$ sudo apt update
$ sudo apt -y install git
$ sudo apt -y install curl
```

Clone repository and execute setup script
```sh
$ git clone https://github.com/karaage0703/ai-karaage-sensei
$ cd ai-karaage-sensei
$ ./setup.sh
```

Write your open api secret key to `.config` file
```
[open_api_key]
key = your_secret_open_api_key
```

Get icon
```sh
$ git clone https://github.com/karaage0703/karaage_icon
```

Attention!! Check the LICENSE of karaage_icon before you use.


## Usage

```sh
$ python3 ai_karaage_sensei.py
```

## References

- https://zenn.dev/karaage0703/articles/0187d1d1f4d139
- https://note.com/npaka/n/n155e66a263a2
- https://okumuralab.org/~okumura/python/chatgpt_api.html
