# Scrub

**Scrub** is a Python project designed to remove Personally Identifiable Information (PII) and Protected Health Information (PHI) from text, images, and other data structures. The project leverages the Microsoft Presidio library to analyze and anonymize sensitive information, making it a valuable tool for industries such as healthcare, legal, and finance where data privacy is critical.

## Features

- **Text Scrubbing**: Removes sensitive information such as email addresses, phone numbers, credit card numbers, social security numbers, and more from text data.
- **Image Scrubbing**: Detects and redacts sensitive information from images using a specified fill color.
- **Supports Multiple Data Types**: Works with strings, dictionaries, lists of dictionaries, and images.
- **Command-Line Interface (CLI)**: Easily scrub text or images via the command line.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KrishPatel13/Scrub.git
    cd Scrub
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Scrubbing Text

You can scrub sensitive information from text directly via the command line.

```bash
python scrub.py scrub_text "My email is john.doe@example.com and my phone number is 123-456-7890."
```

**Expected Output**:
```
My email is ******************** and my phone number is ************.
```

### Scrubbing Images

You can also scrub images to remove sensitive information.

```bash
python scrub.py scrub_image "path_to_your_image.png"
```

The scrubbed image will be saved as `scrubbed_image.png`.

### Example Output

Here is an example of an image before and after scrubbing:

- **Original Image**: Contains sensitive information like names, addresses, etc.
- **Scrubbed Image**: Sensitive regions are redacted using the default red color.

![Scrubbed Image](https://github.com/KrishPatel13/Scrub/blob/main/scrubbed_image.png)

> **Note**: The scrubbed image has been redacted to remove sensitive information, with the red color (default setting) indicating the redacted areas.

## Running Tests

To ensure everything is working correctly, you can run the included test suite.

1. **Navigate to the `tests/SCRUB` directory**:
    ```bash
    cd tests/SCRUB
    ```

2. **Run the tests**:
    ```bash
    pytest test_scrub.py
    ```

    The test suite will:
    - Validate that text scrubbing works as expected for various types of sensitive data (e.g., email, phone numbers, credit card numbers, etc.).
    - Confirm that image scrubbing masks the appropriate areas in an image.

## Configuration

The scrubbing process is highly configurable through the `config.py` file. Key configurations include:

- **NLP Engine**: The project uses the `spacy` NLP engine with a transformer-based model (`en_core_web_trf`) for analyzing text.
- **Scrubbing Entities**: You can define which types of PII/PHI to scrub by modifying the `SCRUBBING_ENTITIES` list.
- **Fill Color for Image Redaction**: The default color for masking sensitive information in images is red, but this can be customized through the `DEFAULT_SCRUB_FILL_COLOR` setting.

## Contribution

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


```
