# frac-crawl
A fractal encoding Python script that generates fractal images based on a given text input, builds a central ledger, updates the metadata of the images.

It splits the text into chunks, encodes each chunk into a fractal image, and saves the images along with the corresponding decoded text. It is intended for large text datasets as fractals but can be adjusted for smaller also.

### Dependencies

To run the code, you will need the following dependencies:

- Python 3.x: The programming language used to write the code.
- Python Imaging Library (PIL): A library for opening, manipulating, and saving many different image file formats.
- NumPy: A library for scientific computing with Python, used for numerical operations and array manipulation.
- Matplotlib: A plotting library used to visualize the generated fractal images.
- Math: A standard Python module for mathematical operations and calculations.
- UUID: A module that provides a unique identifier generation.

### High-Level Overview

The code performs the following steps:

1. Input the text to be encoded into fractal images.
2. Specify the chunk size and number of characters per fractal.
3. Calculate the number of iterations required based on the text length and chunk size.
4. Generate a unique identifier for the set of fractals to be generated.
5. Set up the dimensions of the fractal images.
6. Iterate over the text, splitting it into chunks of the specified size.
7. For each chunk, encode the text into a fractal image using a custom encoding algorithm.
8. Save the fractal image as a PNG and SVG file.
9. Decode the fractal image back into text.
10. Save the decoded text in a separate text file.
11. Append information about the generated fractal to a central ledger.
12. Repeat steps 7-11 for each chunk of text.
13. Provide a summary of the generated fractals.

### Low-Level Overview

Here's a more detailed breakdown of each step:

1. Input the Text:
   - The code expects the user to provide a text input to be encoded into fractal images. This can be modified by assigning a text string to the `text` variable.

2. Specify Chunk Size and Number of Characters per Fractal:
   - The code allows you to specify the chunk size, which determines the number of characters processed in each iteration.
   - The `chunk_size` variable can be modified to set the desired chunk size.
   - The `num_chars` variable can be modified to specify the number of characters present in each fractal image.

3. Calculate the Number of Iterations:
   - Based on the length of the input text and the chunk size, the code calculates the number of iterations required to process the entire text.
   - The `math.ceil` function is used to ensure that any remaining characters in the text are included in the iterations.

4. Generate a Unique Identifier:
   - The code generates a unique identifier using the `uuid.uuid4()` function.
   - This identifier is used to create distinct filenames for the generated fractal images and decoded text files.

5. Set up Fractal Dimensions:
   - The `width` and `height` variables determine the dimensions of the fractal images.
   - By default, the code sets the dimensions to 1990x1990 pixels. These values can be modified as needed.

6. Iteration Loop:
   - The code enters a loop that iterates over the text chunks, processing each chunk separately.
   - The loop variable `i` represents the iteration number, starting from 0.

7. Fractal Encoding:
   - For each text chunk, the code encodes the text into a fractal image using a custom encoding algorithm.
   - The encoding algorithm converts each character in the text to a specific color value based on a predefined mapping.
   - The resulting colors are arranged in a square matrix, forming the fractal image.

8. Save Fractal Images:
   - The generated fractal image is saved in two formats: PNG and SVG.
   - The filenames are created using the fractal identifier, iteration number, and the corresponding file extension.

9. Fractal Decoding:
   - The code decodes the fractal image back into text by reverse-engineering the encoding algorithm.
   - This process involves extracting the color values from the fractal image and mapping them back to characters.

10. Save Decoded Text:
    - The decoded text is saved in a separate text file.
    - The filenames are created using the fractal identifier, iteration number, and the "decoded" keyword.

11. Central Ledger:
    - Information about each generated fractal is appended to a central ledger text file.
    - This ledger contains details such as the fractal identifier, filenames of the fractal images and decoded text, and iteration number.

12. Loop Completion and Summary:
    - Once all iterations are completed, the code provides a summary of the generated fractals.
    - The summary includes the fractal identifier, filenames of the fractal images and decoded text, and the iteration number.

### How to Use the Code

To use the code, follow these steps:

1. Install the required dependencies: Python 3.x, PIL, NumPy, Matplotlib, Math, and UUID.
2. Copy the code into a Python script file (e.g., `frac-crawl.py`).
3. Modify the `text` variable to include your desired text input.
4. Customize the settings, such as `chunk_size`, `num_chars`, `width`, and `height`, based on your requirements.
5. Run the Python script (`python frac-crawl.py`).
6. The code will generate fractal images based on your text input and save them as PNG and SVG files.
7. The decoded text will be saved in separate text files.
8. Information about the generated fractals will be appended to the central ledger.
9. The code will provide a summary of the generated fractals, including filenames and iteration numbers.

Remember to adjust the settings and text input according to your specific needs to achieve the desired results.

That's it! You should now have a clear understanding of how the code works and how to use it to generate fractal images from text.
