# TikTok to YouTube Shorts Automation

## Overview
This project automates the process of identifying popular TikTok videos, downloading them, generating autogenrated commentary, and posting them on YouTube Shorts. The entire workflow is orchestrated using serverless GCP services including Cloud Functions, Cloud Run, and Pub/Sub.

## Features
- Identifies popular TikTok videos.
- Downloads the identified videos.
- Generates autogenrated commentary for the downloaded videos.
- Posts the videos with commentary on YouTube Shorts.

## Components
1. **TikTok Video Identification**
  - Fetches popular TikTok videos.

2. **Video Download**
  - Transfers the fetched videos to a designated GCP bucket for further processing.

3. **Commentary Generation**
  - Utilizes NLP techniques to generate autogenrated commentary for the downloaded videos.

4. **YouTube Shorts Posting**
  - Uses Google Cloud Vision API to post the videos with commentary on YouTube Shorts.

## Technologies Used
- **Google Cloud Platform (GCP) Services**:
 - Cloud Functions: Orchestrating the workflow.
 - Cloud Run: Running serverless containers for specific tasks.
 - Pub/Sub: Messaging service for communication between components.
 - Cloud Storage: Storing videos in GCP buckets.
 - Cloud Vision API: Posting videos on YouTube Shorts.
 - NLP Libraries: Generating commentary for the videos.

## Usage
- Configure the system to fetch popular TikTok videos periodically.
- Access the YouTube Shorts to view the posted videos with autogenrated commentary.

## Contributors
- oswald

## License
Distributed under the MIT License. See `LICENSE` for more information.
