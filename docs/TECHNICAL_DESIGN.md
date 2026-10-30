# NexaFlow Technical Architecture

## System Architecture

```text
 [ Upstream Camera Feed ]          [ Barrierless Toll Plaza ]
           │                                   │
  (ANPR License Plate Scan)             (Overhead RFID Read)
           │                                   │
           ▼                                   ▼
 ┌─────────────────────────────────────────────────────────┐
 │       Raspberry Pi / Edge Laptop (OpenCV + Python)       │
 │   - Binds Plate to FASTag (Creates Digital Twin)        │
 │   - Tracks Distance (Proximity & Tailgate Detection)   │
 └───────────────────────────┬─────────────────────────────┘
                             │
          ┌──────────────────┴──────────────────┐
          ▼                                     ▼
 [ Valid / Sufficient Balance ]         [ Low Balance / Tag Error ]
          │                                     │
  Green Light Signal                    Red Light Signal
 (Barrierless Speed Lane)             (Outer Exception Lane)
 