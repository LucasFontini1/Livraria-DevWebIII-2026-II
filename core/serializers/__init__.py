from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraSerializer,
)
from .editora import EditoraSerializer
from .livro import LivroSerializer, LivroListSerializer, LivroRetrieveSerializer
from .user import UserRegistrationSerializer, UserSerializer