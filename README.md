# FuckWebp - WebP to PNG Converter

This script converts all `.webp` images in the folder to `.png` format, then deletes the original `.webp` files. Designed to sit in your Downloads folder, this script makes it easy to convert downloaded `.webp` images with a single command.

## Features

- **Batch Conversion**: Converts every `.webp` image in the folder to `.png`.
- **Automatic Deletion**: Deletes original `.webp` files after conversion.
- **Simple and Efficient**: Just run the script in your Downloads folder and it will handle all the conversions.

## Installation

1. Ensure you have Python installed.
2. Install the required library by running:
   ```bash
   pip install Pillow
   ```
3. Place the `FuckWebp.py` script in your Downloads folder or any folder containing `.webp` images you want to convert.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder containing the script:
   ```bash
   cd path/to/Downloads
   ```
3. Run the script:
   ```bash
   python FuckWebp.py
   ```
4. The script will convert each `.webp` file to `.png` and delete the original `.webp` files.

## Disclaimer

Please keep in mind that WebP achieves more efficient compression compared to other formats like JPEG and PNG, which means smaller file sizes for the same image quality. This can significantly reduce the amount of data needed to store and transmit images, which improves website load times and reduces bandwidth usage. Most modern web browsers, including Google Chrome, Firefox, Microsoft Edge, and Opera, support WebP. However, some older browsers might not support it, which can necessitate fallback options for compatibility.

Because WebP is relatively new, introduced by Google in 2010, it was not widely adopted by many established image editing software tools that standardized on older formats like JPEG (introduced in 1992) and PNG (introduced in 1996). This lack of universal support is why this script was created—to provide a simple way to convert `.webp` images into the more universally compatible `.png` format.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and make changes! If you improve the script or add new features, consider submitting a pull request to share your work.

---

### Disclaimer

This script is not affiliated with or endorsed by any official organization. Use it responsibly.
