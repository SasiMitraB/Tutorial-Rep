#!/bin/bash

# Update package lists and upgrade existing packages
sudo apt-get update && sudo apt-get upgrade -y

echo "===================================================="
echo "Updated and Upgraded the apt-get"
echo "===================================================="

# Install necessary libraries
sudo apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6
    
echo "===================================================="
echo "Nessecary Libraries have been Updated"
echo "===================================================="

# Install curl if not already installed
sudo apt-get install -y curl

echo "===================================================="
echo "curl has been installed"
echo "===================================================="

# Fetch the latest Anaconda installer URL
LATEST_URL=$(curl -s https://repo.anaconda.com/archive/ | grep -oP 'Anaconda3-\d{4}\.\d{2}-1-Linux-x86_64\.sh' | sort -V | tail -n 1 | sed 's/^/https:\/\/repo.anaconda.com\/archive\//')

echo "===================================================="
echo "Latest URL has been found"
echo "===================================================="

# Download the latest Anaconda installer
curl -O $LATEST_URL

echo "===================================================="
echo "Latest Installer File has been downloaded"
echo "===================================================="

# Extract the filename from the URL
FILENAME=$(basename $LATEST_URL)

echo "===================================================="
echo "Running the latest installer file in batch mode"
echo "===================================================="

# Run the Anaconda installer in batch mode
bash $FILENAME -b -p $HOME/anaconda3

echo "===================================================="
echo "Anaconda has been installed"
echo "===================================================="

# Initialize Anaconda (optional)
# Uncomment the next line if you want to initialize Anaconda automatically
$HOME/anaconda3/bin/conda init

# Clean up the installer
rm $FILENAME

echo "===================================================="
echo "The Installer File has been deleted"
echo "===================================================="

echo "Anaconda installation completed successfully."
