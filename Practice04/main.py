from Practice04.calculation import mat_scal_mul, mat_mat_mul
import time

alpha = 9
beta = - 13

mat_a = [[2, -5, 5], [1, -4, 9], [5, -1, 3]]
mat_b = [[2, -1, 7], [1, -6, 3], [6, -9, 7]]
mat_c = [[4, -3, 9], [5, -4, 1], [3, -5, 3]]

start_time = time.time()
mat_temp = mat_scal_mul(alpha, mat_a)
mat_temp1 = mat_mat_mul(mat_temp, mat_b)
mat_temp2 = mat_scal_mul(beta, mat_c)
mat_result = mat_temp1 + mat_temp2
print("--- %s seconds ---" % (time.time() - start_time))

# --- 0.0009968280792236328 seconds ---
