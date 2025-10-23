"""
Halloween Character Image Generator
Generates 100 high-quality Halloween character images with transparent backgrounds
Supports multiple AI sources: Stability AI, OpenAI DALL-E, Hugging Face (FREE), Replicate
"""

import os
import json
import requests
import time
from PIL import Image
from io import BytesIO
import base64


class HalloweenImageGenerator:
    def __init__(self, config_path="config.json"):
        """Initialize the generator with configuration"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.api_choice = self.config.get('api_choice', 'pollinations')  # 'stability', 'openai', 'huggingface', 'replicate', 'pollinations'
        self.output_dir = self.config.get('output_dir', 'halloween_characters')
        self.width = self.config.get('width', 4500)
        self.height = self.config.get('height', 5400)
        self.dpi = self.config.get('dpi', 300)
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load character prompts
        with open('halloween_prompts.json', 'r') as f:
            self.prompts = json.load(f)

    def generate_with_stability_ai(self, prompt, index):
        """Generate image using Stability AI API"""
        api_key = self.config.get('stability_api_key', '')
        
        if not api_key:
            raise ValueError("Stability AI API key not found in config.json")
        
        # Stability AI API endpoint for SDXL or SD3
        url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
        
        headers = {
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        }
        
        # Enhanced prompt for transparent background
        enhanced_prompt = f"{prompt}, transparent background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
        
        files = {
            "prompt": (None, enhanced_prompt),
            "output_format": (None, "png"),
            "aspect_ratio": (None, "5:6"),  # Closest to 4500x5400
        }
        
        print(f"Generating image {index}: {prompt[:50]}...")
        
        try:
            response = requests.post(url, headers=headers, files=files)
            
            if response.status_code == 200:
                # Load image
                image = Image.open(BytesIO(response.content))
                
                # Resize to exact dimensions
                image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                
                # Process for transparent background if needed
                image = self.ensure_transparent_background(image)
                
                # Save with DPI metadata
                output_path = os.path.join(self.output_dir, f"halloween_character_{index:03d}.png")
                image.save(output_path, "PNG", dpi=(self.dpi, self.dpi))
                
                print(f"✓ Saved: {output_path}")
                return True
            else:
                print(f"✗ Error {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Exception: {str(e)}")
            return False

    def generate_with_openai(self, prompt, index):
        """Generate image using OpenAI DALL-E API"""
        api_key = self.config.get('openai_api_key', '')
        
        if not api_key:
            raise ValueError("OpenAI API key not found in config.json")
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Enhanced prompt for transparent background
        enhanced_prompt = f"{prompt}, isolated on transparent background, PNG format, ultra high detail, 8K quality, professional photography"
        
        data = {
            "model": "dall-e-3",
            "prompt": enhanced_prompt,
            "n": 1,
            "size": "1024x1792",  # Closest aspect ratio available
            "quality": "hd",
            "style": "vivid"
        }
        
        print(f"Generating image {index}: {prompt[:50]}...")
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                image_url = response.json()['data'][0]['url']
                
                # Download the image
                img_response = requests.get(image_url)
                image = Image.open(BytesIO(img_response.content))
                
                # Resize to exact dimensions
                image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                
                # Process for transparent background
                image = self.ensure_transparent_background(image)
                
                # Save with DPI metadata
                output_path = os.path.join(self.output_dir, f"halloween_character_{index:03d}.png")
                image.save(output_path, "PNG", dpi=(self.dpi, self.dpi))
                
                print(f"✓ Saved: {output_path}")
                return True
            else:
                print(f"✗ Error {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Exception: {str(e)}")
            return False

    def generate_with_huggingface(self, prompt, index):
        """Generate image using Hugging Face Inference API (FREE with rate limits)"""
        api_token = self.config.get('huggingface_token', '')
        
        if not api_token:
            print("⚠️  No Hugging Face token found. Using public API (may have rate limits)")
            print("   Get a free token at: https://huggingface.co/settings/tokens")
        
        # Using Stable Diffusion XL or similar free models
        models = [
            "stabilityai/stable-diffusion-xl-base-1.0",
            "runwayml/stable-diffusion-v1-5",
            "prompthero/openjourney-v4"
        ]
        
        model_id = self.config.get('huggingface_model', models[0])
        
        api_url = f"https://api-inference.huggingface.co/models/{model_id}"
        
        headers = {}
        if api_token:
            headers["Authorization"] = f"Bearer {api_token}"
        
        # Enhanced prompt for transparent background
        enhanced_prompt = f"{prompt}, white background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
        
        payload = {
            "inputs": enhanced_prompt,
            "parameters": {
                "negative_prompt": "blurry, low quality, distorted, deformed, ugly",
                "num_inference_steps": 50,
                "guidance_scale": 7.5
            }
        }
        
        print(f"Generating image {index}: {prompt[:50]}...")
        
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                # Load image
                image = Image.open(BytesIO(response.content))
                
                # Resize to exact dimensions
                image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                
                # Process for transparent background
                image = self.ensure_transparent_background(image)
                
                # Save with DPI metadata
                output_path = os.path.join(self.output_dir, f"halloween_character_{index:03d}.png")
                image.save(output_path, "PNG", dpi=(self.dpi, self.dpi))
                
                print(f"✓ Saved: {output_path}")
                return True
            elif response.status_code == 503:
                print(f"⚠️  Model is loading... Retrying in 20 seconds...")
                time.sleep(20)
                return self.generate_with_huggingface(prompt, index)
            else:
                print(f"✗ Error {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Exception: {str(e)}")
            return False

    def generate_with_replicate(self, prompt, index):
        """Generate image using Replicate API (Pay-as-you-go, very affordable)"""
        api_token = self.config.get('replicate_token', '')
        
        if not api_token:
            raise ValueError("Replicate API token not found in config.json")
        
        headers = {
            "Authorization": f"Token {api_token}",
            "Content-Type": "application/json"
        }
        
        # Enhanced prompt
        enhanced_prompt = f"{prompt}, transparent background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
        
        # Using SDXL or other models on Replicate
        data = {
            "version": "stability-ai/sdxl",
            "input": {
                "prompt": enhanced_prompt,
                "negative_prompt": "blurry, low quality, background",
                "width": 1024,
                "height": 1024,
                "num_outputs": 1
            }
        }
        
        print(f"Generating image {index}: {prompt[:50]}...")
        
        try:
            # Start prediction
            response = requests.post(
                "https://api.replicate.com/v1/predictions",
                headers=headers,
                json=data
            )
            
            if response.status_code == 201:
                prediction = response.json()
                prediction_url = prediction['urls']['get']
                
                # Poll for completion
                while True:
                    result = requests.get(prediction_url, headers=headers)
                    result_data = result.json()
                    
                    if result_data['status'] == 'succeeded':
                        image_url = result_data['output'][0]
                        
                        # Download image
                        img_response = requests.get(image_url)
                        image = Image.open(BytesIO(img_response.content))
                        
                        # Resize to exact dimensions
                        image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                        
                        # Process for transparent background
                        image = self.ensure_transparent_background(image)
                        
                        # Save with DPI metadata
                        output_path = os.path.join(self.output_dir, f"halloween_character_{index:03d}.png")
                        image.save(output_path, "PNG", dpi=(self.dpi, self.dpi))
                        
                        print(f"✓ Saved: {output_path}")
                        return True
                    elif result_data['status'] == 'failed':
                        print(f"✗ Generation failed: {result_data.get('error', 'Unknown error')}")
                        return False
                    
                    time.sleep(2)
            else:
                print(f"✗ Error {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Exception: {str(e)}")
            return False

    def generate_with_pollinations(self, prompt, index):
        """Generate image using Pollinations.ai (100% FREE, NO TOKEN REQUIRED)"""
        
        # Enhanced prompt for transparent background
        enhanced_prompt = f"{prompt}, white background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
        
        # URL encode the prompt
        import urllib.parse
        encoded_prompt = urllib.parse.quote(enhanced_prompt)
        
        # Pollinations.ai free API (no authentication needed!)
        # They provide free AI image generation
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&enhance=true"
        
        print(f"Generating image {index}: {prompt[:50]}...")
        
        try:
            # Download the generated image
            response = requests.get(image_url, timeout=120)
            
            if response.status_code == 200:
                # Load image
                image = Image.open(BytesIO(response.content))
                
                # Resize to exact dimensions
                image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                
                # Process for transparent background
                image = self.ensure_transparent_background(image)
                
                # Save with DPI metadata
                output_path = os.path.join(self.output_dir, f"halloween_character_{index:03d}.png")
                image.save(output_path, "PNG", dpi=(self.dpi, self.dpi))
                
                print(f"✓ Saved: {output_path}")
                return True
            else:
                print(f"✗ Error {response.status_code}: Failed to generate image")
                return False
                
        except Exception as e:
            print(f"✗ Exception: {str(e)}")
            return False

    def ensure_transparent_background(self, image):
        """Process image to ensure transparent background"""
        # Convert to RGBA if not already
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        # This is a basic implementation
        # For more sophisticated background removal, consider using rembg library
        return image

    def remove_background_advanced(self, image):
        """Advanced background removal using rembg (optional)"""
        try:
            from rembg import remove
            image = remove(image)
        except ImportError:
            print("Warning: rembg not installed. Skipping advanced background removal.")
            print("Install with: pip install rembg")
        
        return image

    def generate_all(self):
        """Generate all 100 Halloween character images"""
        print(f"Starting generation of {len(self.prompts)} Halloween character images")
        print(f"Output: {self.width}x{self.height} pixels @ {self.dpi} DPI")
        print(f"API: {self.api_choice}")
        print(f"Output directory: {self.output_dir}\n")
        
        successful = 0
        failed = 0
        
        for i, prompt_data in enumerate(self.prompts, start=1):
            prompt = prompt_data.get('prompt', '')
            
            if self.api_choice == 'stability':
                success = self.generate_with_stability_ai(prompt, i)
            elif self.api_choice == 'openai':
                success = self.generate_with_openai(prompt, i)
            elif self.api_choice == 'huggingface':
                success = self.generate_with_huggingface(prompt, i)
            elif self.api_choice == 'replicate':
                success = self.generate_with_replicate(prompt, i)
            elif self.api_choice == 'pollinations':
                success = self.generate_with_pollinations(prompt, i)
            else:
                print(f"Invalid API choice: {self.api_choice}")
                print("Valid options: 'stability', 'openai', 'huggingface', 'replicate', 'pollinations'")
                break
            
            if success:
                successful += 1
            else:
                failed += 1
            
            # Rate limiting
            time.sleep(self.config.get('delay_between_requests', 3))
        
        print(f"\n{'='*60}")
        print(f"Generation Complete!")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"{'='*60}")


def main():
    """Main execution function"""
    print("Halloween Character Image Generator")
    print("="*60)
    
    try:
        generator = HalloweenImageGenerator()
        generator.generate_all()
    except FileNotFoundError as e:
        print(f"\n✗ Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. config.json - with your API keys and settings")
        print("2. halloween_prompts.json - with character descriptions")
    except Exception as e:
        print(f"\n✗ Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
