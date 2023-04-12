import struct

from render import render_template_image, render_template_labels
from plot import render
from conversions import *
from bank_template import bank_template
height=1536
width=1536
input_filename = "PC_Generic_1280.bnk.template"
output_filename = "PC_Generic_1280.bnk"

def main(filename):
    dash_objects = []

    with open(filename, "rb") as f:
        f.seek(0x8)  # seek to the start of the first string
        for i in range(22):
            string_bytes = f.read(0x40)  # read 64 bytes (0x40) for each string
            string = string_bytes.decode("iso-8859-1").rstrip()  # decode the bytes and remove null bytes
            print(f"String {i+1}: {string}")
            
    with open(filename, "rb") as f:
        f.seek(0x8 + 0x40 * 22)  # seek to the start of the data
        while True:
            bytes = f.read(4 + 8 * 4)  # read one integer and eight floats
            if not bytes:  # stop reading if there are no more bytes
                break
            data = struct.unpack("<i8f", bytes)  # unpack the bytes as a little-endian integer and eight little-endian floats
            if data[0] == 3:
                print(data)
                dash_objects.append(data)
    
    render(dash_objects)
    render_template_image(dash_objects, width, height)
    render_template_labels(dash_objects, width, height)
    #print("===========converted: \n")
    #for i in range(len(dash_objects)):
    #    print(convert_to_4(dash_objects[i]))
        

def write_bank():
    # Read the input file and modify the data as needed
    with open(input_filename, "rb") as input_file:
        with open(output_filename, "wb") as output_file:
            # Read the string data
            #input_file.seek(0x8)
            string_data = input_file.read(0x8 + 0x40 * 22)
            output_file.write(string_data)

            # Modify and write the data
            input_file.seek(0x8 + 0x40 * 22)
            iter=0
            while True:
                bytes = input_file.read(4 + 8 * 4)
                if not bytes:
                    break
                data = struct.unpack("<i8f", bytes)
                if data[0] == 3:
                    converted=convert_to_8(bank_template[iter])
                    data = (converted[0], converted[1], converted[2], converted[3] , converted[4],
                            converted[5], converted[6], converted[7] , converted[8])
                    iter += 1
                output_file.write(struct.pack("<i8f", *data))
        
if __name__ == "__main__":
    write_bank()
    main(output_filename)
    