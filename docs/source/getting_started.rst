처음 시작하기
==========================================

이 페이지는 ``dataproc`` 패키지를 처음 사용하는 사용자를 위한 가이드입니다.

설치 방법
----------

다음 명령어를 통해 패키지를 설치할 수 있습니다:

.. code-block:: bash

   pip install dataproc

주요 기능 사용법
------------------

문자열을 datetime 객체로 변환하는 방법입니다:

.. code-block:: python

   from dataproc.transform import str_to_datetime
   
   dt = str_to_datetime("2024-05-01 10:30:00")
   print(dt)