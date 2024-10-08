import requests
from django.shortcuts import render
from django.conf import settings
from .models import Location, SatelliteImage
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('POSITIONSTACK_API_KEY')
# Your API key from PositionStack
def home(request):
    return render(request, 'base/home.html')

def save_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude and longitude:
            # Make the API request to PositionStack
            api_url = f'http://api.positionstack.com/v1/reverse?access_key={API_KEY}&query={latitude},{longitude}'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                location_info = data['data'][0]['label'] if data['data'] else 'Location not found'
                
                  # Save the location to the database
                location, created = Location.objects.get_or_create(
                    latitude=latitude,
                    longitude=longitude,
                    defaults={'address': location_info}
                )

                # Fetch the satellite images for this location
                satellite_images = SatelliteImage.objects.filter(location=location)

                # Render the home page with location information and satellite images
                return render(request, 'base/home.html', {
                    'latitude': latitude,
                    'longitude': longitude,
                    'location_info': location_info,
                    'satellite_images': satellite_images
                })

    # If no POST data, just render the home page without location
    return render(request, 'base/home.html')


import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import geopy.distance

# ReliefWeb API URL for disasters
RELIEFWEB_API_URL = 'https://api.reliefweb.int/v1/disasters'

# Function to check if a location is under a natural calamity using ReliefWeb API
def check_disaster(latitude, longitude):
    # Set parameters for ReliefWeb API request to get recent disasters
    params = {
        'appname': 'your-app-name',
        'filter[field]': 'status',
        'filter[value]': 'current', 
        'limit': 10  # You can increase this if needed
    }

    response = requests.get(RELIEFWEB_API_URL, params=params)
    disasters = response.json().get('data', [])

    # Iterate over disasters and check if any are near the given coordinates
    for disaster in disasters:
        disaster_fields = disaster.get('fields', {})
        disaster_location = disaster_fields.get('primary_country', {}).get('location', None)

        # If a location is available, check the distance to the given coordinates
        if disaster_location:
            disaster_lat = disaster_location['lat']
            disaster_lon = disaster_location['lon']

            # Check if the disaster is within a certain radius (e.g., 100km) of the user's location
            if is_within_radius(latitude, longitude, disaster_lat, disaster_lon, 100):
                return {
                    'is_under_calamity': True,
                    'disaster_type': disaster_fields.get('name', 'Unknown Disaster'),
                    'description': disaster_fields.get('description', 'No description available')
                }

    return {'is_under_calamity': False}


# Helper function to calculate the distance between two lat/lon points (using Haversine formula)
import math

def is_within_radius(lat1, lon1, lat2, lon2, radius_km):
    # Calculate the distance between two lat/lon points
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    distance = geopy.distance.distance(coords_1, coords_2).km
    return distance <= radius_km

