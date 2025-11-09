import cv2
import mediapipe as mp
from gpiozero import LED

# ----- GPIO pin setup -----
led_pins = [17, 27, 22, 23, 24]
leds = [LED(pin) for pin in led_pins]

def show_finger_count(count):
    for i, led in enumerate(leds):
        if i < count:
            led.on()
        else:
            led.off()

# ----- MediaPipe setup -----
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)   # Change to 1 if using external camera
cap.set(3, 640)
cap.set(4, 480)

tip_ids = [4, 8, 12, 16, 20]
print("🖐️ Showing number of fingers on LEDs... Press 'q' to quit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    fingers = 0
    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        lmList = []
        h, w, _ = img.shape

        for id, lm in enumerate(handLms.landmark):
            lmList.append((int(lm.x * w), int(lm.y * h)))

        if lmList:
            # Thumb
            if lmList[tip_ids[0]][0] > lmList[tip_ids[0]-1][0]:
                fingers += 1
            # Other fingers
            for i in range(1, 5):
                if lmList[tip_ids[i]][1] < lmList[tip_ids[i]-2][1]:
                    fingers += 1

        show_finger_count(fingers)
        cv2.putText(img, f"Fingers: {fingers}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    else:
        show_finger_count(0)

    cv2.imshow("Hand Detection - Raspberry Pi", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
show_finger_count(0)
print("🔚 Program ended")
