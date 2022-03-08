# Standard
import os
import platform

# Pip
import typer
import yaml
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
from yaml.scanner import ScannerError

# Custom
from auxiliary.MessageKeys import MessageKeys as mk
from auxiliary.FileExplorer import FileExplorer

# Typer app
app = typer.Typer()

# Files
current_dir = os.getcwd()
files = FileExplorer(home_dir=current_dir)

# Message keys
generate = mk.GeneratePdf
add_meta = mk.AddMetadata
gen_dir = mk.GenerateDir

# Mac and Windows use different slashes.
system: str = platform.system()
if system == "Darwin":
    slash = "/"
elif system == "Windows":
    slash = "\\"


@app.command(
    name=gen_dir.generate_dir,
    help=gen_dir.generate_dir_help
)
def generate_directories() -> None:
    """
    Generating directories wherein the file that should be combined
    are to reside.

        example:
        python main_app.py gen-dir
    :return:
        None
    """

    try:
        typer.echo(gen_dir.generating_dir)
        [os.makedirs(f) for f in ["config", "images", "pdfs", "results"]]
        typer.echo(gen_dir.directory_generated)
    except FileExistsError:
        typer.echo(gen_dir.folders_exists)


@app.command(name=generate.generate_pdf_name,
             help=generate.generate_pdf_command)
def generate_pdf(save_name: str = typer.Argument("generated",
                                            help=generate.generate_pdf_help)
                 ) -> None:
    """
    description:
         Images gathered from the images directory are combined into a single
        .pdf file that is then placed in the pdfs directory. Using the PIL
        library, .jpg, .gif, .png and .tga are supported.

    example:
        python main_app.py gen-pdf

    :arg:
         save_name: str the name of the .pdf file being saved.

    :returns
        no returns
    """

    image_dir: str = files.get_folders().get("images", "")
    path_exist: bool = os.path.exists(image_dir)

    if not path_exist:
        raise SystemExit(typer.echo(generate.missing_directory))

    images: list = []
    valid_images: list = [".jpg", ".jpeg", ".gif", ".png", ".tga"]

    for file_name in os.listdir(image_dir):
        ext: str = os.path.splitext(file_name)[1]
        if ext.lower() not in valid_images:
            continue

        img: str = os.path.join(image_dir, file_name)
        images.append(Image.open(img))

    if images:
        first_image = images[0]
        folders = files.get_folders()

        save: str = fr"{folders.get('pdfs')}{slash}{save_name}.pdf"

        # .pdf generation
        typer.echo(generate.images_generate)
        first_image.save(save,
                         save_all=True,
                         append_images=images[1:])
        typer.echo(generate.file_created)
    else:
        typer.echo(generate.no_images)


@app.command(name=add_meta.add_metadata_name,
             help=add_meta.add_metadata_help)
def add_metadata(
        pdf_name: str = typer.Argument("", help=add_meta.meta_pdf),
        config_name: str = typer.Argument("", help=add_meta.yaml_config)
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

    # Loading pdf file
    try:
        pdf: str = files.get_files("pdfs").get(pdf_name)
        pdf_in = open(pdf, "rb")
    except TypeError:
        raise SystemExit((typer.echo(add_meta.pdf_error)))

    # Loading .yaml file
    try:
        config_file: str = files.get_files("config").get(config_name)
        yaml_meta = yaml.load(open(config_file), Loader=yaml.FullLoader)
    except (TypeError, ScannerError) as error:
        if "yaml" in str(error):
            raise SystemExit(typer.echo(add_meta.yaml_error))
        else:
            raise SystemExit(typer.echo(add_meta.yaml_not_exist))

    # .pdf variables
    reader = PdfFileReader(pdf_in)
    writer = PdfFileWriter()
    writer.appendPagesFromReader(reader)
    metadata = reader.getDocumentInfo()
    writer.addMetadata(metadata)

    # config file
    writer.addMetadata(yaml_meta)

    # pdf with metadata
    save_path: str = files.get_folders().get("results")
    pdf_out = open(rf"{save_path}{slash}{pdf_name}", "wb")
    writer.write(pdf_out)

    # Closing files
    pdf_out.close()
    pdf_in.close()

    # Added metadata
    typer.echo(add_meta.metadata_added)


if __name__ == "__main__":
    app()