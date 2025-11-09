# Real-Time Hand Gesture Controlled LEDs using Raspberry Pi, OpenCV & MediaPipe

This project detects raised fingers from a live camera feed using MediaPipe and controls LEDs on the Raspberry Pi accordingly. Each raised finger lights one LED, demonstrating gesture-based hardware interaction.

---

## 🖥️ Language Used
**Python 3**

---

## 🧰 Requirements
Install required libraries:

---

## 🔧 Hardware Setup
| LED Number | GPIO Pin |
|-----------|----------|
| LED 1     | 17       |
| LED 2     | 27       |
| LED 3     | 22       |
| LED 4     | 23       |
| LED 5     | 24       |

Each LED cathode → 220Ω resistor → GND.

---

## ▶️ Running the Program

Press **'q'** to quit the program.

---

## ✅ Result
The number of raised fingers determines how many LEDs turn ON in real-time, showing interaction between computer vision and physical GPIO control.
