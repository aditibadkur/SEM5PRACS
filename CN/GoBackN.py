import time
import random

frames = 5      # Total number of frames
window = 3      # Window size
timeout = 2     # Timeout duration
sent_frames = 0  # Number of sent frames
current_frame = 0  # Start with frame 0

def send_frame(i):
    print(f"Sending frame {i}")
    
def frame_ack():
    global sent_frames, current_frame, window

    # Sending frames in the current window
    while sent_frames < frames:
        # Send up to the size of the window
        for i in range(current_frame, min(current_frame + window, frames)):
            send_frame(i)

        # Wait for an ACK or NACK for each frame sent
        for i in range(current_frame, min(current_frame + window, frames)):
            t = time.time()
            data = random.choice([True, False])  # Simulate ACK or NACK with random choice
            while time.time() - t < timeout:
                if data:  # ACK received
                    print(f"ACK {i} received")
                    sent_frames += 1
                    current_frame += 1
                    break
                else:  # NACK received
                    print(f"NACK {i} received")
                    print(f"Resending frame {i}...")
                    send_frame(i)
                    break
            else:
                print(f"Timeout exceeded for frame {i}. Resending frame...")
                send_frame(i)
        
        # If all frames in the window are ACK'd, shift the window
        if sent_frames % window == 0:
            current_frame = sent_frames

frame_ack()
