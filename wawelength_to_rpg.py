from PIL import Image
import pickle

filename = 'wawelength.png'


def main():
    with Image.open(filename) as image:
        # Resize original wawelength image to 100 * 1 pixel size
        image_resize = image.resize((100, 1))
        # Save resized image
        image_resize.save("wawelength_resize.png")
        # Get resized image data
        image_data = image_resize.getdata()
        # Save resized image data to file.
        print(list(image_data))
        with open('wawelength.pickle', 'wb') as fp:
            pickle.dump(list(image_data), fp)


if __name__ == "__main__":
    main()
