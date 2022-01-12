import cv2
import mediapipe as mp


#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        print(result.multi_hand_landmarks)
        if result.multi_hand_landmarks:
            for handlandmark in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS) # 把點連接起來
                


        cv2.imshow('img', img)


    if cv2.waitKey(1) == 27:
        break
