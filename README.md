# 🛰️ StarWeb-CARA: Global LEO Satellite Tracker & Ground Control Station

Real-time 3D Space Domain Awareness (SDA) platform tracking Low Earth Orbit (LEO) constellations (Starlink, OneWeb, Iridium NEXT, Planet Labs, ISS) with 60 FPS smooth interpolation using SGP4 orbital mechanics and CesiumJS.

---

## 🚀 Quick Start with Docker

```bash
# Clone the repository
git clone [https://github.com/KULLANICI_ADIN/REPO_ADIN.git](https://github.com/KULLANICI_ADIN/REPO_ADIN.git)
cd REPO_ADIN

# Run with Docker Compose
docker compose up --build

Access the Ground Control Station UI at http://localhost:8000.
```

## 🛠️ Tech Stack & Architecture
```bash
Backend: Python 3.11, FastAPI, WebSockets, Skyfield (SGP4 Orbital Propagator), Pydantic (schemas.py)

Frontend: CesiumJS 3D WebGL Globe, HTML5/CSS3 Glassmorphism UI

DevOps: Docker, Docker Compose
```

## 🛠️ 4. Adım: Git İle GitHub'a Yükleme (Terminal Komutları)

VS Code'un altındaki **PowerShell** terminalinde (`(venv) PS C:\Users\...` yazan yer) sırasıyla şu komutları çalıştır:

### 1. Yerel Depoyu Başlat ve Dosyaları Ekle:
```bash
git init
git add .
git commit -m "feat: initial commit of satellite tracker GCS application"
git branch -M main
```

