```python
from typing import Sequence
Sequence[int]  # 函数期望某种序列，不关心是列表还是元组

dic: dict[str, int] = {
    "s": 1,
    "s1": 2
}

Literal["type1", "type2", "type3"]  # 可选择的选项

Callable[[str, int], int]  # 可调用对象 [[接收值], 返回值]

def raiseError() -> NoReturn:  # 不会正常返回的函数 NoReturn
    pass

Optional[str] str | None 
# 等效
Union[None, str]

Card = Tuple[str, str]  # 类型别名

# ？？？
from typing import Type, TypeVar
TAnimal = TypeVar("TAnimal", bound="Animal")

# new type
new_type = NewType("new_type", int)
new_type(1)  # 1: int ==>> 1: new_type

class Node():
    def __init__(self, prev: "Node"):  # Node -> "Node"
        pass 
    
 
```

