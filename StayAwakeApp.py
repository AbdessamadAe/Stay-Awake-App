import cv2
import mediapipe as mp
import time
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('beep.wav')  # Replace with your sound file

cap = cv2.VideoCapture(0) # 0 is the default camera
drawing_utils = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = drawing_utils.DrawingSpec(thickness=1, circle_radius=1)
pTime = 0
treshold = 0.5

eye_upper_landmarks = [466,398,384,385,386,387,388,161,160,159, 158,157,173,246]
eye_lower_landmarks = [249,382,381,380,374,373,390,163,144, 145, 153,154,155,7]

eye_closed_time = None

opened = False

while True:

    _, frame = cap.read() #The first variable is a boolean variable that returns true if the frame is available. The second variable is the frame that is returned.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert the frame from BGR to RGB
    frame_height, frame_width, _ = frame.shape

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    results = faceMesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            distance = 0
            for upper, lower in zip(eye_upper_landmarks, eye_lower_landmarks):
                upper_point = face_landmarks.landmark[upper]
                lower_point = face_landmarks.landmark[lower]

                frame_height, frame_width = frame.shape[:2]
                upper_point_pixel = (int(upper_point.x * frame_width), int(upper_point.y * frame_height))
                lower_point_pixel = (int(lower_point.x * frame_width), int(lower_point.y * frame_height))

                cv2.circle(frame, upper_point_pixel, 1, (0, 255, 0), -1)  
                cv2.circle(frame, lower_point_pixel, 1, (0, 255, 0), -1)  

                distance += int(upper_point.y*frame_height) - int(lower_point.y*frame_height)

            distance /= 14
            
            if abs(distance) < 4:
                if eye_closed_time is None:
                    eye_closed_time = time.time()
                    
                elif time.time() - eye_closed_time >= treshold:
                    cv2.putText(frame, "Wake Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
                    if not pygame.mixer.get_busy():
                        sound.play()
            else:
                sound.stop()
                eye_closed_time = None
    
    if cv2.getWindowProperty("Virtual Mouse Frame", cv2.WND_PROP_VISIBLE) < 1 and opened == True:  
        break
                
    cv2.imshow("Virtual Mouse Frame", frame)
    opened = True 

    if cv2.waitKey(1) & 0xFF == 27:
        break 

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()