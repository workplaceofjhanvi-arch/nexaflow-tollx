import cv2
import json

class PreScanCamera:
    def __init__(self, source=0):
        self.source = source

    def scan_vehicle(self, sample_data_path="data/sample_test_cases.json"):
        """Simulates camera scanning and fetching test case profiles."""
        with open(sample_data_path, "r") as file:
            data = json.load(file)
        return data
    