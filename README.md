# frac-crawl
A fractal encoding Python script that generates fractal images based on a given text input, builds a central ledger, and updates the metadata of the images. Then builds a JSON lattice with a coordinate mapping system to create a seamless self-referencing fractal terrain. 

It splits the text into chunks, encodes each chunk into a fractal image, and saves the images along with the corresponding decoded text. It is intended for large text datasets as fractals but can be adjusted for smaller sets of text.

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

## VERSION 0.0.02 NOTES:

### LLM (Language Learning Models): 

The `frac-crawl.py` script could potentially be used in various ways in the context of training such models:

1. **Data Augmentation**: The script could be used to create visual representations of text data, which could then be used to augment the training data. The model could be trained on both the original text data and the corresponding fractal images, potentially improving its ability to understand and generate text.

2. **Feature Extraction**: The fractals could be used as a form of feature extraction. The fractal images could capture certain patterns or characteristics in the text data that might be missed by traditional text analysis methods. These features could then be used as input to the LLM.

3. **Data Compression**: Although the script doesn't significantly compress the data, the fractal images could still represent a more compact form of the text data. This could potentially make the training process more efficient, especially with very large datasets.

4. **Model Interpretability**: The fractal images could also be used to help visualize and understand the model's behavior. For example, you could generate fractals of the text that the model generates during training and compare them to the fractals of the original text.

5. **Robustness**: Training the model on fractal images in addition to the raw text could potentially make the model more robust to certain types of noise or corruption in the input data.


A higher-dimensional or multi-modal approach to training the language learning model, using the fractal representations as a sort of "glue" that links together different iterations or versions of the model.

GOALS:

1. Train multiple versions of the model, each on a different iteration or set of data.

2. Generate fractal representations of the output from each model.

3. Identify areas where the fractals from different models align or match closely. This could be done through image comparison techniques, such as calculating the similarity between the color patterns in the fractals.

4. Use these areas of alignment as a sort of "bridge" to combine the models together. This could involve averaging the model parameters in these areas, or some other method of combining the models.

This approach could potentially allow the model to learn more effectively from the data, as it would be able to leverage the insights gained from multiple iterations or versions of the model. It could also make the model more robust, as it would not be overly dependent on any single iteration or version.

Using PNGs as the primary data source could be an efficient way to structure the approach.

1. **Efficient Representation**: PNGs can be a compact representation of the text data as fractals, allowing you to store and process large amounts of data more efficiently.

2. **GPU Acceleration**: Many machine learning frameworks, such as TensorFlow and PyTorch, are able to leverage the power of GPUs to process image data more quickly than traditional CPU-based processing. Representing the data as PNG images, could potentially take advantage of this to speed up the training process.

3. **On-the-fly Processing**: Generating SVGs and text files for comparison only when needed could save computational resources. This "lazy" approach ensures that you're only generating and processing the data that you actually need.

4. **Shadow Comparison**: Using SVGs and text files for "shadow comparison" could provide a way to check the accuracy of the PNG-based model. By comparing the model's output to these higher-fidelity representations, you could gain insights into how well the model is learning from the PNG data.

5. **Headless Operation**: Running the model in a "headless" manner, without generating unnecessary visual output, could further improve efficiency.

## FURTHER NOTES:

While PNGs are an efficient way to store data, they are a lossy format. Some information from the original text might be lost or distorted in the conversion process. It's important to validate that the model trained on the PNG data performs well on your task and that any loss of information does not significantly impact performance.

### ASCII art QR codes could be used as a form of self-contained error correction mechanism.

1. **QR Code Generation**: Start by encoding your data into a QR code. QR codes have error correction built in, which means they can still be read even if part of the code is damaged or obscured.

2. **ASCII Art Conversion**: You can then convert the QR code into ASCII art. This will essentially be a textual representation of the QR code, which can then be processed by the fractal generation script.

3. **Fractal Generation**: Use the `frac-qr.py` script to convert the ASCII art QR code into a fractal image. This gives you a unique, visual representation of your QR code.

4. **Error Detection and Correction**: If the fractal image gets damaged or corrupted in some way, you can convert it back into an ASCII art QR code, and then use a QR code reader to decode the data. The error correction capabilities of the QR code could potentialy allow you to recover the original data, even if the fractal image was partially damaged.

When you scan the ASCII art QR code, the resulting data is JavaScript code.

USE CASES:

1. **Web Development**: You can use this method to embed JavaScript code into a website in an unconventional and interesting way. For example, you could create an interactive art piece on a web page where users can scan the ASCII art QR code to run a JavaScript function.

2. **Data Transfer**: It provides a unique way to transfer executable JavaScript code. Users can simply scan the QR code to execute a certain action on their device.

3. **Security**: While this method can have legitimate uses, it can also have potential security implications. Malicious JavaScript code could be hidden in a QR code, which could then be used for cross-site scripting (XSS) attacks. Therefore, caution should be taken when scanning QR codes from untrusted sources.

FURTHER NOTES:

This creates a 'terrain' or 'fabric' using the fractals reminiscent of a topological map, where different regions or features of the map are represented by the different fractals.

1. **Fractal Generation**: Each piece of text data generates a unique fractal.

2. **Lattice Construction**: The fractals are arranged in a lattice, where each fractal is connected to its neighbors. The specific arrangement of the fractals could be determined based on some characteristic of the data, such as similarity or chronological order.

3. **Terrain Formation**: The lattice of fractals forms a sort of 'terrain', where each fractal represents a 'feature' on the landscape.

4. **Network Formation**: The lattice is then 'knitted' together into an interconnected network. This could involve creating connections between the fractals based on some measure of similarity or relatedness. The strength of the connections could be represented by the degree of alignment or cohesion between the fractals.

