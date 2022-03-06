# standard
import os

# Pip
import typer
from PIL import Image

# Custom
from auxiliary.MessageKeys import MessageKeys as mk
from auxiliary.scripts import folders
from auxiliary.scripts import time_stamp


# Typer app
app = typer.Typer()


@app.command(help="Generate a .pdf from a collection of images.")
def generate_pdf(save_name: str = typer.Argument("save",
                help="Enter the save name of the .pdf file")
                 ):
    """

    :return:
    """

    image_dir: str = folders.get("images", "")

    if not os.path.exists(image_dir):
        msg = typer.style(mk.missing_directory, fg=typer.colors.BRIGHT_MAGENTA)
        typer.echo(msg)
        raise SystemExit

    images: list = []
    valid_images: list = [".jpg", ".gif", ".png", ".tga"]

    for file_name in os.listdir(image_dir):
        ext: str = os.path.splitext(file_name)[1]
        if ext.lower() not in valid_images:
            continue

        img: str = os.path.join(image_dir, file_name)
        images.append(Image.open(img))

    if images:
        first_image = images[0]

        save: str = fr"{folders.get('results')}/{save_name}_{time_stamp}.pdf"

        first_image.save(
            save,
            save_all=True,
            append_images=images[1:]
        )

        msg = typer.style(mk.file_created, fg=typer.colors.GREEN)
        typer.echo(msg)

    else:
        msg = typer.style(mk.no_images, fg=typer.colors.RED)
        typer.echo(msg)


if __name__ == "__main__":
    app()