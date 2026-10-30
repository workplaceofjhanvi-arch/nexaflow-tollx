# NexaFlow: Pre-Gate AI Spatial Sorting for Barrierless Highway Tolling

NexaFlow is an ultra-low-cost, computer-vision-based smart tolling solution designed to eliminate toll plaza congestion through early spatial vehicle pre-scanning and pre-gate exception sorting.

## Key Features
- **Adjacent-Lane Lock:** Eliminates false reads across neighboring lanes using Computer Vision.
- **Tailgating Prevention:** Detects unsafe vehicle proximity before reaching toll gates.
- **Pre-Gate Sorting:** Automatically routes invalid tags to an outer exception lane using smart LED signaling.

## Setup & Running
1. Install Python 3.9+
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `python src/app.py`