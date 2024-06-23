import cv2
import face_recognition
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def encode_faces(images):
    encodings = []
    for image in images:
        encoding = face_recognition.face_encodings(image)
        if len(encoding) > 0:
            encodings.append(encoding[0])
    return encodings

def main():
    # Load and encode images from folders
    front_images = load_images_from_folder("pictures")
    front_encodings = encode_faces(front_images)

    print("Face capture and encoding complete.")
    print("Now recognizing faces...")
    
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Add this line to reduce the buffer size


    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image from webcam. Exiting...")
            break

        print("Frame captured successfully")

        rgb_frame = frame[:, :, ::-1]

        # Encode the captured face
        face_encodings = face_recognition.face_encodings(rgb_frame)

        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]

            # Compare the captured face with images from different positions
            results = face_recognition.compare_faces(front_encodings, face_encoding)
            if True in results:
                print("Front face detected!")
            else:
                print("Face does not match")

        # Display the captured frame
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
