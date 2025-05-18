import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT, PRETTY, FILE, FILE_OUTPUT_DIR


def default_output(results):
    for row in results:
        print(*row)


def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    results_dir = BASE_DIR / FILE_OUTPUT_DIR
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name

    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)

    logging.info(f'Файл с результатами был сохранён: {file_path}')


MODE_TO_OUTPUT = {
    PRETTY: lambda results, cli_args: pretty_output(results),
    FILE: lambda results, cli_args: file_output(results, cli_args),
    'default': lambda results, cli_args: default_output(results),
}


def control_output(results, cli_args):
    output_function = MODE_TO_OUTPUT.get(
        cli_args.output, MODE_TO_OUTPUT['default'])
    return output_function(results, cli_args)
