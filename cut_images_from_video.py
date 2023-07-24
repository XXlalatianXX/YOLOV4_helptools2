import cv2
import os

def extract_frames(video_path, output_folder, frames_per_second):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the frame interval based on the desired frames per second
    frame_interval = int(video.get(cv2.CAP_PROP_FPS) / frames_per_second)

    # Initialize variables
    frame_count = 0
    image_count = 0

    while video.isOpened():
        # Read the current frame
        ret, frame = video.read()

        if not ret:
            break

        # Process frames at the desired frame rate
        if frame_count % frame_interval == 0:
            # Save the frame as an image
            image_path = os.path.join(output_folder, f"frame_{image_count:04d}.jpg")
            cv2.imwrite(image_path, frame)
            image_count += 1

        frame_count += 1

        # Calculate progress percentage
        progress = (frame_count / total_frames) * 100
        print(f"Progress: {progress:.2f}%")

    # Release the video file and close any open windows
    video.release()
    cv2.destroyAllWindows()

    # Print the total number of extracted images
    print(f"Total number of extracted images: {image_count}")


def process_videos(input_folder, output_folder, frames_per_second):
    # Get all .mp4 files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        video_output_folder = os.path.join(output_folder, os.path.splitext(video_file)[0])
        os.makedirs(video_output_folder, exist_ok=True)
        print(f"Processing video: {video_file}")
        extract_frames(video_path, video_output_folder, frames_per_second)

# Example usage
input_folder = "D:/UAV_GRIFFIN/Video_in"
output_folder = "D:/UAV_GRIFFIN/Video_out"
frames_per_second = 1  # Number of frames per second

process_videos(input_folder, output_folder, frames_per_second)