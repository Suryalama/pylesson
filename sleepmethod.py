# sleep method is used to stop execution
# it belongs to time module

import time
for i in range(20):

    print(i)
    
    if(i==10):
        time.sleep(5) # stopping execution for 5 seconds
