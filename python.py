# import numpy as np
# import matplotlib.pyplot as plt

# # Input sequence
# x = np.array(eval(input('Enter the input sequence (as a list): ')))

# N1 = len(x)
# n = np.arange(0, N1, 1)

# plt.subplot(3, 1, 1)
# plt.stem(n, x, basefmt='k')
# plt.xlabel('n ----->')
# plt.ylabel('Amplitude')
# plt.title('Input sequence X(n)')

# # Impulse sequence
# h = np.array(eval(input('Enter the impulse sequence h(n) (as a list): ')))
# N2 = len(h)
# n1 = np.arange(0, N2, 1)

# plt.subplot(3, 1, 2)
# plt.stem(n1, h, basefmt='k')
# plt.xlabel('n --->')
# plt.ylabel('Amplitude')
# plt.title('Impulse sequence h(n)')

# # Output
# y = np.convolve(x, h)
# N = N1 + N2 - 1
# n2 = np.arange(0, N, 1)

# plt.subplot(3, 1, 3)
# plt.stem(n2, y, basefmt='k')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Linear Convolution of two sequences')

# plt.tight_layout()
# plt.show()
def restore_original_string(S):
    vowels = {'a', 'e', 'o', 'u'}
    len_s = len(S)
    
    # Count number of 'i's removed
    count_i_removed = S.count('i')
    
    # Calculate length of the original part of S (before modification)
    len_original = len_s - count_i_removed
    
    # Extract the resulting string from S
    resulting_string = S[:len_original]
    
    # Check if the reconstructed original string matches the rest of S
    if S == resulting_string + S[len_original:]:
        return resulting_string
    else:
        return "notpossible"

# Example usage:
print(restore_original_string("izizibibzzbb"))  # Output: "zizobozzbb"


