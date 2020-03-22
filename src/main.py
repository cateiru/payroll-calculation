'''
main.
'''
import click


@click.command()
@click.option('--hourly-wage', 'hourly_wage', prompt=True, type=int, help='hourly wage.')
@click.option('--payday', 'payday', prompt=True, type=int, help='payday (date).')
@click.option('--payday-details', 'payday_details',
              prompt=True, is_flag=True, default=False, help='Detailed payday settings (such as holiday payments).')
@click.option('--google-calendar', 'google_calendar',
              type=click.Path(exists=True), prompt=True, help='JSON file for Google Calendar authentication.')
@click.option('--slack-webhook', 'slack_webhook', prompt=True, hide_input=True)
def main(hourly_wage: int, payday: int, payday_details: bool, google_calendar: str, slack_webhook: str):
    select_payday_holiday(payday_details)


def select_payday_holiday(payday_details: int) -> int:
    '''
    給料日が休日だった場合にいつ支払いするのかを設定します。
    1. 休日の前払い
    2. 休日の後払い
    3. デフォルト(休日に支払う) -> 0に変更する

    Args:
        payday_details (int): 詳細設定をするか。Trueの場合する。

    Returns:
        int: 上記説明通り。`payday_details`がFalseの場合は0を返す。
    '''
    holiday_payments = 0
    if payday_details:
        payday_details_select_doc = ['Please choose a number.',
                                     '1. If the payday is a holiday, pay faster than expected.',
                                     '2. If the payday is a holiday, pay later than expected.',
                                     '3. Default.', '']
        payday_details_select_doc = '\n'.join(payday_details_select_doc)
        holiday_payments = click.prompt(payday_details_select_doc, type=int)
        if holiday_payments == 3:
            holiday_payments = 0
    else:
        holiday_payments = 0

    return holiday_payments


if __name__ == "__main__":
    main()
