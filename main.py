image = load_image(file_path)
clean_image = median(arr_image, ball(3))
edge_detection(clean_image)

threshold = 90
binary_image = edged_image > threshold
binary_image = binary_image.astype(np.uint8) * 255
edge_image = Image.fromarray(binary_image)
edge_image.save('my_edges.png')
