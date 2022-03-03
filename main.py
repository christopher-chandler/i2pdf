# standard
import os

None

# Pip
import typer
from PIL import Image

# Custom
None

app = typer.Typer()


def generate_folders():
    file_paths = dict()
    my_list = os.listdir(os.getcwd())
    for i in my_list:
        file_paths[i] = f"{os.getcwd()}\\{i}"

    return file_paths


folders = generate_folders()


def generate_pdf():
    """

    :return:
    """

    image_dir = folders.get("images")

    imgs = []

    valid_images = [".jpg", ".gif", ".png", ".tga"]
    for f in os.listdir(image_dir):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(image_dir, f)))

    first_image = imgs[0]
    first_image.convert("RGB")
    print(first_image)

    img = [first_image]

    first_image.save(
        "test.pdf", save_all=True, append_images= imgs[1:]
    )





if __name__ == "__main__":
    generate_pdf()