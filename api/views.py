import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from io import BytesIO
from PIL import Image
import base64
from django.http import HttpResponse

API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
HEADERS = {
    "Authorization": "Bearer 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"
}  # Replace with your actual Hugging Face API token


class ImageGenerationView(APIView):
    def post(self, request, *args, **kwargs):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response(
                {"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
        print(response)

        if response.status_code != 200:
            return Response(
                {"error": "Failed to generate image"}, status=response.status_code
            )

        image_bytes = response.content

        # Return the image as an HTTP response
        return HttpResponse(image_bytes, content_type="image/png")
