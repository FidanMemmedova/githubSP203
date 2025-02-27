from PIL import Image
import sys


ASCII_CHARS = "@%#*+=-:. "[::-1]

def image_to_ascii(image_path, new_width=100):
    try:
       
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)  
    image = image.resize((new_width, new_height))
    
    
    image = image.convert("L")
    
    
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS) - 1))] for pixel in pixels)
    
    
    ascii_str_lines = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    ascii_image = "\n".join(ascii_str_lines)
    
    return ascii_image


def main():
    image_path = input("Enter the path of the image file: ")
    ascii_art = image_to_ascii(image_path)
    if ascii_art:
        print("\nGenerated ASCII Art:\n")
        print(ascii_art)
        
       
        with open("ascii_art.txt", "w") as f:
            f.write(ascii_art)
        print("\nASCII art saved to ascii_art.txt")

if __name__ == "__main__":
    main()
