#!/usr/bin/env python3
"""
Test script to verify the RAG solution setup
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is 3.8+"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    print(f"✅ Python {sys.version.split()[0]} found")
    return True

def check_ollama():
    """Check if Ollama is installed and running"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ollama is installed and running")
            
            # Check for required models
            models = result.stdout
            if 'bge-m3' in models:
                print("✅ BGE-M3 embedding model found")
            else:
                print("⚠️  BGE-M3 model not found - run: ollama pull bge-m3:latest")
            
            if 'gemma2:2b' in models:
                print("✅ Gemma2:2b generation model found")
            else:
                print("⚠️  Gemma2:2b model not found - run: ollama pull gemma2:2b")
            
            return True
    except FileNotFoundError:
        print("❌ Ollama not found - install from https://ollama.ai")
        return False
    except Exception as e:
        print(f"❌ Error checking Ollama: {e}")
        return False

def check_node():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Node.js {version} found")
            return True
    except FileNotFoundError:
        print("❌ Node.js not found - install from https://nodejs.org")
        return False
    except Exception as e:
        print(f"❌ Error checking Node.js: {e}")
        return False

def check_python_packages():
    """Check if required Python packages can be imported"""
    required_packages = [
        'fastapi',
        'uvicorn',
        'pydantic',
        'chromadb',
        'sentence_transformers',
        'ollama'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'sentence_transformers':
                import sentence_transformers
            else:
                importlib.import_module(package)
            print(f"✅ {package} available")
        except ImportError:
            print(f"❌ {package} not found")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Install missing packages:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True

def main():
    print("🔍 Testing RAG Solution Setup...\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Ollama Installation", check_ollama),
        ("Node.js Installation", check_node),
        ("Python Packages", check_python_packages)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n--- {name} ---")
        results.append(check_func())
    
    print("\n" + "="*50)
    if all(results):
        print("🎉 All checks passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Run: ./start.sh")
        print("2. Open: http://localhost:3000")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nRun the setup script: ./setup.sh")

if __name__ == "__main__":
    main()
