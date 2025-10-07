import requests
import time
import random
import os
import sys

def simulate_high_cpu():
    """Simulate high CPU usage"""
    print("🔥 Simulating high CPU usage...")
    for i in range(10000000):
        pass
    print("✅ CPU simulation complete")

def simulate_memory_leak():
    """Simulate memory leak"""
    print("💾 Simulating memory leak...")
    data = []
    for i in range(100000):
        data.append("x" * 1000)
    print("✅ Memory leak simulation complete")

def simulate_network_timeout():
    """Simulate network timeout"""
    print("🌐 Simulating network timeout...")
    try:
        requests.get('http://httpstat.us/200?sleep=30000', timeout=5)
    except requests.exceptions.Timeout:
        print("✅ Network timeout simulation complete")

def simulate_dependency_error():
    """Simulate dependency error (current behavior)"""
    print("📦 Simulating dependency error...")
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(f"✅ Bitcoin price: ${response.json()['bpi']['USD']['rate']}")

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
    
    print("🎉 Demo completed successfully!")

if __name__ == "__main__":
    main()