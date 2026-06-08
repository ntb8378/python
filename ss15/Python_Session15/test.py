def demo(a: str, b: list[str]):
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Raises:
        ValueError: _description_

    Returns:
        int: _description_
    """    
    
    a.upper()
    
    if b == 0:
        raise ValueError("Tham số 2 không được phép bằng 0")

try:
    result = demo(3, 8)
    print(3 / 0)
    
except ValueError:
    print("Nhập lại đi")
