import os
import subprocess

def update_package(package_name):
    """Updates the specified package using pip."""
    try:
        subprocess.check_call(['pip', 'install', '--upgrade', package_name])
        print(f"Package '{package_name}' updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating package '{package_name}': {e}")
    except FileNotFoundError:
        print("Error: pip command not found. Ensure pip is installed and in your PATH.")


def update_requirements(requirements_file="requirements.txt"):
    """Updates all packages listed in the requirements file."""
    if not os.path.exists(requirements_file):
        print(f"Error: Requirements file '{requirements_file}' not found.")
        return

    try:
        with open(requirements_file, 'r') as f:
            packages = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        for package in packages:
            update_package(package)

    except Exception as e:
        print(f"An error occurred while processing the requirements file: {e}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Update Python packages.")
    parser.add_argument("-r", "--requirements", help="Path to requirements.txt file", default="requirements.txt")
    parser.add_argument("-p", "--package", help="Specific package to update")
    args = parser.parse_args()

    if args.package:
        update_package(args.package)
    elif args.requirements:
        update_requirements(args.requirements)
    else:
        print("Please specify either a package name (-p) or a requirements file (-r).")
