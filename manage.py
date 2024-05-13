#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""Утилита командной строки Django для административных задач."""
import os
import sys


def main():
    """Run administrative tasks."""
    """Запустить административные задачи."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            "Не удалось импортировать Django. Вы уверены, что он установлен и "
            "доступен в переменной окружения PYTHONPATH? Возможно, вы забыли "
            "активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()