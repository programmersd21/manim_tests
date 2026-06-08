#!/usr/bin/env bash

set -e

echo "=== 1. Updating system package lists ==="
sudo apt update

echo "=== 2. Installing Manim system dependencies and LaTeX ==="
sudo apt install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    pkg-config \
    ffmpeg \
    libcairo2-dev \
    libpango1.0-dev \
    texlive \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-latex-recommended \
    texlive-science \
    tipa

echo "=== 3. Creating Python Virtual Environment ==="
python3 -m venv ~/manim-env

echo "=== 4. Upgrading Core Pip Packages inside Environment ==="
~/manim-env/bin/pip install -U pip setuptools wheel

echo "=== 5. Installing Manim ==="
~/manim-env/bin/pip install manim

echo "=== 6. Verifying Installation ==="
~/manim-env/bin/manim --version

echo
echo "===================================================="
echo "Setup complete!"
echo
echo "To start using Manim:"
echo "source ~/manim-env/bin/activate"
echo "===================================================="
