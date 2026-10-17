# Uncovered Food Exposure Duration Monitor
import time

class UncoveredFoodMonitor:
    def __init__(self, max_exposure_seconds=30.0):
        self.max_exposure = max_exposure_seconds
        self.tracked_items = {}

    def track_uncovered_item(self, item_id, box):
        now = time.time()
        if item_id not in self.tracked_items:
            self.tracked_items[item_id] = now
            return False, 0.0
        
        elapsed = now - self.tracked_items[item_id]
        alert_triggered = elapsed >= self.max_exposure
        return alert_triggered, elapsed

if __name__ == "__main__":
    monitor = UncoveredFoodMonitor()
    print("Uncovered Food Exposure Monitor initialized.")
