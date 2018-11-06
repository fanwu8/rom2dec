import numpy as np

def finddec(raw_num):
	raw_num_1 = raw_num[0:len(raw_num)-1]
	raw_num_2 = raw_num[1:len(raw_num)]
	sign_deter = np.less(raw_num_1,raw_num_2)
	signed_arr = np.zeros(len(sign_deter))
	signed_arr[np.where(sign_deter == 1)] = -1
	signed_arr[np.where(sign_deter == 0)] = 1
	#sign_deter[np.where(sign_deter == 0)] = sign_deter[np.where(sign_deter == 0)] + 3 
	raw_num[0:len(raw_num)-1] = raw_num[0:len(raw_num)-1]*(signed_arr)
	return np.sum(raw_num)

