import cv2

import mediapipe as mp

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.6)
fingers_raised = 0
sign_language_letter = ""

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    
    frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    hand_results = hands.process(rgb_frame)
    cv2.putText(frame, f"Letter: {sign_language_letter}", (25,100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1)
    fingers_raised = 0
    sign_language_letter = ""
    # if there are any hand landmarks (meaning there are visible hands)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in (hand_results.multi_hand_landmarks):
            hl = hand_landmarks.landmark
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_tips = [hand_landmarks.landmark[8], hand_landmarks.landmark[12], hand_landmarks.landmark[16], hand_landmarks.landmark[20]]  # index and middle
            finger_base = hand_landmarks.landmark[6]  # bottom of index
            if hl[4].x > hl[10].x:
                if hl[4].y < hl[5].y:
                    sign_language_letter = "T"
                else:
                    sign_language_letter = "S"
            # if the thumb tip is higher than the index middle point
            if hand_landmarks.landmark[4].y < hand_landmarks.landmark[6].y:
                sign_language_letter = "A"
            if hand_landmarks.landmark[17].x - hand_landmarks.landmark[13].x > 0:  # if my hand orientation is rotated to match C
                if hl[4].y - hl[8].y < 0.05:
                    sign_language_letter = "O"
                else:
                    sign_language_letter = "C"
            if hl[5].x > hl[2].x: # if my orientation is flipped so my index x is greater than my thumb x
                if hl[12].x > hl[6].x: # if i have two fingers out while in this orientation
                    sign_language_letter = "H"
                else: # if only one finger out
                    sign_language_letter = "G"

            for finger in finger_tips:
                if finger.y < finger_base.y:
                    fingers_raised += 1
                if fingers_raised > len(finger_tips): # resets fingers raised
                    fingers_raised = 0
                # if we are holding up 4 fingers AND thumb tip is inside index root
                if fingers_raised == 4 and hl[4].x < hl[5].x:
                    sign_language_letter = "B"
                if hl[12].y > hl[11].y and hl[4].x < hl[5].x:
                    sign_language_letter = "E"
                if fingers_raised == 1 and hl[4].x < hl[5].x:
                    sign_language_letter = 'D'
                if fingers_raised == 2 and hl[4].x > hl[12].x:
                    if hl[4].y < hl[5].y:
                        sign_language_letter = "K"
                    else:
                        sign_language_letter = "V"
                if fingers_raised == 2 and abs(hl[8].x - hl[12].x) < 0.01:
                    sign_language_letter = "R"
                if fingers_raised == 1 and hl[4].x > hl[2].x:
                    sign_language_letter = "L"
                if fingers_raised == 1 and hl[20].y < hl[8].y:
                    if hl[20].x > hl[7].x:
                        sign_language_letter = "J"
                    else:
                        sign_language_letter = "I"
                if fingers_raised == 3:
                    if hl[20].y > hl[8].y:
                        sign_language_letter = "W"
                    else:
                        sign_language_letter = "F"
                if fingers_raised == 0 and hl[3].x < hl[5].x:
                    if hl[4].y < hl[10].y and hl[4].x < hl[11].x:
                        sign_language_letter = "N"
                    else:
                        sign_language_letter = "M"
                if fingers_raised == 2 and hl[8].x - hl[12].x < 0.03:
                    sign_language_letter = "U"
                if fingers_raised == 1 and hl[17].x > hl[5].x:
                    sign_language_letter = "X"
            if hl[0].y < hl[9].y:
                if hl[12].y > hl[4].y:
                    sign_language_letter = "P"
                else:
                    sign_language_letter = "Q"
            if hl[20].y < hl[12].y and hl[4].y < hl[12].y:
                sign_language_letter = "Y"
            

    cv2.imshow('Camera Feed with Face and Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

