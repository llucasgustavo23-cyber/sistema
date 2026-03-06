from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
    QAbstractScrollArea,
    QAbstractItemView,
)
from PySide6.QtCore import Signal, Qt, QDate
# Se o Ui_listardados estiver em outro módulo, mantenha este import:
from .ui_lista import Ui_listardados
# Caso o Ui_listardados esteja no MESMO arquivo (como você colou acima),
# comente a linha acima e use:  from __main__ import Ui_listardados


class listardados(QWidget, Ui_listardados):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configura a tabela conforme solicitado
        self._setup_table()

        # Ligações (botões, etc.)
        self._wire()

    # --------------------------------------------------------
    # Ligações
    # --------------------------------------------------------
    def _wire(self) -> None:
        # Na UI o botão se chama "pushButton" (VOLTAR)
        if hasattr(self, "pushButton") and self.pushButton:
            self.pushButton.clicked.connect(self.gotomenu.emit)
        else:
            print("[listardados] Aviso: pushButton não encontrado na UI")

        # (Opcional) botaoExcluir — você pode conectar aqui também
        # if hasattr(self, "botaoExcluir") and self.botaoExcluir:
        #     self.botaoExcluir.clicked.connect(self._on_excluir)

    # --------------------------------------------------------
    # Ajustes COMPLETOS da QTableWidget
    # --------------------------------------------------------
    def _setup_table(self) -> None:
        """
        Deixa a QTableWidget ocupar toda a largura da janela, com texto visível
        (sem elipse), suporte a quebra de linha e linhas ajustadas ao conteúdo.
        """
        table = self.tableWidget  # do Ui_listardados

        # 1) Colunas ocupam TODO o espaço horizontal disponível
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)  # redundante com Stretch, mas mantém robustez

        # 2) Expansão adequada dentro do layout
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 3) Ajuste fino de tamanho baseado em conteúdo (sem deixar espaço “morto”)
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # 4) Mostrar texto COMPLETO (sem "...")
        table.setTextElideMode(Qt.ElideNone)

        # 5) Permitir quebra de linha dentro da célula
        table.setWordWrap(True)

        # 6) Ajustar altura das linhas conforme o conteúdo atual
        table.resizeRowsToContents()

        # 7) Comportamento de seleção mais amigável (linha inteira)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 8) Como as colunas esticam, não precisamos de scroll horizontal
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 9) (Opcional) Rolagem mais suave
        table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        # 10) (Opcional) Cores alternadas por linha para legibilidade
        # table.setAlternatingRowColors(True)

        # 11) Reajusta a altura quando o conteúdo mudar (ex.: depois de carregar dados)
        # Se preferir, você pode chamar `self._auto_resize()` manualmente após preencher a tabela.
        table.itemChanged.connect(self._auto_resize)

        print("[listardados] Tabela ajustada com sucesso.")

    def _auto_resize(self, *args):
        """Recalcula a altura das linhas quando o conteúdo muda."""
        try:
            self.tableWidget.resizeRowsToContents()
        except Exception:
            pass

    # --------------------------------------------------------
    # Exemplo (opcional): preencher a tabela e ver os ajustes
    # --------------------------------------------------------
    def carregar_dados_exemplo(self):
        """
        Exemplo de preenchimento para testar os ajustes.
        Remova/adicione conforme sua fonte de dados real.
        """
        dados = [
            ["1", "9BWZZZ377VT004251", "Modelo X muito longo com variações", "2024",
             "Doação de convênio estadual", "Compra direta", "SIM", "NÃO"],
            ["2", "9BWZZZ377VT004252", "Modelo Y", "2023",
             "Licitação 123/2023", "Licitação", "NÃO", "SIM"],
        ]

        self.tableWidget.setRowCount(len(dados))
        for r, linha in enumerate(dados):
            for c, valor in enumerate(linha):
                item = QTableWidgetItem(str(valor))
                # Tooltip ajuda quando o texto é bem grande
                item.setToolTip(str(valor))
                self.tableWidget.setItem(r, c, item)

        # Depois de preencher, ajuste novamente as linhas
        self._auto_resize()
