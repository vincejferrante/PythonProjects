import io
import os
import requests

from google.cloud import videointelligence


def detect_faces(video_file):
  """Detects faces in a video file and returns a list of face objects."""

  client = videointelligence.VideoIntelligenceServiceClient()

  with io.open(video_file, "rb") as video_file_object:
    requests = [
        videointelligence.types.AnnotateVideoRequest(
            features=videointelligence.types.Feature(face_detection=True),
            video=videointelligence.types.Video(
                input_content=video_file_object.read()))
    ]

    response = client.annotate_videos(requests=requests)

    face_objects = []
    for annotation in response.annotation_results:
      for face_detection in annotation.face_detections:
        face_objects.append(face_detection)

    return face_objects


def place_image_over_face(face_object, image_file):
  """Places an image over a face in a video file."""

  image_data = requests.get(image_file).content
  image = io.BytesIO(image_data)

  width, height = face_object.bounding_box.width, face_object.bounding_box.height

  image = image.resize((width, height))

  return image


def main():
  video_file = "video.mp4"
  image_file = "image.png"

  face_objects = detect_faces(video_file)

  for face_object in face_objects:
    image = place_image_over_face(face_object, image_file)


if __name__ == "__main__":
  main()
