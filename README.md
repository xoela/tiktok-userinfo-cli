# TikTok Username Lookup

Terminal based tool to look up TikTok user profiles - displays user info and raw JSON in a clean terminal interface.
I saw someone selling the source code to the exact same tool so I decided to make it myself and release it for free :p
![Python](https://img.shields.io/badge/Python-3.x-blue)

## Features

- Clean terminal UI with colored output
- User info summary (nickname, bio, country, language, avatar, stats)
- Full raw JSON response view
- Handles `@` prefix automatically

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Enter a TikTok username when prompted. Press `Enter` to search again or `Ctrl+C` to exit.

## Preview

```
  ╔═══════════════════════════════════════╗
  ║         TikTok Username Lookup        ║
  ╚═══════════════════════════════════════╝

  User Info:

    Nickname    zex
    Username    @zex
    Country     Germany
    Followers   123,456,789
    ...

  JSON:

  { full raw API response }
```
