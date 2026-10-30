class SpatialSorter:
    def __init__(self, safe_distance_threshold=1.5):
        self.safe_distance_threshold = safe_distance_threshold

    def evaluate_tailgating(self, distance_meters, vehicle_number):
        """Evaluates if a vehicle is too close, indicating a tailgating risk."""
        if distance_meters < self.safe_distance_threshold:
            return {
                "vehicle": vehicle_number,
                "tailgating_detected": True,
                "warning": "TAILGATE_ALERT: Distance below safe threshold!"
            }
        return {
            "vehicle": vehicle_number,
            "tailgating_detected": False,
            "warning": "SAFE"
        }

if __name__ == "__main__":
    sorter = SpatialSorter()
    print(sorter.evaluate_tailgating(0.8, "HR26DK9999"))