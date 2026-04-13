def warp_vectorized(img, T):
    h, w = img.shape[:2]

    ys, xs = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')

    xs = xs + 0.5
    ys = ys + 0.5

    ones = np.ones_like(xs)

    coords = np.stack([xs, ys, ones], axis=0).reshape(3, -1)

    T_inv = np.linalg.inv(T)
    src_coords = T_inv @ coords

    xs_src = src_coords[0, :] - 0.5
    ys_src = src_coords[1, :] - 0.5

    xi = np.round(xs_src).astype(int)
    yi = np.round(ys_src).astype(int)

    valid = (
        (xi >= 0) & (xi < img.shape[1]) &
        (yi >= 0) & (yi < img.shape[0])
    )

    result = np.zeros_like(img).reshape(-1, 3)

    result[valid] = img[yi[valid], xi[valid]]

    return result.reshape(h, w, 3)
import time

start = time.time()
res1 = backward_mapping(img, T, img.shape[:2])
t1 = time.time() - start

start = time.time()
res2 = warp_vectorized(img, T)
t2 = time.time() - start

print("Loop time:", t1)
print("Vectorized time:", t2)