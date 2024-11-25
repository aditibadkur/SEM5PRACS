import time
import random

ack_frames=0
total=10
window=4
sent_frames=0

while ack_frames<total:  
    for i in range(window): # send frames within window
        if sent_frames<total:
            print(f"Sending frame {sent_frames}")
            sent_frames += 1
            time.sleep(1)
        
    for i in range(window): # check for ACK within window
        if sent_frames<total:
            ack = random.choice([True, False])    
            if ack:
                print(f"ACK {ack_frames} recvd")
                ack_frames+=1
            else:
                print(f"NACK {ack_frames}")
                sent_frames = ack_frames
                break
