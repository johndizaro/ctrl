from dataclasses import dataclass, field




@dataclass(order=True)
class Item:
    """
    items
    """

    sert_index_id_item: int = field(init=False, repr=False)
    id_item: int
    desc_item: str
    id_unidade_medida: str

    def __post_init__(self):
        self.sert_index_id_item = self.id_unidade_medida


registros = [
    Item(id_item=1, desc_item="Trigo", id_unidade_medida=1),
    Item(id_item=2, desc_item="Açucar", id_unidade_medida=1),
]

print(f"registros:{registros}")
