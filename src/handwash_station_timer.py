# 20-Second Handwashing Station Hygiene Monitor
class HandwashStationTimer:
    def __init__(self, basin_poly, target_duration_sec=20.0):
        self.basin_poly = basin_poly
        self.target_duration = target_duration_sec
        self.worker_timers = {}

    def update_worker(self, worker_id, is_in_basin_zone, fps=30):
        if is_in_basin_zone:
            self.worker_timers[worker_id] = self.worker_timers.get(worker_id, 0) + (1.0 / fps)
            progress = min(1.0, self.worker_timers[worker_id] / self.target_duration)
            is_compliant = self.worker_timers[worker_id] >= self.target_duration
            return progress, is_compliant
        else:
            self.worker_timers[worker_id] = 0
            return 0.0, False

if __name__ == "__main__":
    timer = HandwashStationTimer(basin_poly=[(100, 100), (300, 100), (300, 300), (100, 300)])
    print("Handwash Station Timer initialized.")
