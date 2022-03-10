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
        """
        see function generate_directories
        """
        generate_dir = "gen-dir"
        generate_dir_help = "Generate directories where " \
                            "the files should reside."

        generating_dir = "Directories being generated."
        directory_generated = typer.style("Directories have been generated.",
                                          fg=typer.colors.GREEN)
        folders_exists = typer.style(
            "The folders already exist in this directory.", fg=typer.colors.RED
        )

    class GeneratePdf:
        """
        see function generate_pdf
        """
        generate_pdf_name = "gen-pdf"
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
        save_name = "The name of the new .pdf file with metadata."
        yaml_error = typer.style("The .yaml file could not be parsed. "
                                  "\nPlease make sure that you have "
                                  "correctly formatted the .yaml file",
                                 fg=typer.colors.RED)

        yaml_not_exist = typer.style(
            "The .yaml file that you have selected does not exist.",
            fg=typer.colors.RED
        )

        pdf_not_exists = typer.style("The .pdf either does not exist or the "
                                     "file name was not entered correctly. "
                                     "Please check the file name.",
                                     fg=typer.colors.RED)

        pdf_corrupt = typer.style("The file you entered is either corrput or "
                                 "is not a .pdf file. "
                                 "Please check the file again.",
                                      fg=typer.colors.RED)

        yaml_config = "The name of the .yaml file " \
                      "which contains the config data."
        metadata_added = typer.style(
            "The metadata has been successfully added!",
            fg=typer.colors.GREEN)