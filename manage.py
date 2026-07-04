#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except Exception as e:
        import traceback
        print("\n" + "=" * 50)
        print("!!! КРИТИЧЕСКАЯ ОШИБКА ДЕПЛОЯ ИМЕННО ТУТ !!!")
        print(f"Тип ошибки: {type(e).__name__}")
        print(f"Описание ошибки: {e}")
        print("=" * 50 + "\n")
        raise e


if __name__ == '__main__':
    main()
