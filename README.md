# Morse Code Translator

This Python program translates text to Morse code and vice versa. It provides functions to convert English text to Morse code and Morse code to English text.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/morse-code-translator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd morse-code-translator
    ```

3. Run the Python script:

    ```bash
    python morse_code_translator.py
    ```

4. Follow the prompts to choose the translation direction and provide input text.

## Functions

### `english_to_morse(text)`

Converts English text to Morse code.

**Parameters:**
- `text`: The English text to be translated.

**Returns:**
- `morse_code`: The Morse code representation of the input text.

### `morse_to_english(morse_code)`

Converts Morse code to English text.

**Parameters:**
- `morse_code`: The Morse code to be translated.

**Returns:**
- `english_text`: The English text representation of the input Morse code.

## Example

```python
english_text = "Hello, World!"
morse_code = english_to_morse(english_text)
print("Morse Code:", morse_code)

morse_code = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
english_text = morse_to_english(morse_code)
print("English Text:", english_text)
```

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
