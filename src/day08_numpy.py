
import numpy as np

a = np.array([3,4,5])
b = np.array([20,30,40])
print(a+b)

#2d array
a = np.array([[3,4,5],
              [1,2,3]])
b = np.array([20,30,40])
print(a+b)

#3d array
a = np.array([[[3,4,5],[1,2,3],[4,6,8]]])
b = np.array([20,30,40])
print(a+b)

#vectorization
arr=np.random.rand(10)
squared=arr**2
print(squared)

#matrix
arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)

#stacking
x = np.array([[1, 2]])
y = np.array([[3, 4]])
vstacked = np.vstack((x, y))
print(vstacked)

#statistical #mean
data=np.array([[10,20,30],
               [40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))

#TASK--1 THE NORMALIZER
import numpy as np
score=np.array(np.random.randint(50,100,size=(5,3)))
subject_mean=score.mean(axis=0)
centralized_score=score-subject_mean
print(f"original_score\n{score}\ncentralized_score{centralized_score}")

#TASK--2 THE RESHAPER
data=np.arange(24)
reshaped_data=data.reshape(4,3,2)
print(reshaped_data,"\n\n\n")
final_data=reshaped_data.transpose()
print(final_data)




























