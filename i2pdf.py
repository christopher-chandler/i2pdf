# Standard
import datetime
import os
import platform

from typing import Optional

# Pip
import typer
import yaml

from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
from yaml.scanner import ScannerError
from yaml.loader import SafeLoader

# Custom
from auxiliary.message_keys import MessageKeys as Mk
from auxiliary.file_explorer import FileExplorer

# Typer app
app = typer.Typer(no_args_is_help=True)

# Files
current_dir = os.getcwd()
files = FileExplorer(home_dir=current_dir)

# Message keys
generate = Mk.GeneratePdf
add_meta = Mk.AddMetadata
gen_dir = Mk.GenerateDir

# Mac and Windows use different slashes.
system: str = platform.system()
if system == "Darwin":
    slash = "/"
elif system == "Windows":
    slash = "\\"

now = datetime.datetime.now()
timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")


@app.command(name=gen_dir.generate_dir, help=gen_dir.generate_dir_help)
def generate_directories() -> None:
    """
    Generating directories wherein the files that should be combined
    are to reside.

        example:
        python main_app.py gen-dir
    :return:
        None
    """
    try:
        typer.echo(gen_dir.generating_dir)
        [
            os.makedirs(folder_dir)
            for folder_dir in ["config", "images", "pdfs", "results"]
        ]
        typer.echo(gen_dir.directory_generated)
    except FileExistsError:
        typer.echo(gen_dir.folders_exists)


@app.command(name=generate.generate_pdf_name,
             help=generate.generate_pdf_command)
def generate_pdf(
    dir_name: Optional[str] = typer.Option(
        current_dir,
        generate.generate_custom_dir_long,
        generate.generate_custom_dir_short,
        help=generate.generate_pdf_help,
    ),
    save_name: Optional[str] = typer.Option(
        f"generated_{timestamp}",
        generate.generated_file_name_long,
        generate.generated_file_name_short,
        help=generate.generate_pdf_help,
    ),
) -> None:
    """
    Description:
         Images gathered from the images directory are combined into a single
        .pdf file that is then placed in the pdfs directory. Using the PIL
        library, .jpg, .gif, .png and .tga are supported.
    Example:
        python main_app.py gen-pdf

    :arg:
         save_name: str the name of the .pdf file being saved.

    :returns
        no returns
    """

    if dir_name != "images":
        image_dir = dir_name
    else:
        image_dir: str = files.get_folders().get("images", current_dir)

    path_exist: bool = os.path.exists(image_dir)

    if not path_exist:
        raise SystemExit(typer.echo(generate.missing_directory))

    image_collection: list = []
    image_path_names: list = []
    valid_images: list = [".jpg", ".jpeg", ".gif", ".png", ".tga"]
    for file_name in sorted(os.listdir(image_dir)):

        ext: str = os.path.splitext(file_name)[1]
        if ext.lower() not in valid_images:
            continue

        img: str = os.path.join(image_dir, file_name)
        image_path_names.append(img)
        image_collection.append(Image.open(img))

    if image_collection:
        first_image = image_collection[0]
        folders = files.get_folders()

        if not image_dir:
            generated_pdf: str = rf"{folders.get('pdfs')}{slash}{save_name}.pdf"
        else:
            generated_pdf: str = rf"{image_dir}{slash}{save_name}.pdf"

        # .pdf generation
        typer.echo(generate.images_generate)
        first_image.save(generated_pdf, save_all=True,
                         append_images=image_collection[1:])
        typer.echo(generate.file_created)

        # Deleting images from directory
        answer = typer.prompt("Delete files ?: yes/y ")
        confirmation = ("y", "yes")

        if answer.lower() in confirmation:
            for image in image_path_names:
                os.remove(image)
            typer.echo(generate.images_removed)
        else:
            typer.echo(generate.retain_images)
    else:
        dir_echo_name = typer.style(dir_name, fg=typer.colors.BRIGHT_YELLOW)
        typer.echo(f"{generate.no_images} '{dir_echo_name}'")


@app.command(name=add_meta.add_metadata_name, help=add_meta.add_metadata_help)
def add_metadata(
    pdf_name: str = typer.Argument("", help=add_meta.meta_pdf),
    config_name: str = typer.Argument("", help=add_meta.yaml_config),
    save_name: str = typer.Argument(add_meta.results, help=add_meta.save_name),
) -> None:
    """
    description:
        the data from the .yaml file is added to the respective .pdf file
        as metadata

    example:
        python main_app.py add-metadata gen.pdf test.yaml

    :arg:
        pdf_name: str is the name of the .pdf which should have metadata added
        to it

        config_name: str is the name of the .yaml file which contains the
        metadata.

    :returns
        None
    """

    # Loading .pdf file
    try:
        pdf: str = files.get_files("pdfs").get(pdf_name)
        pdf_in = open(pdf, "rb")
    except TypeError:
        raise SystemExit((typer.echo(add_meta.pdf_not_exists)))

    # Loading .yaml file
    try:
        config_file: str = files.get_files("config").get(config_name)
        yfile = open(config_file, mode="r")
        yaml_meta = yaml.load(yfile, Loader=SafeLoader)
    except (TypeError, ScannerError, AttributeError) as error:
        if "yaml" in str(error):
            raise SystemExit(typer.echo(add_meta.yaml_error))
        else:
            raise SystemExit(typer.echo(add_meta.yaml_not_exist))

    try:
        # Loading .pdf
        reader = PdfFileReader(pdf_in)
        writer = PdfFileWriter()
        writer.appendPagesFromReader(reader)
        metadata = reader.getDocumentInfo()
        writer.addMetadata(metadata)

        typer.echo(f"The following metadata has been added:")
        for data in dict(yaml_meta):
            typer.echo(dict(yaml_meta).get(data))

        # config file
        writer.addMetadata(
            {
                '/Author': yaml_meta.get('/Author', 'Author unknown'),
                '/Title': yaml_meta.get('/Title', 'Title unknown'),
                '/Keywords': yaml_meta.get('/Keywords', 'Keywords unknown')
            }
        )

        # .pdf with metadata
        save_path: str = files.get_folders().get("results")
        pdf_out = open(rf"{save_path}{slash}{save_name}_{pdf_name}", "wb")
        writer.write(pdf_out)

        # Closing files
        pdf_out.close()
        pdf_in.close()

        # Added metadata
        typer.echo(add_meta.metadata_added)

    except OSError:
        raise SystemExit((typer.echo(add_meta.pdf_corrupt)))


if __name__ == "__main__":
    app()
