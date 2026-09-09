# SteveBot 🤖

A lightweight, automated Discord bot deployment system backed by a continuous deployment pipeline (CI/CD) hosted on a self-managed Ubuntu environment.

---

## Overview

SteveBot is designed to demonstrate automated deployment practices for modern Python applications. Instead of requiring manual updates or SSH access every time code changes, this repository leverages **GitHub Webhooks**, a **Cloudflare Tunnel**, and a custom **systemd service architecture** to deliver instant, automated redeployments directly from git pushes.

---

## Features & Architecture

* **Automated CI/CD Pipeline:** Pushing code triggers a GitHub Webhook payload that automatically notifies the server to pull updates and restart the service.
* **Secure Reverse Proxying:** Utilizes a Cloudflare Tunnel to handle ingress traffic securely without exposing home network ports to the public internet.
* **Process Management:** Managed by Linux `systemd` daemons, ensuring high availability, automatic startup on boot, and background process isolation.
* **Decoupled Architecture:** Clean separation between the listener layer (`webhook`), secure tunneling layer (`cloudflared`), and execution scripts (`post-receive`).

---

## System Architecture Flow

```
[ PyCharm / Local Machine ]
           │
           │  git push origin main
           ▼
    [ GitHub Repo ]
           │
           │  HTTP POST (Webhook Payload)
           ▼
  [ Cloudflare Tunnel ]
           │
           │  Forwarded Traffic
           ▼
[ Ubuntu Server (webhook.service) ]
           │
           │  Triggers Executable Script
           ▼
   [ ./post-receive Script ]
           │
           ├── git pull origin main
           └── systemctl restart stevebot.service
```

---

## Technical Stack

* **Language:** Python
* **Host Environment:** Ubuntu Linux Server
* **Process Orchestration:** systemd
* **Network & Ingress:** Cloudflare Tunnels (`cloudflared`), Linux Webhook Engine (`webhook`)
* **Version Control & CI/CD:** Git, GitHub Webhooks

---

## Local Setup & Installation

If you wish to test or run the bot locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/SteveBot.git
   cd SteveBot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

5. **Run the bot:**
   ```bash
   python bot.py
   ```

---

## Deployment & Production Infrastructure

For reference, the production instance runs on a dedicated Ubuntu Linux host with the following configuration highlights:

### System Services
* **`webhook.service`**: Listens on local port `9000` for payload signatures from GitHub and invokes system scripts upon validation.
* **`cloudflared.service`**: Encrypts and proxies external webhook notifications through Cloudflare infrastructure back to the local network.

### Deployment Hook (`post-receive`)
Upon receiving a valid webhook request, the server executes an internal script:
```bash
#!/bin/bash
cd /home/chase/SteveBot
git pull origin main
# Automated service restart / environment re-activation
```

---

## Author

* **Chase Hildebrand** — Computer Science @ Penn State University
* **Portfolio:** [chasehildebrand.dev](https://chasehildebrand.dev)
