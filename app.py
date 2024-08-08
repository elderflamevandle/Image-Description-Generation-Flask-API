from flask import Flask, request, jsonify
import ollama
import os

app = Flask(__name__)

# Function to generate caption using the Ollama model
def generate_desciption(model, image_path, prompt):
    stream = ollama.generate(
        model=model,
        prompt=prompt,
        images=[image_path],
        stream=True
    )
    response = ""
    for chunk in stream:
        response += chunk['response']
    return response

@app.route('/generate_desciption', methods=['POST'])
def generate_description_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded image to a temporary location
    image_path = os.path.join("uploaded_image.png")
    image.save(image_path)

    # Prompt to generate the caption
    prompt = "'describe this image and make sure to include anything notable about it (include text you see in the image):"
    model = 'llava:7b-v1.5-q4_0'

    # Generate caption
    caption = generate_desciption(model, image_path, prompt)

    # Delete the image after processing
    os.remove(image_path)

    # Return the generated caption as JSON response
    return jsonify({"description": caption})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