# Django view to handle the incoming POST request with coordinates
@csrf_exempt
def disaster_status_view(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # Check if the location is under a calamity
        result = check_disaster(latitude, longitude)

        # Pass the result to calamity_result.html
        return render(request, 'base/calamity_result.html', result)

    return render(request, 'disaster.html', {'error': 'Invalid request'})


import os
import cv2
import numpy as np
from django.shortcuts import render, get_object_or_404
from .forms import CoordinateForm
from .models import SatelliteImage
from tensorflow.keras.models import load_model, Model # type: ignore
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, MaxPooling2D, UpSampling2D, concatenate, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore

# U-Net model definition
def unet_model(input_size=(256, 256, 1)):
    inputs = Input(input_size)

    # Encoding path
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = BatchNormalization()(conv1)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = Conv2D(128, 3, activation='relu', padding='same')(pool1)
    conv2 = BatchNormalization()(conv2)
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(conv2)
    conv2 = BatchNormalization()(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = BatchNormalization()(conv3)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)
    conv3 = BatchNormalization()(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = Conv2D(512, 3, activation='relu', padding='same')(pool3)
    conv4 = BatchNormalization()(conv4)
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(conv4)
    conv4 = BatchNormalization()(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

    conv5 = Conv2D(1024, 3, activation='relu', padding='same')(pool4)
    conv5 = BatchNormalization()(conv5)
    conv5 = Conv2D(1024, 3, activation='relu', padding='same')(conv5)
    conv5 = BatchNormalization()(conv5)
    conv5 = Dropout(0.5)(conv5)

    # Decoding path
    up6 = UpSampling2D(size=(2, 2))(conv5)
    merge6 = concatenate([conv4, up6], axis=3)
    conv6 = Conv2D(512, 3, activation='relu', padding='same')(merge6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Conv2D(512, 3, activation='relu', padding='same')(conv6)
    conv6 = BatchNormalization()(conv6)

    up7 = UpSampling2D(size=(2, 2))(conv6)
    merge7 = concatenate([conv3, up7], axis=3)
    conv7 = Conv2D(256, 3, activation='relu', padding='same')(merge7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Conv2D(256, 3, activation='relu', padding='same')(conv7)
    conv7 = BatchNormalization()(conv7)

    up8 = UpSampling2D(size=(2, 2))(conv7)
    merge8 = concatenate([conv2, up8], axis=3)
    conv8 = Conv2D(128, 3, activation='relu', padding='same')(merge8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Conv2D(128, 3, activation='relu', padding='same')(conv8)
    conv8 = BatchNormalization()(conv8)

    up9 = UpSampling2D(size=(2, 2))(conv8)
    merge9 = concatenate([conv1, up9], axis=3)
    conv9 = Conv2D(64, 3, activation='relu', padding='same')(merge9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Conv2D(64, 3, activation='relu', padding='same')(conv9)
    conv9 = BatchNormalization()(conv9)

    conv10 = Conv2D(1, 1, activation='sigmoid')(conv9)

    model = Model(inputs, conv10)
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

    return model

def load_and_preprocess_image(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Resize the image to 256x256
    image = cv2.resize(image, (256, 256))
    # Normalize the pixel values to [0, 1]
    image = image / 255.0
    # Reshape to add the channel dimension
    image = np.expand_dims(image, axis=-1)  # shape (256, 256, 1)
    # Expand dimensions to create a batch of size 1
    image = np.expand_dims(image, axis=0)  # shape (1, 256, 256, 1)
    return image

def pathfinding_view(request, image_id):
    image_instance = get_object_or_404(SatelliteImage, id=image_id)
    image_path = image_instance.image.path

    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            # Get start and goal coordinates from the form
            start_x = form.cleaned_data['start_x']
            start_y = form.cleaned_data['start_y']
            goal_x = form.cleaned_data['goal_x']
            goal_y = form.cleaned_data['goal_y']
            start = (start_x, start_y)
            goal = (goal_x, goal_y)

            # Load and preprocess the image
            test_image = load_and_preprocess_image(image_path)

            # Load training images and masks
            train_images, train_masks = load_training_data()  # Function should load your data properly

            # Ensure training data has the correct shape
            train_images = np.expand_dims(train_images, axis=-1)  # Add channel if missing
            train_masks = np.expand_dims(train_masks, axis=-1)    # Add channel if missing

            # Initialize U-Net model
            model = unet_model()

            # Train the model on the training data
            model.fit(train_images, train_masks, batch_size=8, epochs=10)

            # Save the trained model
            model.save(os.path.join('your_model_directory', 'unet_trained.h5'))

            # Predict the mask using the trained U-Net model
            predicted_mask = model.predict(test_image)[0, :, :, 0]

            # Post-process the predicted mask
            predicted_mask = post_process_mask(predicted_mask)

            # Perform A* search to find the path
            path = a_star_search(start, goal, lambda node: heuristic(node, goal), predicted_mask)

            # Draw the path on the original image
            colored_image = draw_path_on_image(test_image[0, :, :, 0], path)

            return render(request, 'base/path_result.html', {
                'image': image_instance,
                'path': path,
                'colored_image': convert_image_to_html(colored_image),
            })
    else:
        form = CoordinateForm()

    return render(request, 'base/pathfinding.html', {
        'form': form,
        'image': image_instance,
    })

def draw_path_on_image(image, path):
    """
    Draw the safe path on the image.
    """
    # Convert predicted mask to 3 channels (RGB) for visualization
    colored_image = cv2.cvtColor((image * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)

    # Draw the path as a line in red
    for i in range(1, len(path)):
        start_point = (int(path[i - 1][0]), int(path[i - 1][1]))
        end_point = (int(path[i][0]), int(path[i][1]))
        cv2.line(colored_image, start_point, end_point, (0, 0, 255), thickness=2)

    return colored_image

from io import BytesIO
import base64
from PIL import Image

def convert_image_to_html(image):
    """
    Convert an OpenCV image to a format suitable for HTML display (base64-encoded).
    """
    # Convert OpenCV image to PIL Image for better handling
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{image_base64}"

def load_training_data():
    """
    Load training images and masks from your dataset directory.
    Replace this with your actual data loading logic.
    """
    # Assuming images and masks are stored in two separate directories
    images_dir = 'static/images'
    masks_dir = 'static/images'

    # Create lists to hold images and masks
    images = []
    masks = []

    # Load images
    for filename in os.listdir(images_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img_path = os.path.join(images_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (256, 256))
            img = img / 255.0  # Normalize
            images.append(img)

    # Load masks
    for filename in os.listdir(masks_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            mask_path = os.path.join(masks_dir, filename)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            mask = cv2.resize(mask, (256, 256))
            mask = mask / 255.0  # Normalize
            masks.append(mask)

    # Convert lists to numpy arrays and reshape for the model
    images = np.array(images).reshape(-1, 256, 256, 1)
    masks = np.array(masks).reshape(-1, 256, 256, 1)

    return images, masks

def post_process_mask(mask):
    """
    Post-process the predicted mask.
    You can apply thresholding or morphological operations here if needed.
    """
    # Threshold the mask to convert it to binary
    _, binary_mask = cv2.threshold(mask, 0.5, 1, cv2.THRESH_BINARY)
    return binary_mask

def a_star_search(start, goal, heuristic, mask):
    """
    Implement the A* search algorithm here.
    This is a placeholder function; replace with your actual A* implementation.
    """
    # Create a simple placeholder path for demonstration purposes
    path = [start, goal]  # Replace with actual pathfinding logic
    return path

def heuristic(node, goal):
    """
    Heuristic function for A* search.
    """
    # Simple Manhattan distance
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
