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
