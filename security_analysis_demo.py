#!/usr/bin/env python3
"""
Демонстрационный скрипт анализа датасетов и моделей информационной безопасности
Безопасная версия без секретов
"""

import json
from typing import List, Dict, Any

def load_security_summary():
    """Загрузка сводки по безопасности"""
    try:
        with open('security_datasets_summary.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def print_summary():
    """Вывод сводки результатов"""
    data = load_security_summary()
    if not data:
        print("❌ Файл security_datasets_summary.json не найден")
        return
    
    print("🔍 АНАЛИЗ ДАТАСЕТОВ И МОДЕЛЕЙ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ")
    print("=" * 70)
    
    summary = data['summary']
    print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
    print(f"   📈 Всего датасетов: {summary['total_datasets']:,}")
    print(f"   🤖 Всего моделей: {summary['total_models']:,}")
    print(f"   🔒 Релевантных датасетов: {summary['security_datasets']:,}")
    print(f"   🛡️ Релевантных моделей: {summary['security_models']:,}")
    print(f"   📅 Дата поиска: {summary['search_date']}")
    
    print(f"\n📊 КАТЕГОРИИ ДАТАСЕТОВ:")
    for category, count in data['categories']['datasets'].items():
        print(f"   {category.replace('_', ' ').title()}: {count}")
    
    print(f"\n🤖 КАТЕГОРИИ МОДЕЛЕЙ:")
    for category, count in data['categories']['models'].items():
        print(f"   {category.replace('_', ' ').title()}: {count}")
    
    print(f"\n🏆 ТОП ДАТАСЕТЫ ПО КАТЕГОРИЯМ:")
    for category, datasets in data['top_datasets'].items():
        print(f"\n   {category.replace('_', ' ').upper()}:")
        for i, dataset in enumerate(datasets[:5], 1):
            print(f"     {i}. {dataset}")
    
    print(f"\n🤖 ТОП МОДЕЛИ ПО КАТЕГОРИЯМ:")
    for category, models in data['top_models'].items():
        print(f"\n   {category.replace('_', ' ').upper()}:")
        for i, model in enumerate(models[:5], 1):
            print(f"     {i}. {model}")
    
    print(f"\n🎯 РЕСУРСЫ CIRCL:")
    print(f"   📊 Датасеты:")
    for dataset in data['circl_resources']['datasets']:
        print(f"     - {dataset}")
    
    print(f"   🤖 Модели:")
    for model in data['circl_resources']['models']:
        print(f"     - {model}")

def print_download_commands():
    """Вывод команд для загрузки"""
    data = load_security_summary()
    if not data:
        return
    
    print(f"\n📥 КОМАНДЫ ДЛЯ ЗАГРУЗКИ:")
    print(f"\n🔒 ТОП ДАТАСЕТЫ CIRCL:")
    for dataset in data['circl_resources']['datasets']:
        print(f"huggingface-cli download {dataset}")
    
    print(f"\n🤖 ТОП МОДЕЛИ БЕЗОПАСНОСТИ:")
    for model in data['top_models']['generation'][:3]:
        print(f"huggingface-cli download {model}")

def main():
    """Основная функция"""
    print_summary()
    print_download_commands()
    
    print(f"\n💡 ИСПОЛЬЗОВАНИЕ:")
    print(f"   📖 Подробный отчет: final_security_report.md")
    print(f"   📋 Краткий обзор: top10_summary.md")
    print(f"   📚 Полная документация: SECURITY_ANALYSIS_README.md")
    print(f"   🔧 VulnTrain команды:")
    print(f"      pip install vulntrain[all]")
    print(f"      vulntrain-dataset-generation --sources cvelistv5,ghsa --nb-rows 1000000")

if __name__ == "__main__":
    main()