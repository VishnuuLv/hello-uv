import sys
import requests

def main():
    print("Python version:", sys.version.split()[0])
    print("Interpreter:", sys.executable)
    response = requests.get("https://pypi.org/pypi/requests/json", timeout=10)
    data = response.json()
    print("Latest requests on PyPI:", data["info"]["version"])

if __name__=="__main__":
    main()