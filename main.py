import numpy as np
from PIL import Image

# 1. Encoding
msg = "Hi mr ibrahem im ayed eid and sabreen shalafeh"
delimiter = "@@@@"
message = msg + delimiter
binary_msg = "".join(format(ord(c), "08b") for c in message)

img = Image.open("input.jbg.png").convert("RGB")
data = np.array(img)
flat_data = data.flatten()

for i in range(len(binary_msg)):
    flat_data[i] = (flat_data[i] & 254) | int(binary_msg[i])

encoded_img = flat_data.reshape(data.shape)
Image.fromarray(encoded_img.astype("uint8")).save("output.png")

# 2. Decoding
decoded_img = Image.open("output.png")
flat_decoded = np.array(decoded_img).flatten()

bits = ""
extracted_text = ""
for i in range(len(flat_decoded)):
    bits += str(flat_decoded[i] & 1)
    if len(bits) == 8:
        char = chr(int(bits, 2))
        extracted_text += char
        bits = ""
        if delimiter in extracted_text:
            print(extracted_text.replace(delimiter, ""))
            break