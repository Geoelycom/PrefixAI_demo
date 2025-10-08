import requests
import time
import random
import os
import sys

def simulate_high_cpu():
    """Simulate high CPU usage and fail"""
    print("🔥 Simulating high CPU usage...")
    for i in range(10000000):
        pass
    print("❌ CPU usage exceeded threshold - FAILING")
    sys.exit(1)  # This will cause the workflow to fail

def simulate_memory_leak():
    """Simulate memory leak and fail"""
    print("💾 Simulating memory leak...")
    data = []
    for i in range(100000):
        data.append("x" * 1000)
    print("❌ Memory usage exceeded threshold - FAILING")
    sys.exit(1)  # This will cause the workflow to fail

def simulate_network_timeout():
    """Simulate network timeout and fail"""
    print("🌐 Simulating network timeout...")
    try:
        requests.get('http://httpstat.us/200?sleep=30000', timeout=5)
    except requests.exceptions.Timeout:
        print("❌ Network timeout occurred - FAILING")
        sys.exit(1)  # This will cause the workflow to fail

def simulate_dependency_error():
    """Simulate dependency error and fail"""
    print("📦 Simulating dependency error...")
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        print(f"❌ Dependency check failed - FAILING")
        sys.exit(1)  # This will cause the workflow to fail
    except Exception as e:
        print(f"❌ Dependency error: {e} - FAILING")
        sys.exit(1)

def main():
    failure_type = os.getenv('FAILURE_TYPE', 'dependency')
    
    print(f"🚀 Starting demo with failure type: {failure_type}")
    
    if failure_type == 'cpu':
        simulate_high_cpu()
    elif failure_type == 'memory':
        simulate_memory_leak()
    elif failure_type == 'network':
        simulate_network_timeout()
    elif failure_type == 'dependency':
        simulate_dependency_error()
    else:
        print(f"❌ Unknown failure type: {failure_type}")
        sys.exit(1)
    
    # This line will never be reached because all functions exit with error
    print("🎉 Demo completed successfully!")

if __name__ == "__main__":
    main()