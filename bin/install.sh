#!/bin/bash


#############################
# TO RUN USE THE FOLLOWING
#############################
# source ./install.sh 
#############################


# Create Conda environment
conda create --name condaScripts python=3.8

# Initialize Conda (required before activating environments)
conda init

# Activate Conda environment
source activate condaScripts

# Install dependencies
pip install argparse pyinputplus dnspython requests scapy beautifulsoup4
echo "Dependencies installed successfully."
echo "Conda environment created and activated."

setup_local_bin() {
    local_bin_dir="$HOME/.local/bin"
    if [ ! -d "$local_bin_dir" ]; then
        mkdir -p "$local_bin_dir"
        echo "Created local bin directory: $local_bin_dir"
    fi
}

pip install -r requirements.txt
pip install lxml
chmod -R +rwx ../dotfiles

source /root/miniconda3/etc/profile.d/conda.sh
conda activate condaScripts
