# 📊 Отчет по датасетам и моделям в области информационной безопасности

## 🎯 CIRCL (Computer Incident Response Center Luxembourg)

### 📊 Датасеты CIRCL

| Датасет | Описание | Загрузки | Лайки | Размер |
|---------|----------|----------|-------|--------|
| **CIRCL/vulnerability** | Основной датасет уязвимостей | 115 | 1 | 100K-1M |
| **CIRCL/vulnerability-scores** | Датасет с CVSS оценками (600K+ записей) | 432 | 4 | 100K-1M |
| **CIRCL/vulnerability-csaf-redhat** | CSAF данные Red Hat | 10 | 0 | 10K-100K |
| **CIRCL/vulnerability-csaf-cisa** | CSAF данные CISA | 20 | 0 | 1K-10K |
| **CIRCL/Vulnerability-CNVD** | Китайская база уязвимостей | 241 | 2 | 100K-1M |

### 🤖 Модели CIRCL

| Модель | Тип | Загрузки | Лайки | Описание |
|--------|-----|----------|-------|----------|
| **CIRCL/vulnerability-severity-classification-distilbert-base-uncased** | Классификация | 347 | 2 | Классификация серьезности уязвимостей |
| **CIRCL/vulnerability-severity-classification-roberta-base** | Классификация | 310 | 4 | Классификация серьезности (RoBERTa) |
| **CIRCL/vulnerability-description-generation-gpt2** | Генерация | 7 | 0 | Генерация описаний уязвимостей |
| **CIRCL/vulnerability-description-generation-gpt2-large** | Генерация | 6 | 0 | Генерация описаний (GPT-2 Large) |
| **CIRCL/vulnerability-severity-classification-chinese-macbert-base** | Классификация | 137 | 1 | Классификация для китайских уязвимостей |

---

## 🔒 Модели по кибербезопасности

### 🏆 Топ модели

| Модель | Загрузки | Лайки | Описание |
|--------|----------|-------|----------|
| **Trendyol/Trendyol-Cybersecurity-LLM-Qwen3-32B-Q8_0-GGUF** | 967 | 38 | Кибербезопасность LLM на базе Qwen3-32B |
| **segolilylabs/Lily-Cybersecurity-7B-v0.2** | 638 | 110 | Специализированная модель кибербезопасности |
| **AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF** | 358 | 58 | Offensive Security LLM |
| **QuantFactory/Lily-Cybersecurity-7B-v0.2-GGUF** | 294 | 18 | GGUF версия Lily Cybersecurity |
| **ZySec-AI/SecurityLLM** | 278 | 78 | Security LLM на базе Mistral |

### 🔍 Модели по уязвимостям

| Модель | Загрузки | Лайки | Описание |
|--------|----------|-------|----------|
| **Zaib/Vulnerability-detection** | 21 | 7 | Детекция уязвимостей |
| **jiekeshi/CodeBERT-50MB-Vulnerability-Prediction** | 0 | 2 | Предсказание уязвимостей в коде |
| **jiekeshi/CodeBERT-25MB-Vulnerability-Prediction** | 0 | 1 | Предсказание уязвимостей (25MB) |
| **jiekeshi/GraphCodeBERT-50MB-Vulnerability-Prediction** | 0 | 0 | GraphCodeBERT для уязвимостей |

---

## 📊 Датасеты по уязвимостям

### 🏆 Популярные датасеты

| Датасет | Загрузки | Лайки | Описание |
|---------|----------|-------|----------|
| **CyberNative/Code_Vulnerability_Security_DPO** | 1,094 | 109 | Уязвимости в коде с DPO |
| **msc-smart-contract-auditing/vulnerability-severity-classification** | 133 | 3 | Классификация уязвимостей смарт-контрактов |
| **Zaib/java-vulnerability** | 89 | 7 | Уязвимости в Java коде |
| **ArmurAI/Solana_vulnerability_audit_dataset_V2** | 32 | 2 | Аудит уязвимостей Solana |

---

## 🛡️ Датасеты по кибербезопасности

### 🏆 Топ датасеты

| Датасет | Загрузки | Лайки | Описание |
|---------|----------|-------|----------|
| **clydeiii/cybersecurity** | 2,539 | 2 | APTnotes корпус |
| **Vanessasml/cybersecurity_32k_instruction_input_output** | 110 | 15 | 32K инструкций по кибербезопасности |
| **zeroshot/cybersecurity-corpus** | 210 | 8 | Корпус кибербезопасности |
| **schooly/Cyber-Security-Breaches** | 36 | 11 | Нарушения кибербезопасности |
| **bnsapa/cybersecurity-ner** | 87 | 2 | NER для кибербезопасности |

---

## 🔐 Датасеты по малвари

| Датасет | Загрузки | Лайки | Описание |
|---------|----------|-------|----------|
| **cw1521/ember2018-malware** | 541 | 8 | EMBER 2018 - 1M записей малвари |
| **PurCL/malware-top-100** | 115 | 2 | Топ-100 малвари |
| **naorm/malware-text-db** | 55 | 2 | Текстовая база малвари |
| **naorm/malware-text-db-cyner** | 18 | 1 | Малвари с Cyner анализом |

---

## 🌐 Сетевая безопасность

| Датасет | Загрузки | Лайки | Описание |
|---------|----------|-------|----------|
| **James4Ever0/network_security_questions** | 40 | 9 | Вопросы по сетевой безопасности |

---

## 💡 Рекомендации по использованию

### 🎯 Для анализа уязвимостей:
1. **CIRCL/vulnerability-scores** - основной датасет с CVSS оценками
2. **CIRCL/vulnerability-severity-classification-distilbert-base-uncased** - модель классификации
3. **CyberNative/Code_Vulnerability_Security_DPO** - для анализа кода

### 🔒 Для кибербезопасности:
1. **segolilylabs/Lily-Cybersecurity-7B-v0.2** - специализированная модель
2. **clydeiii/cybersecurity** - большой корпус данных
3. **Vanessasml/cybersecurity_32k_instruction_input_output** - инструкции

### 🔐 Для анализа малвари:
1. **cw1521/ember2018-malware** - крупнейший датасет малвари
2. **PurCL/malware-top-100** - топ малвари

### 🚀 Для создания собственных моделей:
1. Используйте VulnTrain для создания датасетов
2. Обучайте на базе существующих моделей CIRCL
3. Применяйте специализированные модели для конкретных задач

---

## 📈 Статистика

- **Всего датасетов CIRCL**: 5
- **Всего моделей CIRCL**: 5
- **Популярные модели кибербезопасности**: 10+
- **Датасеты по уязвимостям**: 10+
- **Датасеты по малвари**: 8
- **Общий объем данных**: 1M+ записей

---

## 🔗 Полезные ссылки

- [CIRCL на Hugging Face](https://huggingface.co/CIRCL)
- [VulnTrain GitHub](https://github.com/vulnerability-lookup/VulnTrain)
- [Vulnerability-Lookup](https://www.vulnerability-lookup.org/)
- [Hugging Face Security Models](https://huggingface.co/models?search=security)
- [Hugging Face Cybersecurity Datasets](https://huggingface.co/datasets?search=cybersecurity)