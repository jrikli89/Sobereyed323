#!/usr/bin/env python3
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Import datadog
from datadog import initialize, api

# Set your API key
options = {
    'api_key':'abc123',
    'app_key':'def456'
}
initialize(**options)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('SETTINGS_FILE', 'Smodal.settings'))
    try:
        # activate the virtual environment
        activate_venv_path = "/path/to/project/venv/bin/activate_this.py"
        with open(activate_venv_path) as f:
            exec(f.read(), dict(__file__=activate_venv_path))

        # Modify the run command
        os.system("gunicorn --worker-tmp-dir /dev/shm Smodal.wsgi")

    except Exception as e:
        print(f'An error occurred while trying to run command: {e}')

        # Send an event to Datadog
        title = "Exception in manage.py"
        text = f'An error occurred while trying to run command: {e}'
        tags = ['application:Smodal', 'environment:development']
        api.Event.create(title=title, text=text, tags=tags)

        # Update the main function to handle any exceptions occurred during the execution of the new plan
        print("Execution of the plan was unsuccessful. Please review and rectify the errors.")

if __name__ == '__main__':
    main()