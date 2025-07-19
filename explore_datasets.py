#!/usr/bin/env python3
"""
Скрипт для исследования датасетов и моделей в области информационной безопасности
"""

import requests
import json
from typing import List, Dict, Any

def search_huggingface_datasets(query: str, limit: int = 50) -> List[Dict[str, Any]]:
    """Поиск датасетов на Hugging Face"""
    url = "https://huggingface.co/api/datasets"
    params = {
        "search": query,
        "limit": limit,
        "full": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка при поиске датасетов: {e}")
        return []

def search_huggingface_models(query: str, limit: int = 50) -> List[Dict[str, Any]]:
    """Поиск моделей на Hugging Face"""
    url = "https://huggingface.co/api/models"
    params = {
        "search": query,
        "limit": limit,
        "full": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка при поиске моделей: {e}")
        return []

def get_circl_datasets() -> List[Dict[str, Any]]:
    """Получить все датасеты CIRCL"""
    url = "https://huggingface.co/api/datasets"
    params = {
        "author": "CIRCL",
        "limit": 100,
        "full": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка при получении датасетов CIRCL: {e}")
        return []

def get_circl_models() -> List[Dict[str, Any]]:
    """Получить все модели CIRCL"""
    url = "https://huggingface.co/api/models"
    params = {
        "author": "CIRCL",
        "limit": 100,
        "full": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка при получении моделей CIRCL: {e}")
        return []

def print_dataset_info(dataset: Dict[str, Any]) -> None:
    """Вывести информацию о датасете"""
    print(f"📊 {dataset.get('id', 'N/A')}")
    print(f"   Описание: {dataset.get('description', 'N/A')[:100]}...")
    print(f"   Загрузки: {dataset.get('downloads', 0):,}")
    print(f"   Лайки: {dataset.get('likes', 0)}")
    print(f"   Теги: {', '.join(dataset.get('tags', []))}")
    print()

def print_model_info(model: Dict[str, Any]) -> None:
    """Вывести информацию о модели"""
    print(f"🤖 {model.get('id', 'N/A')}")
    print(f"   Описание: {model.get('description', 'N/A')[:100]}...")
    print(f"   Загрузки: {model.get('downloads', 0):,}")
    print(f"   Лайки: {model.get('likes', 0)}")
    print(f"   Теги: {', '.join(model.get('tags', []))}")
    print()

def main():
    print("🔍 Исследование датасетов и моделей в области информационной безопасности\n")
    
    # 1. Датасеты CIRCL
    print("=" * 80)
    print("📊 ДАТАСЕТЫ CIRCL")
    print("=" * 80)
    
    circl_datasets = get_circl_datasets()
    if circl_datasets:
        for dataset in circl_datasets:
            print_dataset_info(dataset)
    else:
        print("Не удалось получить датасеты CIRCL")
    
    # 2. Модели CIRCL
    print("=" * 80)
    print("🤖 МОДЕЛИ CIRCL")
    print("=" * 80)
    
    circl_models = get_circl_models()
    if circl_models:
        for model in circl_models:
            print_model_info(model)
    else:
        print("Не удалось получить модели CIRCL")
    
    # 3. Поиск датасетов по уязвимостям
    print("=" * 80)
    print("🔍 ДАТАСЕТЫ ПО УЯЗВИМОСТЯМ (VULNERABILITY)")
    print("=" * 80)
    
    vuln_datasets = search_huggingface_datasets("vulnerability", 20)
    if vuln_datasets:
        for dataset in vuln_datasets[:10]:  # Показываем первые 10
            print_dataset_info(dataset)
    else:
        print("Не удалось найти датасеты по уязвимостям")
    
    # 4. Поиск моделей по информационной безопасности
    print("=" * 80)
    print("🔒 МОДЕЛИ ПО ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ")
    print("=" * 80)
    
    security_models = search_huggingface_models("cybersecurity OR security OR vulnerability", 20)
    if security_models:
        for model in security_models[:10]:  # Показываем первые 10
            print_model_info(model)
    else:
        print("Не удалось найти модели по информационной безопасности")
    
    # 5. Поиск датасетов по кибербезопасности
    print("=" * 80)
    print("🛡️ ДАТАСЕТЫ ПО КИБЕРБЕЗОПАСНОСТИ")
    print("=" * 80)
    
    cybersec_datasets = search_huggingface_datasets("cybersecurity OR security", 20)
    if cybersec_datasets:
        for dataset in cybersec_datasets[:10]:  # Показываем первые 10
            print_dataset_info(dataset)
    else:
        print("Не удалось найти датасеты по кибербезопасности")

if __name__ == "__main__":
    main()