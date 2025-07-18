from .user import UserSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, 
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, 
    ItensCompraSerializer,
)
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer

