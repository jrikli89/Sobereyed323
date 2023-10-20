#!/usr/bin/env python3.11.4
"""
Django's command-line utility for administrative tasks.
This script is the entry point for running the Django application and handling essential tasks such as migrations.
"""
import os
import sys
from django.core.management import execute_from_command_line

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Smodal.settings')
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f'An error occurred in main: {e}')

if __name__ == '__main__':
    main()