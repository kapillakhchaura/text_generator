# task4_text_generator.py

# Import necessary libraries
from transformers import pipeline, set_seed

# Initialize GPT-2 text generation pipeline
print("Loading GPT-2 model (please wait for a few seconds)...")
generator = pipeline('text-generation', model='gpt2')

# Set random seed for consistent results
set_seed(42)

# Take topic input from user
topic = input("Enter a topic to generate a paragraph: ")

# Generate paragraph using GPT-2
print("\nGenerating text...\n")
output = generator(topic, max_length=100, num_return_sequences=1)

# Display the generated text
print("Generated Paragraph:\n")
print(output[0]['generated_text'])
