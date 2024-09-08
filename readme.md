# Person Detection and Tracking Pipeline

## Overview

This project aims to develop a person detection and tracking system for identifying children with Autism Spectrum Disorder (ASD) and therapists in a video. The system will assign unique IDs to individuals, track them throughout the video, and handle re-entries, occlusions, and partial visibility.

## Features

- **Person Detection**: Detect children and adults in video frames.
- **Tracking**: Track individuals across frames and assign unique IDs.
- **Re-entries Handling**: Recognize and track individuals who leave and re-enter the frame.
- **Post-Occlusion Tracking**: Maintain correct IDs even after occlusions or partial visibility.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- TensorFlow or PyTorch (depending on the model used)
- `sort` module (or any other tracking algorithm)

Trained Model: https://drive.google.com/file/d/1Wl433OaO-DyXQp2ae9gr6CeFAFXmOnm7/view?usp=drive_link
Output Video: https://drive.google.com/file/d/1X8vWkwHvitnNzKCgLc-ceCpM22n9YTlf/view?usp=drive_link


