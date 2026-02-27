Use this version:
🛠 Project Environment Setup Guide

This project uses a dedicated Conda environment to ensure clean dependency management and reproducibility.

Create Environment
conda create -n ai_engineer python=3.11

Activate Environment
conda activate ai_engineer

Install Jupyter Notebook
conda install notebook

Launch Jupyter
jupyter notebook

Verify Python Version
Inside Jupyter:
import sys
print(sys.version)

Expected Output:
Python 3.11.x

📌 Why Dedicated Environment?

Prevents dependency conflicts

Keeps project isolated

Ensures reproducibility

Professional AI engineering practice

