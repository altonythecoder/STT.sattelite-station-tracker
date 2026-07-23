# main.py
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sat_tracker import SatelliteTracker, ConstellationTracker

app = FastAPI(title="Global LEO Satellite Tracker GCS", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.websocket("/ws/orbit/{norad_id}")
async def websocket_single_orbit(websocket: WebSocket, norad_id: int):
    await websocket.accept()
    tracker = SatelliteTracker(norad_id)
    try:
        while True:
            telemetry = tracker.get_current_telemetry()
            await websocket.send_json(telemetry)
            await asyncio.sleep(0.8)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"WS Single Error: {e}")

@app.websocket("/ws/constellation/{group_name}")
async def websocket_constellation(websocket: WebSocket, group_name: str):
    await websocket.accept()
    tracker = ConstellationTracker(group_name)
    try:
        while True:
            telemetries = tracker.get_compact_telemetries()
            await websocket.send_json(telemetries)
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"WS Constellation Error: {e}")
