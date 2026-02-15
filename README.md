<div align="center">

<img src="https://i.postimg.cc/fR6G47Wp/r-generator-cover.jpg" alt="R-Generator Banner" width="100%"/>

<br/>
<br/>

# R-Generator

### Roblox Account Generation & Engagement on Autopilot

*Generate accounts. Automate favorites. Grow your presence — hands-free.*

<br/>

[How It Works](#-how-it-works) · [Key Features](#-key-features) · [What You Get](#-what-you-get) · [Get Started](#-get-started)

<br/>

---

</div>

<br/>

## About

**R-Generator** is a desktop automation tool with a sleek dark-mode GUI that handles [Roblox](https://roblox.com) account generation and automated catalog/game favoriting.

You configure the parameters. The bot creates accounts, solves captchas, and favorites items. You scale your presence while you sleep.

<br/>

## How It Works

```
You configure generation settings via the GUI
        ↓
Bot launches a headless Chromium browser
        ↓
Accounts are created with random credentials
        ↓
Captchas are auto-solved via integrated extension
        ↓
Cookies are saved for each generated account
        ↓
Favorite bot uses stored cookies to like items
        ↓
Repeat — with smart delays and batch limits
```

Everything is managed through a modern **desktop GUI**. Click a button — the bot does the rest.

<br/>

## Key Features

| | Feature | Description |
|---|---|---|
| **Gen** | Account Creation | Automatically generates Roblox accounts with random credentials |
| **AI** | Captcha Solving | Integrated Capsolver extension handles reCAPTCHA, hCaptcha, FunCaptcha & more |
| **Bot** | Catalog Favorites | Bulk-favorite clothing items across multiple accounts |
| **Bot** | Game Favorites | Bulk-favorite games across multiple accounts |
| **Auto** | Batch Generation | Configurable auto-generation with cooldowns and batch limits |
| **GUI** | Dark-Mode Interface | Clean CustomTkinter dashboard with real-time status updates |
| **Safety** | Smart Pacing | Randomized delays between actions to mimic human behavior |
| **Logs** | Debug Logging | Full activity logging to `debug.log` for transparency |

<br/>

## What You Get

- **Hands-free account generation** — create accounts in batches while AFK
- **Automated favoriting** — boost catalog items and games with stored accounts
- **Auto-generation mode** — set batch limits and cooldowns, let it run
- **Captcha bypass** — integrated solver handles all major captcha providers
- **Cookie persistence** — accounts saved as JSON for reuse across sessions
- **Real-time feedback** — live status updates and account count in the GUI

<br/>

## GUI Controls

| Control | What It Does |
|---|---|
| **Account Generator** | Create new Roblox accounts one at a time |
| **Delay Configurator** | Set auto-generation mode, cooldown, and batch limits |
| **Favorite Bot** | Enter a catalog item ID and account limit to bulk-favorite |
| **Game Favorite** | Enter a game ID and account limit to bulk-favorite |

<br/>

## Under the Hood

| Component | Technology |
|---|---|
| GUI Framework | CustomTkinter |
| Browser Automation | DrissionPage (Chromium) |
| Captcha Solving | Capsolver Extension (Manifest V3) |
| Data Generation | Faker |
| Data Storage | JSON cookie files |
| Language | Python 3.x |

<br/>

## Project Structure

```
r-generator/
├── main.py                 # GUI application
├── generate_accounts.py    # Account creation logic
├── favorite_bot.py         # Favoriting automation
├── accounts/               # Stored account cookies (JSON)
├── assets/fonts/           # Custom Roboto fonts for UI
└── extenstion/capsolver/   # Captcha solver Chrome extension
```

<br/>

## Get Started

1. Install dependencies:
   ```bash
   pip install customtkinter drissionpage faker
   ```

2. Run the application:
   ```bash
   python main.py
   ```

<br/>
