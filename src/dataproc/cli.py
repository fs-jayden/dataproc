"""dataproc CLI 진입점."""

import logging
import sys

import click

from dataproc import str_to_datetime, str_to_unixtime

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """dataproc: datetime 문자열 변환 CLI 도구."""
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)


@cli.command(name="to-unixtime")
@click.argument("date_string")
def to_unixtime_cmd(date_string):
    """datetime 문자열을 unix timestamp (microseconds) 로 변환한다.

    \b
    사용 예시:
        dataproc to-unixtime "2024-05-01T10:30:00"
        dataproc to-unixtime "01/05/24 10:30:00"
    """
    logger.info(f"Converting {date_string!r} to unix timestamp")
    try:
        result = str_to_unixtime(date_string)
        click.echo(result)
    except ValueError as e:
        raise click.ClickException(str(e))


@cli.command(name="to-datetime")
@click.argument("date_string")
def to_datetime_cmd(date_string):
    """datetime 문자열을 ISO 8601 포맷으로 정규화한다.

    \b
    사용 예시:
        dataproc to-datetime "01/05/24 10:30:00"
        dataproc to-datetime "2024-05-01T10:30:00.123456"
    """
    logger.info(f"Converting {date_string!r} to ISO datetime")
    try:
        result = str_to_datetime(date_string)
        click.echo(result.isoformat())
    except ValueError as e:
        raise click.ClickException(str(e))


if __name__ == "__main__":
    cli()
