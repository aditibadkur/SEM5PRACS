import time
import random

frames = 10      # Total number of frames
window = 4      # Window size
timeout = 2     # Timeout duration
sleep_time = 1  # Sleep time between actions (in seconds)
sent_frames = 0  # Number of sent frames
current_frame = 0  # Start with frame 0

def send_frame(i):
    print(f"Sending frame {i}")
    time.sleep(sleep_time)  # Sleep time after sending a frame
    
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
                    time.sleep(sleep_time)  # Sleep time after receiving ACK
                    break
                else:  # NACK received
                    print(f"NACK {i} received")
                    print(f"Resending frame {i}...")
                    send_frame(i)
                    time.sleep(sleep_time)  # Sleep time after resending frame
                    break
            else:
                print(f"Timeout exceeded for frame {i}. Resending frame...")
                send_frame(i)
                time.sleep(sleep_time)  # Sleep time after timeout

        # If all frames in the window are ACK'd, shift the window
        if sent_frames % window == 0:
            current_frame = sent_frames

frame_ack()
