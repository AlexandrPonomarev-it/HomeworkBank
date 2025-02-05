from src.open_csv_excel_file import read_csv_file, read_excel_file
from src.processing import date_changing, filter_by_state, sort_by_date, sort_by_sum_of_operation
from src.transaction_search import search_for_a_transaction_by_keyword
from src.utils import get_financial_transactions
from src.widget import mask_account_card


def main() -> list:
    """Функция обрабатывает файлы различных категорий и фильтрует содержащиеся в них
    транзакции по нескольким показателям и возвращает отфильтрованный список транзакций"""
    transactions_sorted_list = []
    operations_list_result = []
    operation_list_conclusion = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        choosing_an_operation = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
            "Ввод: "
        )

        if choosing_an_operation == "1":
            transactions_sorted_list = get_financial_transactions("data/operations.json")
            print("Для обработки выбран JSON-файл")
            break
        elif choosing_an_operation == "2":
            transactions_sorted_list = read_csv_file("transactions.csv")
            print("Для обработки выбран CSV-файл")
            break
        elif choosing_an_operation == "3":
            transactions_sorted_list = read_excel_file("transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл")
            break
        else:
            print("Введены некорректные данные")
            continue

    while True:
        choosing_an_state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"
            "Ввод: "
        )

        if choosing_an_state.upper() == "EXECUTED":
            transactions_sorted_list = filter_by_state(transactions_sorted_list, "EXECUTED")
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            break
        elif choosing_an_state.upper() == "CANCELED":
            transactions_sorted_list = filter_by_state(transactions_sorted_list, "CANCELED")
            print("Операции отфильтрованы по статусу 'CANCELED'")
            break
        elif choosing_an_state.upper() == "PENDING":
            transactions_sorted_list = filter_by_state(transactions_sorted_list, "PENDING")
            print("Операции отфильтрованы по статусу 'PENDING")
            break
        else:
            print(f"Статус операции {choosing_an_state} недоступен")
            continue

    while True:
        sort_date_input = input("Отсортировать операции по дате? Да/Нет ")
        if sort_date_input.lower() == "да":
            transactions_sorted_list = sort_by_date(transactions_sorted_list)
            break
        elif sort_date_input.lower() == "нет":
            transactions_sorted_list = transactions_sorted_list
            break
        else:
            print(f"Сортировка по {sort_date_input} недоступна")
            continue

    while True:
        sort_ascending_or_descending_input = input("Отсортировать по возрастанию или по убыванию?  ")
        transactions_sorted_list = sort_by_sum_of_operation(transactions_sorted_list)
        if sort_ascending_or_descending_input.lower() == "по возрастанию":
            sort_by_sum_of_operation(transactions_sorted_list)
            break
        elif sort_ascending_or_descending_input.lower() == "по убыванию":
            sort_by_sum_of_operation(transactions_sorted_list, False)
            break
        else:
            print(f"Сортировка по {sort_ascending_or_descending_input} недоступна")
            continue

    while True:
        only_rub_transactions_input = input("Выводить только рублевые транзакции? Да/Нет ")
        if only_rub_transactions_input.lower() == "да":
            transactions_sorted_list_rub = []
            for act in transactions_sorted_list:
                if act["operationAmount"]["currency"]["code"] == "RUB":
                    transactions_sorted_list_rub.append(act)
                    transactions_sorted_list = transactions_sorted_list_rub
            break
        elif only_rub_transactions_input.lower() == "нет":
            transactions_sorted_list = transactions_sorted_list
            break
        else:
            print(f"Ответ {only_rub_transactions_input} недоступен")
            continue

    while True:
        filter_word_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
        if filter_word_input.lower() == "да":
            search_string = input("Введите слово для фильтрации транзакций: ")
            transactions_sorted_list = search_for_a_transaction_by_keyword(transactions_sorted_list, search_string)
            break
        elif filter_word_input.lower() == "нет":
            transactions_sorted_list = transactions_sorted_list
            break
        else:
            print(f"Ответ {filter_word_input} недоступен")
            continue

    for transactions in transactions_sorted_list:
        if "from" in transactions:
            operations_list_result.append(
                [
                    transactions["date"],
                    transactions["description"],
                    transactions["from"],
                    transactions["to"],
                    transactions["operationAmount"]["amount"],
                    transactions["operationAmount"]["currency"]["name"],
                ]
            )
        else:
            operations_list_result.append(
                [
                    transactions["date"],
                    transactions["description"],
                    transactions["to"],
                    transactions["operationAmount"]["amount"],
                    transactions["operationAmount"]["currency"]["name"],
                ]
            )

    for operation in operations_list_result:

        if len(operation) == 6:
            operation_list_conclusion.append(
                f"{date_changing(operation[0][:10])} {operation[1]}\n"
                f"{mask_account_card(operation[2])} -> {mask_account_card(operation[3])}\n"
                f"Сумма: {operation[4]} {operation[5]}"
            )
        else:
            operation_list_conclusion.append(
                f"{date_changing(operation[0][:10])} {operation[1]}\n"
                f"{mask_account_card(operation[2])}\n"
                f"Сумма: {operation[3]} {operation[4]}"
            )

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions_sorted_list)}")
    if len(transactions_sorted_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []
    return operation_list_conclusion


if __name__ == "__main__":
    for i in main():
        print(i)
