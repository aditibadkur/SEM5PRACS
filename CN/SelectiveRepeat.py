import time
import random

ack_frames = 0       
total = 10           
window = 4           
sent_frames = 0      
ack_status = [False] * total 

while ack_frames < total:
    for i in range(window): # send frames within the window & check if ack status == False
        if sent_frames < total and not ack_status[sent_frames]:
            print(f"Sending frame {sent_frames}")
            sent_frames += 1
            time.sleep(1)  
    
 
    for i in range(window):
        if ack_frames < total:
            ack = random.choice([True, False])  
            if ack:
                print(f"ACK {ack_frames} recvd")
                ack_status[ack_frames] = True 
                ack_frames += 1  
            else:
                print(f"NACK {ack_frames}, resending it...")
    time.sleep(1)  
