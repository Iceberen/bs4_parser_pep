import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT, PRETTY, FILE


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
    results_dir = BASE_DIR / 'results'
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


def control_output(results, cli_args):
    MODE_TO_OUTPUT = {
        PRETTY: lambda out_fun: pretty_output(results),
        FILE: lambda out_fun: file_output(results, cli_args),
        'default': lambda out_fun: default_output(results),
    }
    output_function = MODE_TO_OUTPUT.get(
        cli_args.output, MODE_TO_OUTPUT['default'])
    return output_function(results)
