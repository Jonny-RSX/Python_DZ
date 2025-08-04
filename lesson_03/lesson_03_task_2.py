from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13", "+79111111111"),
    Smartphone("Samsung", "Galaxy S21", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79333333333"),
    Smartphone("Huawei", "P40 Pro", "+79444444444"),
    Smartphone("OnePlus", "9 Pro", "+79555555555")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")