# Personal Website

Personal homepage for Ingo Reschke - IT Solution Architect

## Overview

A clean, professional single-page website showcasing professional profile and contact information.

## Features

- Responsive design optimized for all devices
- Professional visit card layout
- Contact information and social links
- German language content

## Structure

```
.
├── index.html          # Main homepage
├── impressum.html      # Legal notice (Impressum)
├── css/               # Stylesheets
├── img/               # Images and assets
└── sport/             # Additional content section
```

## Tech Stack

- HTML5
- CSS3
- Vanilla JavaScript (no frameworks)

## Deployment

Automatisiertes Deployment via GitHub Actions zu Netcup Webhosting (.github/workflows/deploy.yml) per FTPS.

### Benötigte GitHub Repository Secrets:
* `NETCUP_FTP_SERVER`: Netcup FTPS Hostname (z. B. `hostingXXXXXX.a2e12.netcup.net` oder `ingo-reschke.de`)
* `NETCUP_FTP_USERNAME`: Netcup FTP-Benutzername (z. B. `hostingXXXXXX` oder angelegter FTP-Nutzer)
* `NETCUP_FTP_PASSWORD`: Das zugehörige FTP-Passwort
* `NETCUP_SERVER_DIR` *(optional)*: Zielverzeichnis auf dem Server (Standard: `httpdocs/`)

## Local Development

Simply open `index.html` in a web browser, or use a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx serve
```

Then navigate to `http://localhost:8000`

## License

© 2026 Ingo Reschke. All rights reserved.
