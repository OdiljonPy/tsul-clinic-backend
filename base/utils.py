import os

from django.core.exceptions import ValidationError


def validate_video_file(file):
    # Get the file extension and validate if it's a video file
    ext = os.path.splitext(file.name)[1]  # Extract the file extension
    valid_video_extensions = ['.mp4', '.mov', '.avi', '.mkv']  # Add more extensions as needed
    if ext.lower() not in valid_video_extensions:
        raise ValidationError('Unsupported file type. Only video files are allowed.')
