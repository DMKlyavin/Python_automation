from adress import Address
from mailing import Mailing

letter = Mailing(Address("г.Владимир", "ул.Смоленская", "д.10", "кв.1", "600029"),
                 Address("г.Светлогорск",  "ул.Приморская",
                         "д.11", "кв.8", "238563"),
                 "400 ₽", "805 130 969 12500")

print(f"Письмо с номером отслеживания: {letter.track} отправлено с адреса: {
      letter.from_address}. В пункт назначения: {letter.to_address}. Стоимость отправления составляет: {letter.cost}")
