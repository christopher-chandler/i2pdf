# Standard
None

# Pip
import typer

# Custom
None


class MessageKeys:
    """
    This class contains the strings for the respective functions
    so that they can be accessed through dot notation.
    """

    class GenerateDir:
        generate_dir ="generate-dir"
        generate_dir_help = "Generating directories " \
                            "where the files should reside."
    class GeneratePdf:
        """
        see function generate_pdf
        """
        generate_pdf_name = "generate-pdf"
        generate_pdf_command = "Generate a .pdf from a collection of images."
        images_generate = typer.style(
            "The .pdf file is being generated. Please wait...",
            fg=typer.colors.BRIGHT_MAGENTA
            )
        generate_pdf_help = "Enter the save name of the .pdf file"
        file_created = typer.style(".pdf file was successfully created!",
                                   fg=typer.colors.GREEN)
        no_images = typer.style("Error: Please make sure that "
                                "there are images in the image directory",
                                fg=typer.colors.RED)
        missing_directory = typer.style(
            "Error: The image directory is missing!",
            fg=typer.colors.BRIGHT_MAGENTA)

    class AddMetadata:
        """
        see function add_metadata
        """
        add_metadata_name = "add-metadata"
        add_metadata_help = "Add the data from the .yaml file " \
                            "to the .pdf as metadata."

        meta_pdf = "The name of the .pdf that should have metadata added."

        yamal_error = typer.style("The .yaml file could not be parsed. "
                                  "\nPlease make sure that you have "
                                  "correctly formatted the .yaml file",
                                  fg=typer.colors.RED)

        yaml_not_exist = typer.style(
            "The .yaml file that you have selected does not exist.",
            fg=typer.colors.RED
        )

        pdf_error = typer.style("The .pdf either does not exist or is corrupt"
                                "Please check the file", fg=typer.colors.RED)

        yaml_config = "The name of the .yaml file " \
                      "which contains the config data."
        metadata_added = typer.style(
            "The metadata has been successfully added!",
            fg=typer.colors.GREEN)