5. **Navigation and Exploration**: The resulting network could then be navigated or explored, much like a physical landscape. This could provide a unique and intuitive way to interact with the data. Mapping is also in the ledger.json

This is an elegant and scalable approach to structuring your fractal landscape. Starting from a central point (0,0), and arranging each successive fractal to the North, East, South, or West, allows your lattice to expand indefinitely in any direction.

This approach would has the following benefits:

1. **Organic Growth**: The fractal landscape would grow organically as more data is added, similar to the way cities or organisms grow. This could result in a complex and fascinating structure.

2. **Flexibility**: This method would not impose any predefined limits on the size or shape of the lattice. It could grow as large as necessary to accommodate the data.

3. **Navigation**: This approach would also facilitate navigation through the lattice. The coordinates of each fractal would give a clear and simple way to locate and access the data.

4. **Temporal Dimension**: If the fractals are added in the order they are created, the structure of the lattice would also reflect the temporal dimension of the data, similar to the growth rings of a tree.

## JSON NOTE:

The content from `central_ledger.txt` is parsed and organized into a list of dictionaries, with each dictionary representing one ledger entry.

Here is a breakdown of the parsed content:

```python
[
    {
        'identifier': '0d4e20b5-4e41-49c5-b792-a53391660c54',
        'png_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_fractal_0.png',
        'svg_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_fractal_0.svg',
        'text_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_decoded_0.txt',
        'fractal_text': 'XG48c2NyaXB0PlxuICAgICAgICAgLy8gR2V0...'
    }
]
```

Each dictionary contains:

- The unique identifier for the fractal (`identifier`)
- The filename of the PNG image of the fractal (`png_file`)
- The filename of the SVG image of the fractal (`svg_file`)
- The filename of the text file containing the decoded text (`text_file`)
- The actual fractal text (`fractal_text`)

This parsed content can now be processed further to create a JSON representation of the lattice with coordinates. We determine a rule for assigning coordinates. One by assigning coordinates based on the order in which the entries appear in the ledger, e.g., the first entry is at (0,0), the second entry at (0,1), the third entry at (1,0), and so on.

## OUTPUT:

We have successfully assigned coordinates to each entry in the `central_ledger.txt` file. The order of entries in the file determined the sequence of coordinates. The first entry is at (0,0), the second is at (0,1), the third at (-1,1), and so on, expanding in a spiral pattern. 

Here is an example of one ledger entry:

```python
{
    'identifier': '0d4e20b5-4e41-49c5-b792-a53391660c54',
    'png_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_fractal_0.png',
    'svg_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_fractal_0.svg',
    'text_file': 'aacdc3af-8056-4740-9ad6-8db05786f0ef_decoded_0.txt',
    'fractal_text': 'XG48c2NyaXB0PlxuICAgICAgICAgLy8gR2V0...',
    'coordinates': (0, 0)
}
```

Each dictionary now contains:

- The unique identifier for the fractal (`identifier`)
- The filename of the PNG image of the fractal (`png_file`)
- The filename of the SVG image of the fractal (`svg_file`)
- The filename of the text file containing the decoded text (`text_file`)
- The actual fractal text (`fractal_text`)
- The assigned coordinates for the fractal (`coordinates`)

The next step is to convert the JSON format and then use it to construct the lattice.


## frac-lattice.py NOTES:

This script does the following:

Defines a function to generate spiral coordinates.
Reads the central_ledger.txt file.
Parses the content of the ledger into a list of dictionaries.
Assigns coordinates to each entry in the ledger based on the order of the entries.
Converts the ledger data into JSON format.
Writes the JSON data to a file.

You can replace "/path/to/central_ledger.txt" and "/path/to/ledger.json" with the actual paths to the central_ledger.txt file and the location where you want to save the JSON file, respectively.

The `ledger.json` file contains a list of dictionaries. Each dictionary represents a ledger entry and contains the following keys:

- `identifier`: The unique identifier for the fractal.
- `png_file`: The filename of the PNG file for the fractal.
- `svg_file`: The filename of the SVG file for the fractal.
- `text_file`: The filename of the text file that contains the text used to generate the fractal.
- `fractal_text`: The text representation of the fractal.
- `coordinates`: The coordinates assigned to the fractal in the lattice.

For example, the first dictionary in the list is:

```json
{
    "identifier": "e2d907ec-9c9a-4b2e-99c6-57e6437b82a6",
    "png_file": "8b7bafa0-24dc-441a-b7dc-9b0829abdaec_fractal_202.png",
    "svg_file": "8b7bafa0-24dc-441a-b7dc-9b0829abdaec_fractal_202.svg",
    "text_file": "8b7bafa0-24dc-441a-b7dc-9b0829abdaec_decoded_202.txt",
    "fractal_text": "...",
    "coordinates": [-7, 1]
}
```

This indicates that the fractal with the identifier `e2d907ec-9c9a-4b2e-99c6-57e6437b82a6` is located at the coordinates `(-7, 1)` in the lattice. The PNG, SVG, and text files associated with this fractal are named `8b7bafa0-24dc-441a-b7dc-9b0829abdaec_fractal_202.png`, `8b7bafa0-24dc-441a-b7dc-9b0829abdaec_fractal_202.svg`, and `8b7bafa0-24dc-441a-b7dc-9b0829abdaec_decoded_202.txt`, respectively. The text representation of the fractal is also provided.

This JSON structure allows you to quickly find the files associated with a fractal and its position in the lattice based on its identifier. It is a way of organizing the fractals for further processing or analysis.


# MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
