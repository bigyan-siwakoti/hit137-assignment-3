# model_handler.py

import torch
from diffusers import StableDiffusionPipeline
from transformers import pipeline

# --- Global variables to hold the models ---
# We start with None and will load them on demand.
text_to_image_pipe = None
image_classifier_pipe = None

def load_models():
    """
    Loads both AI models into memory. Call this function once when the app starts.
    """
    global text_to_image_pipe, image_classifier_pipe
    
    print("Loading Text-to-Image model...")
    # This line is modified to be compatible with CPU execution
    text_to_image_pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    text_to_image_pipe = text_to_image_pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    print("Text-to-Image model loaded.")

    print("Loading Image Classification model...")
    image_classifier_pipe = pipeline("image-classification", model="google/vit-base-patch16-224")
    print("Image Classification model loaded.")

def generate_image_from_prompt(prompt_text):
    """
    Takes a text prompt and returns a generated image.
    """
    if text_to_image_pipe is None:
        return "Error: Text-to-Image model not loaded."
    
    print(f"Generating image for prompt: {prompt_text}")
    try:
        image = text_to_image_pipe(prompt_text).images[0]
        image.save("generated_image.png")
        return "Image successfully saved as generated_image.png"
    except Exception as e:
        return f"An error occurred: {e}"

def classify_image(image_path):
    """
    Takes a path to an image file and returns a text classification.
    """
    if image_classifier_pipe is None:
        return "Error: Image Classification model not loaded."
        
    print(f"Classifying image: {image_path}")
    try:
        results = image_classifier_pipe(image_path)
        formatted_results = "\n".join([f"Label: {res['label']}, Score: {res['score']:.2f}" for res in results])
        return formatted_results
    except Exception as e:
        return f"Error: Could not classify image: {e}"