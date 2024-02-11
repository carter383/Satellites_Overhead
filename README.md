Satellite Overhead Notifier
===========================

Overview
--------

The Satellite Overhead Notifier is a Python application designed to notify users when a satellite is overhead based on their geographical location. This tool uses TLE (Two-Line Element set) data from [Space-Track.org](https://www.space-track.org/) to track satellites in real-time. Whether you're an astronomy enthusiast, a researcher, or someone curious about satellites crossing your sky, this project provides a simple yet effective way to stay informed.

Features
--------

-   Real-time Satellite Tracking: Utilizes up-to-date TLE data from Space-Track.org to monitor satellite positions.
-   Customizable Notification Radius: Set a specific radius in miles within which you want to be notified about overhead satellites.
-   Console Notifications: Receive immediate notifications in your console when a satellite is overhead.
-   Easy Configuration: Simple `config.yaml` setup for personalization.

Upcoming Features
-----------------

-   User Interface: Develop a user-friendly interface for easier management of settings and viewing of overhead satellites.
-   Community Features: Share sightings and track satellites of interest as a community.

Prerequisites
-------------

Before you begin, ensure you have the following:

-   Python 3.x installed on your machine.
-   A registered account on [Space-Track.org](https://www.space-track.org/) for accessing TLE data.

Installation
------------

1.  Clone the repository to your local machine:

    bashCopy code

    `git clone https://github.com/carter383/Satellites_Overhead.git`

2.  Navigate to the project directory:

    bashCopy code

    `cd satellite-overhead-notifier`

3.  Install the required Python packages:

    bashCopy code

    `pip install -r requirements.txt`

Configuration
-------------

1.  Copy `config_example.yaml` to `config.yaml`:

    bashCopy code

    `cp config_example.yaml config.yaml`

2.  Edit `config.yaml` with your preferred text editor and update the following fields:
    -   `username`: Your Space-Track.org username.
    -   `password`: Your Space-Track.org password.
    -   `lat`: Your latitude.
    -   `lon`: Your longitude.
    -   `within_miles`: The radius in miles within which you want to be notified about overhead satellites.

Usage
-----

To start tracking satellites and receive notifications, run the following command in your terminal:

bashCopy code

`python notify.py`

The script will continuously monitor for satellites overhead based on your configured settings and print notifications to the console.

Contributing
------------

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
---------------

-   Thanks to [Space-Track.org](https://www.space-track.org/) for providing the TLE data used in this project.
