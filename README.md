# Image Description Generation Flask API

This is a Flask web application that uses the Ollama model to generate descriptions for uploaded images.

## Requirements

- Python 3.7 or later
- The required Python packages are listed in the `requirements.txt` file.

## Installation

1. Create a new virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```

2. Install the required packages:
``` pip install -r requirements.txt ```

## Usage

1. Run the Flask app:
``` python app.py ```

2. Open your web browser and go to `http://localhost:5000/`.

## Endpoints

- **`/generate_desciption`** (POST): This endpoint accepts an image file in the `image` field of the request body and generates a description for the image using the Ollama model. The generated description is returned as a JSON response.

## API Usage Example

You can use a tool like Postman or cURL to interact with the API. Here's an example using cURL:
```
curl -X POST -F 'image=@/path/to/your/image.jpg' http://localhost:5000/generate_desciption
```

This will send a POST request to the `/generate_desciption` endpoint with the image file attached. The API will respond with a JSON object containing the generated description.

## Files

- `app.py`: The main Flask application file that handles the image processing and description generation.

## Customization

You can customize the following aspects of the application:

- **Ollama Model**: The current implementation uses the `'llava:7b-v1.5-q4_0'` model. You can change this by modifying the `model` variable in the `generate_desciption()` function.
- **Prompt**: The current prompt is `"'describe this image and make sure to include anything notable about it (include text you see in the image):"`. You can modify this to change the instructions for the Ollama model.

## License

This project is licensed under the [Apache Licence 2.0](LICENSE).

