from datetime import datetime, timezone

import numpy as np


def str_to_datetime(date_str: str) -> datetime:
    """ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식의 날짜 문자열을 datetime 객체로 변환


    Parameters
    ----------
    date_str : str
        변환할 날짜 문자열. ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식을 지원

    Returns
    -------
    datetime
        datetime 객체로 변환된 날짜

    Raises
    ------
    ValueError
        지원하지 않는 형식의 날짜 문자열이 주어지는 경우
    ValueError
        미래의 날짜인 경우

    Examples
    --------
    >>> str_to_datetime("2024-05-01 10:30:00")
    datetime(2024, 5, 1, 10, 30)
    >>> str_to_datetime("2024/05/01 10:30")
    ValueError: 지원하지 않는 날짜 포맷입니다: 2024/05/01 10:30
    >>> str_to_datetime("2026-06-01 10:30:00")
    ValueError: 미래 날짜는 처리할 수 없습니다: 2026-06-01 10:30:00
    """
    dt: datetime

    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        try:
            dt = datetime.strptime(date_str, "%d/%m/%y %H:%M:%S")
        except ValueError:
            raise ValueError(f"지원하지 않는 날짜 포맷입니다: {date_str}")

    if dt > datetime.now():
        raise ValueError(f"미래 날짜는 처리할 수 없습니다: {date_str}")

    return dt


def str_to_unixtime(date_str: str) -> np.int64:
    """
    ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식의 날짜 문자열을 유닉스 타임스탬프로 변환.
    변환된 값은 마이크로초(microseconds) 단위의 64비트 정수

    Parameters
    ----------
    date_str : str
        변환할 날짜 문자열. ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식을 지원

    Returns
    -------
    np.int64
        64bit integer (numpy.int64) unix timestamp (microseconds 단위)

    Raises
    ------
    ValueError
        지원하지 않는 형식의 날짜 문자열이 주어지는 경우
    ValueError
        미래 날짜가 전달되는 경우

    Examples
    --------
    >>> str_to_unixtime("2024-05-01 10:30:00")
    1714527000000000
    >>> str_to_unixtime("2026-07-06T11:30:12.365233")
    ValueError: 미래 날짜는 처리할 수 없습니다: 2026-07-06T11:30:12.365233
    >>> str_to_unixtime("2024/05/01 10:30")
    ValueError: 지원하지 않는 날짜 포맷입니다: 2024/05/01 10:30

    """
    dt = str_to_datetime(date_str)

    unix_micros = int(dt.timestamp() * 1_000_000)

    return np.int64(unix_micros)
