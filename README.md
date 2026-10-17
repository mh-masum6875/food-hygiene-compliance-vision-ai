# Food Hygiene Compliance and Kitchen Safety Vision

[![HACCP](https://img.shields.io/badge/Compliance-HACCP%20%26%20Food%20Safety-brightgreen)](https://github.com/mh-masum6875/food-hygiene-compliance-vision-ai)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![Ultralytics](https://img.shields.io/badge/YOLO-Ultralytics-00FFFF)](https://ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated computer vision audit system engineered for commercial kitchens, Quick Service Restaurants (QSR), and food processing plants to ensure strict sanitary and food safety compliance.

---

## Core Capabilities

### 1. Kitchen Headwear & Hairnet Compliance (`kitchen_headwear_detector.py`)
- Multi-class model (`Person`, `Hairnet`, `No Hairnet`) checking headwear compliance in food preparation areas.
- **Geometric Alignment**: Verifies that headwear centers lie within the upper 40% of the worker bounding box with horizontal tolerance.
- Temporal persistence: 100-frame trust buffer to prevent false alarms caused by head turning.

### 2. 20-Second Handwashing Station Verification (`handwash_station_timer.py`)
- Tracks basin zone occupancy ensuring kitchen workers complete the mandatory **20-second hand hygiene cycle**.
- Renders real-time visual progress HUD on active workers with compliance timestamps.

### 3. Exposed / Uncovered Food Exposure Monitor (`uncovered_food_monitor.py`)
- Spatial detector identifying covered vs uncovered food containers and utensils.
- Time-decay tracking: Automatically triggers sanitation alerts when food is left exposed for more than 30 seconds.

### 4. Sanitation & Floor Mopping Detection (`sanitation_mopping_detector.py`)
- Open-vocabulary cross-object interaction engine: correlates cleaning apparatus (broom, mop, brush, scrubber) with floor regions to verify facility sanitation schedules.

### 5. Food Processing Poultry Conveyor Counter (`poultry_conveyor_counter.py`)
- Class-agnostic tracking counting food units on processing conveyor lines with automated throughput reporting.

---

## Quickstart

```bash
git clone https://github.com/mh-masum6875/food-hygiene-compliance-vision-ai.git
cd food-hygiene-compliance-vision-ai
pip install -r requirements.txt

# Run Hairnet Compliance Detector
python src/kitchen_headwear_detector.py --source kitchen_feed.mp4

# Run 20s Handwash Station Auditor
python src/handwash_station_timer.py --source basin_feed.mp4
```

---

## License
This project is licensed under the MIT License.
