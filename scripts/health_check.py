#!/usr/bin/env python3
"""
Container health check script
"""

import requests
import time
import sys

def check_api_health():
    """Check if API is healthy"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Main health check"""
    max_attempts = 10
    for attempt in range(max_attempts):
        if check_api_health():
            print("✅ API is healthy!")
            sys.exit(0)
        else:
            print(f"⏳ Waiting for API... (attempt {attempt + 1}/{max_attempts})")
            time.sleep(5)
    
    print("❌ API health check failed!")
    sys.exit(1)

if __name__ == "__main__":
    main()
