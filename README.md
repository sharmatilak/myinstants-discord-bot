# 🎵 MyInstants Discord Bot

A Discord bot built with **discord.py** that lets you search **MyInstants** directly from Discord using slash command autocomplete and instantly share sound effects with a single command.

Simply type `/instants`, start typing the name of a sound, choose one of the live search results, and the bot will download and upload the selected sound as an audio attachment.

---

## ✨ Features

- 🔍 Live MyInstants search
- ⚡ Discord slash command autocomplete
- 🎵 Downloads and uploads sounds directly to Discord
- 👤 Optional user mention support
- 🌐 User Install compatible
- 🚀 Fully asynchronous using `aiohttp`
- 🧠 Per-user autocomplete cache to prevent conflicts between users

---

## 📸 Example

```text
/instants sound: vine boom
```

Discord displays live autocomplete suggestions while you type.

Selecting a result downloads the corresponding sound from MyInstants and uploads it directly into the chat.

---

## 🛠 Technologies Used

- Python 3.11+
- discord.py
- aiohttp
- parsel
- requests
- requests-toolbelt
- python-dotenv
- user_agent

---

## 📁 Project Structure

```
.
├── myinstants.py        # MyInstants scraper
├── myinstantsbot.py     # Discord bot
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/sharmatilak/myinstants-discord-bot.git

cd myinstants-discord-bot
```

Create a virtual environment.

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root.

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

---

## ▶ Running the Bot

```bash
python myinstantsbot.py
```

If everything is configured correctly, you'll see:

```text
Logged in as MyInstantsBot
Synced 1 commands.
```

---

## 📖 Usage

Run the slash command:

```text
/instants
```

Start typing the sound name.

Example:

```text
/instants sound: rick roll
```

Choose one of the autocomplete suggestions.

The bot will automatically download the selected sound and upload it to the current Discord channel.

---

## ⚙ How It Works

1. User runs `/instants`.
2. Discord requests autocomplete suggestions.
3. The bot searches MyInstants in real time.
4. Search results are cached for the current user.
5. The selected sound is downloaded.
6. The bot uploads the audio directly to Discord.

---

## 📦 Dependencies

- discord.py
- aiohttp
- parsel
- requests
- requests-toolbelt
- python-dotenv
- user_agent

---

## ⚠ Notes

- This project searches and retrieves sounds from **MyInstants**.
- Some cloud hosting providers may experience Cloudflare rate limiting because of shared IP addresses.
- Running the bot on a VPS or your own machine generally provides the best reliability.

---

## 🙏 Acknowledgements

Special thanks to **heylouiz** for the original `myinstants.py` implementation that powers the MyInstants search functionality.

GitHub: https://github.com/heylouiz

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are always welcome.

Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
