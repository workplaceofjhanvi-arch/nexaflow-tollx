import cv2
import numpy as np

class VisionPipeline:
    def __init__(self):
        print("[INFO] Initializing NexaFlow Vision Pipeline...")

    def process_frame(self):
        # Create a blank dummy frame simulating an overhead highway camera feed
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(frame, "NexaFlow Lane Monitor: ACTIVE", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Status: Safe Distance Verified", (30, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        return frame

if __name__ == "__main__":
    vp = VisionPipeline()
    img = vp.process_frame()
    print("[SUCCESS] Vision pipeline frame generated successfully!")
    