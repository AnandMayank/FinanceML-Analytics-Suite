#!/usr/bin/env python3
"""
Setup script for FinanceML Analytics Suite
"""

import os
import sys
from pathlib import Path

def create_directories():
    """Create necessary directories for the project"""
    directories = [
        'src',
        'notebooks', 
        'models',
        'data',
        'docs',
        'tests',
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_requirements():
    """Check if requirements.txt exists and install dependencies"""
    if Path('requirements.txt').exists():
        print("✓ Found requirements.txt")
        print("Run: pip install -r requirements.txt")
    else:
        print("⚠ requirements.txt not found")

def check_env_file():
    """Check for environment configuration"""
    if Path('.env').exists():
        print("✓ Found .env file")
    elif Path('.env.example').exists():
        print("⚠ Copy .env.example to .env and add your API keys")
    else:
        print("⚠ No environment configuration found")

def main():
    """Main setup function"""
    print("🚀 Setting up FinanceML Analytics Suite...")
    print("=" * 50)
    
    create_directories()
    check_requirements()
    check_env_file()
    
    print("=" * 50)
    print("✅ Setup complete!")
    print("\nNext steps:")
    print("1. Copy .env.example to .env and add your API keys")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Run the chatbot: streamlit run src/main.py")
    print("4. Run the dashboard: bokeh serve src/FInancial_Dashboard.py --show")

if __name__ == "__main__":
    main()
