# import numpy as np
# import imageio
# # Load the image
# img = imageio.imread('image.jpg')
# # Calculate U (u), Σ (s) and V (vh)
# u, s, vh = np.linalg.svd(img)
# # Remove sigma values below threshold (250)
# s_cleaned = s
# # Calculate A' = U * Σ (cleaned) * V
# img_denoised = np.array(np.dot(u * s_cleaned, vh), dtype=int)
# # Save the new image
# imageio.imsave('image_denoised.jpg', img_denoised)

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] = [16, 8]


A = imread('image.jpg')
X = np.mean(A, -1); # Convert RGB to grayscale

img = plt.imshow(X)
img.set_cmap('gray')
plt.axis('off')
plt.show()

U, S, VT = np.linalg.svd(X,full_matrices=False)
S = np.diag(S)

j = 0
for r in (1, 5, 10, 30,100,680):
    # Construct approximate image
    Xapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
    plt.figure(j+1)
    j += 1
    img = plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r = ' + str(r))
plt.show()
