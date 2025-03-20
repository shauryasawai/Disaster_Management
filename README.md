# SHELTER MAP

## Overview
**SHELTER MAP** is a web application designed to provide real-time assistance during natural disasters. It integrates data from multiple sources, including the OCHA database and satellite imagery, to offer accurate and timely information during emergencies.

## Problem Statement
Natural disasters are unpredictable and often catch people unprepared, leaving them disconnected and vulnerable. During such crises, accessing real-time information, safe evacuation routes, and emergency services is critical for survival. The common challenges include:
- Lack of real-time disaster information from reliable sources.
- Limited access to safe routes and navigation during emergencies.
- Difficulty in reaching emergency services like police, fire, and medical support.
- Inability to report incidents anonymously, which can delay critical response.

## How It Works
1. **Registration & Profile Setup**: 
   - New users are directed to a sign-up page.
   - After successful registration, users are redirected to their profile section, which gathers basic health information to create a health card (e.g., medical conditions, allergies, emergency contacts).
   
2. **Home Page & Panic Button**:
   - Users are directed to the home page upon completing their profile.
   - The home page features a **Panic Button** for real-time assistance during disasters, integrating data from multiple sources like the OCHA database.
   - User's exact location (latitude and longitude coordinates) is automatically fetched and displayed on a map.
   
3. **Safe Navigation & Incident Reporting**:
   - The system uses trained ML models (GNNs, A*, and U-Net algorithms) for image processing and pathfinding to navigate users to the safest path.
   - Users can report incidents, such as accidents, fires, or hazards, anonymously on every page.
   - Real-time updates about disaster incidents and suspicious activities are available.

4. **Emergency Services**:
   - Quick access to Police, Fire, and Ambulance services.
   - Resource information about emergency services (e.g., contact details, nearest stations).
   - Nearby hospitals' directions and contacts are accessible through maps.
   
## Market Impact
- **Improved Public Safety**: Provides real-time disaster updates, safe route navigation, and quick access to emergency services.
- **Global Applicability**: Usable in disaster-prone regions worldwide, adaptable to various languages and local needs.
- **Government & NGO Support**: Assists in coordinating faster relief efforts and efficient resource management.
- **Reduced Economic Losses**: Minimizes property damage and speeds up evacuations, reducing strain on emergency services.
- **Scalable Solution**: As climate-related disasters increase, the app can grow with more features and integrations.

## Future Plans
- **Predictive Disaster Alerts**: Integrate AI-based models to predict disasters and send early warnings to users.
- **Expanded Data Sources**: Incorporate additional real-time data from local governments, NGOs, and private sector organizations.
- **Multilingual Support**: Enable the app to support more languages for global accessibility.
- **Offline Functionality**: Develop offline capabilities for safe route navigation and emergency information when internet access is unavailable.
- **Community Reporting**: Introduce a feature for users to report real-time hazards, traffic blockages, and safe zones during disasters.
- **Integration with Wearables**: Sync with smartwatches and other wearable devices for immediate alerts and health monitoring in emergencies.

## Tech Stack
- **Frontend**: [ React, Vue.js]
- **Backend**: [ Django]
- **Machine Learning Models**: GNNs, A*, U-Net for image processing and pathfinding
- **Database**: [ PostgreSQL]
- **APIs**: OCHA database integration, real-time satellite imagery processing , NASA Satellite Imagery.

## Contributing
Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

**Developed by**  
Hounds of Justice

---


Below are the setup instructions for running both a Django backend and a React frontend for the project.

---


Prerequisites

---

Python (3.8 or higher)
Node.js (with npm)
PostgreSQL (or any other database you're using)

---

Backend: Setting Up Django Server

---


## Prerequisites

Before starting, ensure you have the following installed:

- Python (version 3.x)
- pip (Python package installer)
- virtualenv

## Installation Steps

### Step 1: Clone the Repository

Clone the Django application repository to your local machine using the following command:

```bash
git clone https://github.com/Marketscope-Dev/Resume-Parser-Data-Entry
```

### Step 2: Navigate to the Project Directory

Change into the directory of the cloned repository:

```bash
cd Resume-Parser-Data-Entry
```

### Step 3: Create a Virtual Environment

Create a virtual environment using `virtualenv`:

```bash
python -m venv my_env
```
```bash
pip install virtualenv
```
This will create a virtual environment named `my_env`.

### Step 4: Activate the Virtual Environment

Activate the virtual environment using the following command:

- On Windows:
  ```bash
  my_env\Scripts\activate
  ```
- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 5: Install Dependencies

With the virtual environment activated, install the required dependencies using `pip`:

```bash
pip install -r requirement.txt
```

This will install all the dependencies listed in the `full-requirements.txt` file.

### Step 6: Run Migrations

Apply the database migrations:

```bash
python manage.py migrate
```

### Step 7: Start the Development Server

Run the development server to start the application:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/` in your web browser.

## Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```bash
deactivate
```

## Additional Notes

- Ensure you have the latest version of `pip` by running `pip install --upgrade pip`.
- If you encounter any issues during the installation process, check the error messages for guidance and ensure all prerequisites are met.


---

Frontend: Setting Up React Server

---

# Step 1: Navigate to the frontend directory
cd frontend-react

# Step 2: Install required packages
npm install

# Step 3: Start the React development server
npm start

# The React server will be running at http://localhost:3000/

---
