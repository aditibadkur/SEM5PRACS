def char_count():
  n = int(input("Num of frames: "))
  final = ""
  
  for i in range(n):
      data = input(f"Enter data for frame {i+1}: ")
      count = str(len(data)+1)+data
      final += " "+count
  print("Transmitted msg: "+final)

def bit_stuff():
    msg = list(input("Enter msg: "))
    flag = input("Enter start and end flag: ")
    count = 0
    
    for i in range(len(msg)):
        # if data is 0, move on else keep count 
        if msg[i]=='1':
            count += 1
        # else:
        #     pass
        
        # if count = 5, add 0 and iterate
        if count==5:
            msg.insert(i, '0')
            count = 0
            i+=1
        
    print(msg)
    ans = flag+"".join(msg)+flag
    print(ans)

  
char_count()
bit_stuff()      
# byte um
