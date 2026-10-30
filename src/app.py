import time
from pre_scan_camera import PreScanCamera
from vision_pipeline import VisionPipeline
from spatial_sorter import SpatialSorter

def main():
    print("==================================================")
    print("  NexaFlow: Full Toll System Simulation Active    ")
    print("==================================================")
    
    camera = PreScanCamera()
    vision = VisionPipeline()
    sorter = SpatialSorter()
    test_cases = camera.scan_vehicle()
    
    for tc in test_cases:
        print(f"\n[SCAN] Processing Vehicle: {tc['vehicle_number']}")
        print(f"  Description    : {tc['description']}")
        print(f"  FASTag Status  : {tc['fastag_status']} (Balance: ₹{tc['balance_inr']})")
        print(f"  Distance       : {tc['distance_meters']} meters")
        
        # Run vision frame processing
        frame = vision.process_frame()
        print(f"  Vision Status  : Frame processed successfully ({frame.shape[1]}x{frame.shape[0]})")
        
        # Run spatial sorting / tailgating check
        spatial_result = sorter.evaluate_tailgating(tc['distance_meters'], tc['vehicle_number'])
        print(f"  Spatial Check  : {spatial_result['warning']}")
        
        print(f"  Expected Action: {tc['expected_action']}")
        print(f"  Signal LED     : {tc['expected_led']}")
        print("-" * 50)
        time.sleep(1)

    print("\n[INFO] Complete NexaFlow simulation ran successfully!")

if __name__ == "__main__":
    main()