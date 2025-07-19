#!/usr/bin/env python3
"""
Детальный анализ датасетов и моделей в области информационной безопасности
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

def print_detailed_dataset_info(dataset: Dict[str, Any]) -> None:
    """Вывести детальную информацию о датасете"""
    print(f"📊 {dataset.get('id', 'N/A')}")
    print(f"   Описание: {dataset.get('description', 'N/A')[:150]}...")
    print(f"   Загрузки: {dataset.get('downloads', 0):,}")
    print(f"   Лайки: {dataset.get('likes', 0)}")
    print(f"   Размер: {dataset.get('size_categories', 'N/A')}")
    print(f"   Формат: {dataset.get('format', 'N/A')}")
    print(f"   Теги: {', '.join(dataset.get('tags', [])[:5])}")
    print()

def print_detailed_model_info(model: Dict[str, Any]) -> None:
    """Вывести детальную информацию о модели"""
    print(f"🤖 {model.get('id', 'N/A')}")
    print(f"   Описание: {model.get('description', 'N/A')[:150]}...")
    print(f"   Загрузки: {model.get('downloads', 0):,}")
    print(f"   Лайки: {model.get('likes', 0)}")
    print(f"   Теги: {', '.join(model.get('tags', [])[:5])}")
    print()

def main():
    print("🔍 ДЕТАЛЬНЫЙ АНАЛИЗ ДАТАСЕТОВ И МОДЕЛЕЙ В ОБЛАСТИ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ\n")
    
    # 1. Поиск моделей по различным запросам
    print("=" * 80)
    print("🔒 МОДЕЛИ ПО КИБЕРБЕЗОПАСНОСТИ (CYBERSECURITY)")
    print("=" * 80)
    
    cybersecurity_models = search_huggingface_models("cybersecurity", 15)
    if cybersecurity_models:
        for model in cybersecurity_models[:10]:
            print_detailed_model_info(model)
    else:
        print("Не найдено моделей по кибербезопасности")
    
    print("=" * 80)
    print("🛡️ МОДЕЛИ ПО БЕЗОПАСНОСТИ (SECURITY)")
    print("=" * 80)
    
    security_models = search_huggingface_models("security", 15)
    if security_models:
        for model in security_models[:10]:
            print_detailed_model_info(model)
    else:
        print("Не найдено моделей по безопасности")
    
    print("=" * 80)
    print("🔍 МОДЕЛИ ПО УЯЗВИМОСТЯМ (VULNERABILITY)")
    print("=" * 80)
    
    vuln_models = search_huggingface_models("vulnerability", 15)
    if vuln_models:
        for model in vuln_models[:10]:
            print_detailed_model_info(model)
    else:
        print("Не найдено моделей по уязвимостям")
    
    # 2. Поиск датасетов по различным запросам
    print("=" * 80)
    print("🛡️ ДАТАСЕТЫ ПО КИБЕРБЕЗОПАСНОСТИ (CYBERSECURITY)")
    print("=" * 80)
    
    cybersec_datasets = search_huggingface_datasets("cybersecurity", 15)
    if cybersec_datasets:
        for dataset in cybersec_datasets[:10]:
            print_detailed_dataset_info(dataset)
    else:
        print("Не найдено датасетов по кибербезопасности")
    
    print("=" * 80)
    print("🔒 ДАТАСЕТЫ ПО БЕЗОПАСНОСТИ (SECURITY)")
    print("=" * 80)
    
    security_datasets = search_huggingface_datasets("security", 15)
    if security_datasets:
        for dataset in security_datasets[:10]:
            print_detailed_dataset_info(dataset)
    else:
        print("Не найдено датасетов по безопасности")
    
    # 3. Поиск по специфическим темам
    print("=" * 80)
    print("💻 ДАТАСЕТЫ ПО БЕЗОПАСНОСТИ КОДА (CODE SECURITY)")
    print("=" * 80)
    
    code_security_datasets = search_huggingface_datasets("code security OR secure coding", 10)
    if code_security_datasets:
        for dataset in code_security_datasets[:8]:
            print_detailed_dataset_info(dataset)
    else:
        print("Не найдено датасетов по безопасности кода")
    
    print("=" * 80)
    print("🔐 ДАТАСЕТЫ ПО МАЛВАРИ (MALWARE)")
    print("=" * 80)
    
    malware_datasets = search_huggingface_datasets("malware", 10)
    if malware_datasets:
        for dataset in malware_datasets[:8]:
            print_detailed_dataset_info(dataset)
    else:
        print("Не найдено датасетов по малвари")
    
    print("=" * 80)
    print("🌐 ДАТАСЕТЫ ПО СЕТЕВОЙ БЕЗОПАСНОСТИ (NETWORK SECURITY)")
    print("=" * 80)
    
    network_security_datasets = search_huggingface_datasets("network security", 10)
    if network_security_datasets:
        for dataset in network_security_datasets[:8]:
            print_detailed_dataset_info(dataset)
    else:
        print("Не найдено датасетов по сетевой безопасности")

if __name__ == "__main__":
    main()