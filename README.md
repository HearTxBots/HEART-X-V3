<p align="center">
   <img src="docs/HeartxBots.png" alt="HeartxBots logo" width="420">
</p>

<!-- HEADER -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&weight=700&size=40&duration=4000&pause=500&color=FF4E50&center=true&vCenter=true&width=800&lines=🪩+Heart+X+Bots;⚡+Leech+%26+Mirror+Repo;🚀+Fast+%7C+Reliable+%7C+Ad-Free" />
</p>

<!-- TELEGRAM BUTTON -->
<p align="center">
  <a href="https://t.me/heartxbots">
    <img src="https://img.shields.io/badge/🚀%20JOIN%20OUR%20TELEGRAM%20CHANNEL-ff4e50?style=for-the-badge&logo=telegram&logoColor=white&labelColor=ff758c" />
  </a>
</p>

<!-- DIVIDER -->
<p align="center">
  <img src="https://github.com/rohanreddych/gradient-lines/blob/main/purple-pink.gif?raw=true" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/⚕️%20HEROKU%20SUPPORTED%20REPO-WITHOUT%20SUSPENSION%20OR%20BAN-FFD700?style=for-the-badge&logo=heroku&logoColor=white" alt="Heroku supported" width="600" />
</p>

## Index

<details open>
   <summary>Table of Contents <kbd>Click Here</kbd></summary>

   - [At a Glance](#at-a-glance)
   - [Why Use It](#why-use-it)
   - [What It Covers](#what-it-covers)
   - [How It Runs](#how-it-runs)
   - [Deployment](#deployment)
   - [Configuration](#configuration)
   - [Project Layout](#project-layout)
   - [Documentation](#documentation)
   - [Support](#support)
   - [Credits](#credits)
   - [License](#license)
</details>

## At a Glance

| Area | Details |
|---|---|
| Runtime | Python Telegram bot + web UI |
| Deployment | Docker & Docker Compose |
| Required config | `BOT_TOKEN`, `TELEGRAM_API`, `TELEGRAM_HASH`, `OWNER_ID`, `DATABASE_URL` |
| Port controls | `BASE_URL_PORT`, `RCLONE_SERVE_PORT` |
| License | [LICENSE](LICENSE) |

## Why Use It

HeartxBots is built for users who want a single bot stack that can mirror, leech, manage files, and expose a simple web-based selection flow without stitching together multiple tools. The README focuses on what you need to deploy it quickly, understand the moving parts, and tune the behavior safely.

## What It Covers

| Capability | Outcome |
|---|---|
| Mirroring | Send files to Telegram with a controllable pipeline |
| Leeching | Deliver files in the format you prefer, including document and media workflows |
| File selection UI | Review and select torrent / NZB / upload contents before finalizing |
| Multi-source downloads | Use qBittorrent, Aria2, JDownloader, Mega, NZB, and yt-dlp integrations |
| Storage and upload paths | Push content to Google Drive, Rclone, Mega, and other supported routes |
| Automation | Limit tasks, tune queues, and manage startup updates from one config layer |

## How It Runs

Deploy with Docker and provide the required configuration values. The container takes care of the runtime path, so users only need to build or start the image and set their settings.

<details>
   <summary>What you need <kbd>Click Here</kbd></summary>

   - Docker installed
   - Your Telegram bot token and Telegram API credentials
   - A MongoDB connection string
   - The optional service credentials you want to enable, such as Drive, Rclone, Mega, JDownloader, or SABnzbd
</details>

## Deployment

<details open>
   <summary>Recommended: Docker Compose</summary>

   ```bash
   git clone https://github.com/HearTxBots/HEART-X-V3.git
   cd HEART-X-V3
   docker compose up --build
   ```

   Use this when you want the simplest full deployment path.
</details>

<details>
   <summary>Single Container</summary>

   ```bash
   git clone https://github.com/HearTxBots/HEART-X-V3.git
   cd HEART-X-V3
   docker build -t wzmlx .
   docker run -p 80:80 -p 8080:8080 wzmlx
   ```

   Use this if you want a manual one-container deployment.
</details>

<details>
   <summary>Deployment Notes</summary>

   1. Set `BASE_URL_PORT` and `RCLONE_SERVE_PORT` to match the ports you want to expose.
   2. If you use qBittorrent, tune `AsyncIOThreadsCount` to your machine size.
   3. Stop the container before removing it, and remove the container before pruning images.
   4. Useful cleanup commands:

   ```bash
   sudo docker container prune
   sudo docker image prune -a
   ```
</details>

<details>
   <summary>Legacy Workflow Guide</summary>

   Some users still rely on the external workflow path referenced by the previous README:

   - [WZ Deploy workflow guide](https://github.com/SilentDemonSD/WZ-Deploy/tree/main?tab=readme-ov-file#2%EF%B8%8F%E2%83%A3-method-2-github-workflow-guide)

   Keep this only if that workflow still matches your deployment style.
</details>

## Configuration

Start with the required values:

- `BOT_TOKEN`
- `TELEGRAM_API`
- `TELEGRAM_HASH`
- `OWNER_ID`
- `DATABASE_URL`

Then tune the optional behavior from `config_sample.py`.

<details>
   <summary>Important user-facing settings</summary>

   | Setting | User impact |
   |---|---|
   | `DEFAULT_LANG` | Bot language |
   | `STATUS_LIMIT` | How much status data is shown |
   | `DEFAULT_UPLOAD` | Default upload target |
   | `LEECH_SPLIT_SIZE` | How large leech outputs are split |
   | `QUEUE_ALL`, `QUEUE_DOWNLOAD`, `QUEUE_UPLOAD` | Queue pressure and concurrency |
   | `SHOW_CLOUD_LINK` | Whether cloud links are shown to users |
   | `WEB_PINCODE` | Protects web access to file selection |
   | `UPDATE_PKGS` | Package refresh behavior during startup |
</details>

<details>
   <summary>Integrations available in config</summary>

   The sample config also covers:

   - qBittorrent and Aria2-related controls
   - JDownloader login details
   - Mega credentials
   - SABnzbd server definitions
   - Google Drive settings
   - RSS, search, media metadata, and logging controls
</details>

## Project Layout

| Path | Purpose |
|---|---|
| `bot/` | Bot core, handlers, listeners, and modules |
| `web/` | FastAPI app, templates, and the file selector UI |
| `gen_scripts/` | Setup helpers for sessions, tokens, and drive configuration |
| `plugins/` | Optional bot plugins |
| `qBittorrent/` | Default qBittorrent configuration |
| `sabnzbd/` | Default SABnzbd configuration |

## Documentation

> [!NOTE]
> This documentation is still being expanded.

- Full guides: `docs/`
- Deployment notes: the docs site linked from the repository at WZ Docs
- Configuration reference: `config_sample.py`

## Support

<details>
   <summary>Join Community</summary>

   - Telegram channel: https://t.me/HeartxBots
   - Support group: https://t.me/TgHelpingGroupHeart
</details>

## Credits

HeartxBots is a fork of [WZML-X](https://github.com/SilentDemonSD/WZML-X). The base project belongs to [SilentDemonSD](https://github.com/SilentDemonSD/WZML-X) and upstream contributors.

## License

This project is distributed under the terms of the repository license. See [LICENSE](LICENSE) for the full text.

