import argparse
import json
import sys
from pathlib import Path
from .core import find_paths

def main():
    parser = argparse.ArgumentParser(description="🔍 JSON Path Finder - Find keys or values in deep JSON.")
    parser.add_argument("file", help="Path to JSON file")
    parser.add_argument("--key", "-k", help="Search by key name")
    parser.add_argument("--value", "-v", help="Search by value")
    
    args = parser.parse_args()

    if not args.key and not args.value:
        print("❌ Error: You must specify either --key or --value")
        sys.exit(1)

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ Error: File '{file_path}' not found.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON file.")
        sys.exit(1)

    target = args.key if args.key else args.value
    mode = 'key' if args.key else 'value'

    print(f"🔎 Searching for {mode}: '{target}'...")
    results = find_paths(data, target, mode)

    if results:
        print(f"✅ Found {len(results)} matches:")
        for path in results:
            print(f"   {path}")
    else:
        print("🤷‍♂️ Nothing found.")

if __name__ == "__main__":
    main()