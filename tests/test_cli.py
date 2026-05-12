"""dataproc CLI 의 테스트."""

from click.testing import CliRunner

from dataproc.cli import cli


def test_cli_help():
    """--help 옵션이 정상 동작한다."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "to-unixtime" in result.output
    assert "to-datetime" in result.output


def test_cli_to_unixtime_valid_input():
    """유효한 datetime 문자열을 unix timestamp 로 변환한다."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-unixtime", "2024-05-01T10:30:00"])
    assert result.exit_code == 0
    # stdout 에 숫자가 출력되어야 함
    assert result.output.strip().isdigit()


def test_cli_to_unixtime_invalid_input():
    """잘못된 포맷에 대해 0 이 아닌 exit code 를 반환한다."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-unixtime", "completely invalid"])
    assert result.exit_code != 0


def test_cli_to_datetime_valid_input():
    """유효한 datetime 문자열을 ISO 포맷으로 정규화한다."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-datetime", "01/05/24 10:30:00"])
    assert result.exit_code == 0
    assert "2024" in result.output


def test_cli_to_datetime_invalid_input():
    """잘못된 포맷에 대해 0 이 아닌 exit code 를 반환한다."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-datetime", "completely invalid"])
    assert result.exit_code != 0
