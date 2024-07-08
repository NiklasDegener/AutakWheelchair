# ImageToHighColor conversion tool
Python command-line tool for image format conversion. Needs path to image file as input. Additional options available.
Takes any openCV supported image format (e.g. .png, .jpeg) as input and outputs a list of hex-values to be used in C code (e.g. for TFT screens)

## arguments
| Argument  | function | required? | default |
| ------------- | ------------- |
| "-f", "--file" | path to input image file | yes | x |
| "-o", "--output  | path to output text file | no | x |
| "-r", "--rows" | length of each output row | no | 16 |