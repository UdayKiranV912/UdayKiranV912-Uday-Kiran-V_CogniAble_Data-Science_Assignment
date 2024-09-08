import os
import torch
import cv2
import numpy as np
from sort import sort

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5 small model

# Initialize the SORT tracker
tracker = sort()

def detect_and_track(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform detection
        results = model(frame)

        # Extract bounding boxes and class labels
        det = []
        for *xyxy, conf, cls in results.xyxy[0]:
            if int(cls) == 0:  # Filter for persons only
                det.append([*xyxy, conf])
        
        det = np.array(det)
        
        # Update the tracker
        tracks = tracker.update(det)
        
        # Draw bounding boxes with IDs
        for track in tracks:
            x1, y1, x2, y2, track_id = track
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame, f'ID {int(track_id)}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Write the frame to the output video
        out.write(frame)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def process_multiple_videos(video_paths, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for video_path in video_paths:
        # Extract video filename
        video_name = os.path.basename(video_path)
        output_path = os.path.join(output_dir, f"output_{video_name}")
        
        print(f"Processing {video_name}...")
        detect_and_track(video_path, output_path)
        print(f"Saved output to {output_path}")

if __name__ == "__main__":
    # List of video paths to process
    video_paths = [
    "test_videos/ABA Autism Training - Chapter 1 - The Discrete Trial.webm",
    "test_videos/ABA Therapy - Learning about Animals.mp4",
    "test_videos/ABA Therapy - Play.webm",
    "test_videos/ABA Therapy - Social Engagement.mp4",
    "Ctest_videos/ABA Therapy： Daniel - Communication.webm",
    "test_videos/Augmentative and Alternative Communication AAC.webm",
    "test_videos/Autism (Moderate - Severe) and ABA - Training Session.webm",
    "test_videos/Discrete Trial Training.mp4",
    "test_videos/Exploring the Therapeutic Playroom.mkv",
    "test_videos/Group Therapy for Autism Spectrum Disorder.webm",
    "test_videos/How to Do Play Therapy ： Building a Growth Mindset Role Play.mp4",
    "test_videos/Incidental Teaching.mkv",
    "test_videos/Jan 5 SonRise Mom part 1.mkv",
    "test_videos/MASS TRIAL (Gross motor imitation).mkv",
    "test_videos/Matching.mkv",
    "test_videos/Natural Environment Teaching (NET).mkv",
    "test_videos/Preference Assessment with Toys： Multiple Stimulus without Replacement (MSWO).webm",
    "est_videos/Sensory Play at Home： Proprioceptive Games.webm",
    "test_videos/Speech Therapy Training Session- Moderate to Severe Autism.webm"
    
    ]
    
    # Directory to save output videos
    output_dir = 'output_videos'
    
    # Process all videos
    process_multiple_videos(video_paths, output_dir)
