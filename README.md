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
