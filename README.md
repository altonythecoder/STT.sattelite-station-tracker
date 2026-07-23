# 🛰️ locaSAT: Global LEO Satellite Tracker & Ground Control Station[cite: 7]

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-38bdf8.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A highly responsive, real-time 3D Space Domain Awareness (SDA) platform designed to track Low Earth Orbit (LEO) constellations[cite: 7]. Built with a high-performance Python backend and a WebGL frontend, **locaSAT** visualizes major satellite fleets including Starlink, OneWeb, Iridium NEXT, Planet Labs, and the ISS with 60 FPS smooth interpolation using SGP4 orbital mechanics[cite: 4, 7].


## ✨ Key Features

### 🔭 Advanced Orbital Mechanics & Tracking
* **SGP4 Propagator:** Utilizes the `skyfield` library to calculate high-precision geocentric and topocentric satellite positions[cite: 8, 9].
* **Live TLE Fetching:** Automatically retrieves the latest Two-Line Elements (TLE) from Celestrak for highly accurate telemetry[cite: 9]. Includes built-in fallback TLEs for uninterrupted ISS tracking[cite: 9].
* **Massive Scale:** Capable of rendering over 10,000 active LEO space objects simultaneously, grouping them by operators (SpaceX, OneWeb, Iridium, etc.)[cite: 4, 9].

### 💻 Ground Control Station (GCS) Interface
* **3D WebGL Globe:** Powered by CesiumJS for seamless, hardware-accelerated Earth visualization[cite: 4, 7].
* **Custom Ground Stations:** View satellites relative to major observatories such as DAG (3170m) and TÜBİTAK TUG (2500m), or input manual latitude/longitude coordinates[cite: 4].
* **Live GPS Integration:** Automatically locks the ground station to your current physical location via browser Geolocation API[cite: 4].
* **Glassmorphism UI:** A sleek, modern command panel with a dynamic "Fleet Info Card" displaying operator details, orbital speeds (~27,000 km/s), altitudes, and communication bands[cite: 4].
* **Map Layers:** Switch between Real-Time Satellite Imagery, ESRI Dark, and CartoDB Dark Matter themes[cite: 4].

### ⚡ Real-Time Data Streaming
* **WebSocket Architecture:** Telemetry data is streamed asynchronously from the FastAPI backend to the frontend every 1.0 second[cite: 6].
* **Data Validation:** Strict schema enforcement using Pydantic models for live telemetry and pass predictions (`LiveSatelliteTelemetry`, `PassPrediction`)[cite: 10].

---

## 🏗️ System Architecture & Tech Stack

**Backend:**
* **Language:** Python 3.11[cite: 3]
* **Framework:** FastAPI, Uvicorn[cite: 6, 8]
* **Astrodynamics:** Skyfield (SGP4), NumPy[cite: 7, 8]
* **Data Validation:** Pydantic[cite: 10]

**Frontend:**
* **Core:** HTML5, CSS3, JavaScript (Vanilla)[cite: 4]
* **3D Engine:** CesiumJS (v1.115)[cite: 4]

**DevOps & Deployment:**
* Docker & Docker Compose[cite: 2, 7]
* Environment variable management via `.env`[cite: 1, 9]

---

## 🚀 Installation & Setup

### Prerequisites
* Docker & Docker Compose (Recommended)
* Python 3.11+ (For manual setup)[cite: 3]
* Optional: Spacetrack account credentials for extended API access[cite: 9].

### Method 1: Docker (Recommended)[cite: 7]
The easiest way to run locaSAT is using Docker.

```bash
# 1. Clone the repository[cite: 7]
git clone [https://github.com/altonythecoder/locasat-location.leosat](https://github.com/altonythecoder/locasat-location.leosat)[cite: 7]
cd locasat-location.leosat[cite: 7]

# 2. Build and launch the container[cite: 7]
docker compose up --build[cite: 7]


The application will be accessible at `http://localhost:8000`.

### Method 2: Manual Installation


# 1. Create a virtual environment
python -m venv .venv[cite: 1]
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# 2. Install dependencies
pip install --no-cache-dir -r requirements.txt[cite: 3]

# 3. Start the ASGI Server
uvicorn main:app --host 0.0.0.0 --port 8000[cite: 3]

```
---

## 📡 WebSocket API Reference

locaSAT exposes real-time endpoints for raw telemetry data.

### `WS /ws/orbit/{norad_id}`

Streams highly detailed telemetry for a single satellite relative to the ground station.
Yields (`LiveSatelliteTelemetry`):

```json
{
  "satellite_name": "ISS (ZARYA)",
  "norad_id": 25544,
  "timestamp_utc": "2026-07-23T10:00:00Z",
  "latitude": 51.64,
  "longitude": 120.5,
  "altitude_km": 415.2,
  "azimuth_deg": 145.2,
  "elevation_deg": 45.1,
  "distance_km": 520.4
}

```

### `WS /ws/constellation/{group_name}`

Streams compact coordinate arrays for entire constellations to optimize frontend rendering performance. Supported groups: `starlink`, `oneweb`, `iridium-NEXT`, `planet`, `stations`, `active`.
**Yields:**

```json
[
  [ -120.4532, 45.1234, 550.2, "STARLINK-1234" ],
  [ 45.1234, -12.3456, 549.8, "STARLINK-5678" ]
]

```

---

## ⚙️ Configuration

You can configure the backend by creating a `.env` file in the root directory:

```ini
SPACETRACK_USER=your_email@example.com
SPACETRACK_PASS=your_password
PYTHONUNBUFFERED=1

```

Note: The `.env` file is ignored by git for security purposes.

---

## 📜 License

This project is licensed under the MIT License - Copyright (c) 2026 Altay. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

*Built with 💻 and ☕ for Space Domain Awareness.*


