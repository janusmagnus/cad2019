# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 15:01:58 2015

@author: ACSECKIN

python -m pip install opencv-python
"""

import vrep
import time
import cv2
import numpy as np
from PIL import Image
import array

vrep.simxFinish(-1)

clientID = vrep.simxStart('140.130.17.32', 19999, True, True, 5000, 5)

if clientID!=-1:
    print('Connected to remote API server')
    print('Vision Sensor object handling')
    res, v1 = vrep.simxGetObjectHandle(clientID, 'vs1', vrep.simx_opmode_oneshot_wait)
    print('Getting first image')
    err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v1, 0, vrep.simx_opmode_streaming)
    while (vrep.simxGetConnectionId(clientID) != -1):
        err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v1, 0, vrep.simx_opmode_buffer)
        if err == vrep.simx_return_ok:
            print("image OK!!!")
            # show image
            img = np.array(image,dtype=np.uint8)
            img.resize([resolution[1],resolution[0],3])
            cv2.imshow('image',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        elif err == vrep.simx_return_novalue_flag:
            print("no image yet")
            pass
        else:
          print(err)
else:
  print("Failed to connect to remote API Server")
  vrep.simxFinish(clientID)

cv2.destroyAllWindows()