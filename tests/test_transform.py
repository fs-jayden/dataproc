from contextlib import nullcontext
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

from dataproc.transform import str_to_datetime, str_to_unixtime

# 과제에서 제공된 테스트 데이터 세트
DATASTRINGS = [
    (
        "2026-05-06T11:30:12.365233",
        datetime(2026, 5, 6, 11, 30, 12, 365233),
        1778034612365233,
        nullcontext(),
    ),
    (
        "2024-05-01 10:30:10.000100",
        datetime(2024, 5, 1, 10, 30, 10, 100),
        1714527010000100,
        nullcontext(),
    ),
    ("2024-05-01 10:30", datetime(2024, 5, 1, 10, 30), 1714527000000000, nullcontext()),
    (
        "2024/05/01 10:30",
        datetime(2024, 5, 1, 10, 30),
        1714527000000000,
        pytest.raises(ValueError),
    ),
]


@pytest.fixture
def sample_datetime_string_df():
    data = {
        "datetime_string": [
            "2026-05-06T11:30:12.365233",
            "2024-05-01 10:30:10.000100",
            "2024-05-01 10:30",
            "2024/05/01 10:30",
        ],
        "expected": [
            datetime(2026, 5, 6, 11, 30, 12, 365233),
            datetime(2024, 5, 1, 10, 30, 10, 100),
            datetime(2024, 5, 1, 10, 30),
            datetime(2024, 5, 1, 10, 30),
        ],
    }
    return pd.DataFrame(data)


@pytest.mark.parametrize(
    "date_str, expected_dt, expected_unix, expectation", DATASTRINGS
)
def test_transform_parameterized(date_str, expected_dt, expected_unix, expectation):
    """str_to_datetime: 입력 날짜 문자열을 datetime 객체로 변환하는 함수
        str_to_unixtime: 입력 날짜 문자열을 유닉스 타임스탬프로 변환하는 함수
        위 2가지 함수에 대해 다양한 입력과 예상 결과를 테스트하는 함수

    Parameters
    ----------
    date_str : _type_
        입력 날짜 문자열
    expected_dt : _type_
        변환 후 예상되는 datetime
    expected_unix : _type_
        변환 후 예상되는 유닉스 타임스탬프
    expectation : _type_
        변환 후 성공/실패 예상
    """
    # str_to_datetime 테스트
    # ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식을 입력받고,
    # datetime 객체로 변환하는지 테스트
    with expectation:
        dt_result = str_to_datetime(date_str)
        assert dt_result == expected_dt

    # str_to_unixtime 테스트
    # ISO 8601 형식과 "YYYY-MM-DD HH:MM:SS" 형식을 입력받고,
    # 유닉스 타임스탬프(int64)로 변환하는지 테스트
    with expectation:
        unix_result = str_to_unixtime(date_str)
        assert unix_result == expected_unix
        assert isinstance(unix_result, np.int64)


def test_str_to_datetime_with_df(sample_datetime_string_df):
    failing_inputs = ["2024/05/01 10:30"]

    for _, row in sample_datetime_string_df.iterrows():
        # 허용되지 않은 포맷인 네 번째 행(2024/05/01 10:30)은 ValueError가 발생
        if row["datetime_string"] in failing_inputs:
            with pytest.raises(ValueError):
                str_to_datetime(row["datetime_string"])
        else:
            assert str_to_datetime(row["datetime_string"]) == row["expected"]


def test_str_to_unixtime_with_df(sample_datetime_string_df):
    failing_inputs = ["2024/05/01 10:30"]

    unix_map = {item[0]: item[2] for item in DATASTRINGS}

    for _, row in sample_datetime_string_df.iterrows():
        # 허용되지 않은 포맷인 네 번째 행(2024/05/01 10:30)은 ValueError가 발생
        if row["datetime_string"] in failing_inputs:
            with pytest.raises(ValueError):
                str_to_unixtime(row["datetime_string"])
        else:
            expected_unix = np.int64(unix_map[row["datetime_string"]])
            result = str_to_unixtime(row["datetime_string"])

            # 값의 정확성 검증
            assert result == expected_unix
            # 리턴 타입이 numpy.int64인지 검증
            assert isinstance(result, np.int64)
