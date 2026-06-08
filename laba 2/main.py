"""Реализация паттерна «Декоратор» для курсов валют ЦБ РФ."""

import csv
import io
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import requests
import yaml


class Component(ABC):
    """Абстрактный интерфейс компонента."""

    @abstractmethod
    def operation(self) -> Any:
        """Возвращает данные компонента."""


class SaveMixin(ABC):
    """Интерфейс для сохранения данных в файл."""

    @abstractmethod
    def save_to_file(self, filename: str) -> None:
        """Сохраняет результат работы в файл."""


class CurrencyComponent(Component):
    """Компонент, получающий курсы валют с сайта ЦБ РФ."""

    URL = "https://www.cbr-xml-daily.ru/daily_json.js"

    def operation(self) -> dict[str, Any]:
        """Получает данные о курсах валют в виде словаря."""
        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()
        return response.json()


class Decorator(Component):
    """Базовый класс декоратора."""

    def __init__(self, component: Component) -> None:
        """Инициализирует декоратор."""
        self._component = component

    @property
    def component(self) -> Component:
        """Возвращает оборачиваемый компонент."""
        return self._component

    def operation(self) -> Any:
        """Делегирует выполнение операции компоненту."""
        return self.component.operation()


class JsonDecorator(Decorator, SaveMixin):
    """Декоратор для преобразования данных в JSON."""

    def operation(self) -> str:
        """Возвращает данные в формате JSON."""
        data = super().operation()
        return json.dumps(data, ensure_ascii=False, indent=4)

    def save_to_file(self, filename: str) -> None:
        """Сохраняет JSON-данные в файл."""
        Path(filename).write_text(self.operation(), encoding="utf-8")


class YamlDecorator(Decorator, SaveMixin):
    """Декоратор для преобразования данных в YAML."""

    def operation(self) -> str:
        """Возвращает данные в формате YAML."""
        data = super().operation()
        return yaml.safe_dump(data, allow_unicode=True, sort_keys=False)

    def save_to_file(self, filename: str) -> None:
        """Сохраняет YAML-данные в файл."""
        Path(filename).write_text(self.operation(), encoding="utf-8")


class CsvDecorator(Decorator, SaveMixin):
    """Декоратор для преобразования данных в CSV."""

    def operation(self) -> str:
        """Возвращает данные о валютах в формате CSV."""
        data = super().operation()
        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(["code", "name", "nominal", "value", "previous"])

        for code, currency in data.get("Valute", {}).items():
            writer.writerow(
                [
                    code,
                    currency.get("Name", ""),
                    currency.get("Nominal", ""),
                    currency.get("Value", ""),
                    currency.get("Previous", ""),
                ]
            )

        return output.getvalue()

    def save_to_file(self, filename: str) -> None:
        """Сохраняет CSV-данные в файл."""
        Path(filename).write_text(self.operation(), encoding="utf-8")


def client_code(component: Component) -> None:
    """Клиентский код, работающий через общий интерфейс Component."""
    print(component.operation())


if __name__ == "__main__":
    source = CurrencyComponent()

    json_data = JsonDecorator(source)
    yaml_data = YamlDecorator(source)
    csv_data = CsvDecorator(source)

    client_code(json_data)
    client_code(yaml_data)
    client_code(csv_data)

    json_data.save_to_file("currencies.json")
    yaml_data.save_to_file("currencies.yaml")
    csv_data.save_to_file("currencies.csv")