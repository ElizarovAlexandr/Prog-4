"""Тесты для лабораторной работы с паттерном «Декоратор»."""

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

from main import Component, CsvDecorator, JsonDecorator, YamlDecorator


class FakeCurrencyComponent(Component):
    """Тестовый компонент без обращения к интернету."""

    def operation(self) -> dict[str, Any]:
        """Возвращает тестовые данные валют."""
        return {
            "Date": "2024-01-01",
            "Valute": {
                "USD": {
                    "Name": "Доллар США",
                    "Nominal": 1,
                    "Value": 90.0,
                    "Previous": 89.5,
                },
                "EUR": {
                    "Name": "Евро",
                    "Nominal": 1,
                    "Value": 100.0,
                    "Previous": 99.5,
                },
            },
        }


class TestJsonDecorator(unittest.TestCase):
    """Тесты JSON-декоратора."""

    def test_json_operation(self) -> None:
        """Проверяет преобразование данных в JSON."""
        result = JsonDecorator(FakeCurrencyComponent()).operation()
        data = json.loads(result)
        self.assertEqual(data["Valute"]["USD"]["Name"], "Доллар США")

    def test_json_save_to_file(self) -> None:
        """Проверяет сохранение JSON в файл."""
        decorator = JsonDecorator(FakeCurrencyComponent())

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "data.json"
            decorator.save_to_file(str(path))
            self.assertTrue(path.exists())


class TestYamlDecorator(unittest.TestCase):
    """Тесты YAML-декоратора."""

    def test_yaml_operation(self) -> None:
        """Проверяет преобразование данных в YAML."""
        result = YamlDecorator(FakeCurrencyComponent()).operation()
        data = yaml.safe_load(result)
        self.assertEqual(data["Valute"]["EUR"]["Name"], "Евро")

    def test_yaml_save_to_file(self) -> None:
        """Проверяет сохранение YAML в файл."""
        decorator = YamlDecorator(FakeCurrencyComponent())

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "data.yaml"
            decorator.save_to_file(str(path))
            self.assertTrue(path.exists())


class TestCsvDecorator(unittest.TestCase):
    """Тесты CSV-декоратора."""

    def test_csv_operation(self) -> None:
        """Проверяет преобразование данных в CSV."""
        result = CsvDecorator(FakeCurrencyComponent()).operation()
        self.assertIn("USD", result)
        self.assertIn("Доллар США", result)

    def test_csv_save_to_file(self) -> None:
        """Проверяет сохранение CSV в файл."""
        decorator = CsvDecorator(FakeCurrencyComponent())

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "data.csv"
            decorator.save_to_file(str(path))
            self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()