# Standard
import os
import yaml
from yaml.scanner import ScannerError
# Pip
import typer
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter

# Custom
from auxiliary.MessageKeys import MessageKeys as mk
from auxiliary.FileExplorer import FileExplorer

# Typer app
app = typer.Typer()

# Files
files = FileExplorer(home_dir=os.getcwd())

# Message keys
generate = mk.GeneratePdf
add_meta = mk.AddMetadata


@app.command(name=generate.generate_pdf_name,
             help=generate.generate_pdf_command)
def generate_pdf(save_name: str = typer.Argument("generated",
                                            help=generate.generate_pdf_help)):
    """
    description:
         Images gathered from the images directory are combined into a single
        .pdf file that is then placed in the pdfs directory. Using the PIL
        library, .jpg, .gif, .png and .tga are supported.

    example:
        python main.py generate

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

    valid_images: list = [".jpg", ".gif", ".png", ".tga"]

    for file_name in os.listdir(image_dir):
        ext: str = os.path.splitext(file_name)[1]
        if ext.lower() not in valid_images:
            continue

        img: str = os.path.join(image_dir, file_name)
        images.append(Image.open(img))

    if images:
        first_image = images[0]
        folders = files.get_folders()

        save: str = fr"{folders.get('pdfs')}/{save_name}.pdf"

        # .pdf generation
        print(generate.images_generate)
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
        config_name: str = typer.Argument("", help=add_meta.yaml_config)):

    """
    description:
        the data from the .yaml file is added to the respective .pdf file
        as metadata

    example:
        python main.py metadata gen.pdf test.yaml

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
        pdf = files.get_files("pdfs").get(pdf_name)
        pdf_in = open(pdf, "rb")
    except TypeError as error:
        raise SystemExit((typer.echo(add_meta.pdf_error)))

    # Loading .yaml file
    try:
        config_file = files.get_files("config").get(config_name)
        yaml_meta = yaml.load(open(config_file), Loader=yaml.FullLoader)
    except (TypeError, ScannerError) as error:
        if "yaml" in str(error):
            raise SystemExit(typer.echo(add_meta.yamal_error))
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
    save_path = files.get_folders().get("results")
    pdf_out = open(rf"{save_path}\{pdf_name}", "wb")
    writer.write(pdf_out)

    # Closing files
    pdf_out.close()
    pdf_in.close()

    # Added metadata
    typer.echo(add_meta.metadata_added)


if __name__ == "__main__":
    app()