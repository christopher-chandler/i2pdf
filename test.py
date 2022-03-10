# Standard
import os
import platform

# Pip
import typer
import yaml
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
from yaml.scanner import ScannerError
from yaml.loader import SafeLoader

# Custom
from auxiliary.MessageKeys import MessageKeys as mk
from auxiliary.FileExplorer import FileExplorer

system: str = platform.system()
if system == "Darwin":
    slash = "/"
elif system == "Windows":
    slash = "\\"

# Typer app
app = typer.Typer()
pdf_name ="test"
# Files
current_dir = os.getcwd()
files = FileExplorer(home_dir=current_dir)

# Message keys
generate = mk.GeneratePdf
add_meta = mk.AddMetadata
gen_dir = mk.GenerateDir


# Loading pdf file
pdf: str = files.get_files("pdfs").get("generated.pdf")
pdf_in = open(pdf, "rb")

config_file: str = files.get_files("config").get("test.yaml")
yfile = open(config_file, mode="r")
yaml_meta = yaml.load(yfile, Loader=SafeLoader)


# .pdf variables

reader = PdfFileReader(pdf)
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