# i2pdf
i2pdf is a simple CLIP that combines ***.jpegs,
.png, .jpg, .gif*** files into a single pdf. There is also the 
option of assigning metadata to this generated .pdf.

![shields.io](https://img.shields.io/badge/License-MIT-red)
![Version Number](https://img.shields.io/badge/Version-1.0.3-brightgreen)
![Lastupdated](https://img.shields.io/badge/Last_Updated-March_2022-blue)
![System](https://img.shields.io/badge/Windows-Tested-yellow)
![System](https://img.shields.io/badge/Mac-Tested-purple)


# License 
i2pdf comes with the [MIT](https://opensource.org/licenses/MIT) license.
Please use this license when reusing this code. 

# Dependencies 
i2pdf was created with python 3.9 and should be used with this version of python 

## Standard Libraries
The following standard libraries are used. 
```
os
platform
```

## Pip 
The following dependencies are necessary.
```
typer~=0.4.0
PyYAML~=6.0
Pillow~=9.0.1
PyPDF2~=1.26.0
```

# Install 

To install, enter the following command. 
```
pip install i2pdf
```

If the installation was successful, then the following text 
should appear in the terminal 

Mac example
```
Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  add-metadata  Add the data from the .yaml file to the .pdf as metadata.
  generate-dir  Generating directories where the files should reside.
  generate-pdf  Generate a .pdf from a collection of images.
```

# Commands

## add-metadata

```
Arguments:
  [PDF_NAME]     The name of the .pdf that should have metadata added.
                 [default: ]

  [CONFIG_NAME]  The name of the .yaml file which contains the config data.
                 [default: ]
```

Example:
```
i2pdf add-metadata test.pdf test.yml
```

If you wish to have metadata added to the .pdf,
you must store it in a .yaml or .yml file. 

The format of this file should be as follows:
```
/author: test author
/keywords: test keywords
```

This file should be stored in the config folder. 

## generate-dir 
Before you can combine the images to a .pdf,
you must first generate the necessary folders. 
It is possible to do this by hand, 
but this command automatically generates the folders 
in the directy in which i2pdf was called. 

The following empty folders are generated:

| Folder      | Description |
| ----------- | ----------- |
| config      | this contains the .yaml files.       |
| images   | the image files that are to be combined to a pdf        |
| pdfs      | the generated .pdf files.       |
| results | the pdf files that had metadata added .       |

## generate-pdf 
```
Arguments:
  [SAVE_NAME]  Enter the save name of the .pdf file  [default: generated]
```

Example:
```
i2pdf generate-pdf testfile
```
Place the images in this file that are to be combined to a .pdf file.
You have the option of specifying a name for the file being generated.
if no file is added, then it is automatically called generated 