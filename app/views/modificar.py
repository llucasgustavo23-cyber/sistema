from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from PySide6.QtCore import Signal, QDate, Qt, QStringListModel
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication, QDialogButtonBox, QCompleter
from PySide6.QtGui import QCloseEvent
from ui_modificar import Ui_modificar
from sugestoes import SugestoesProvider  # <<-- provider central
import sys


@dataclass
class AmbulanciaDTO:
    modelo: str
    placa: str
    chassi: str
    tipo_aquisicao: str
    data_aquisicao: QDate
    ano: int
    cnes: str
    denominacao: str


class Modificar(QWidget, Ui_modificar):
    gotomenu = Signal()                      
    submitted = Signal(AmbulanciaDTO)         

    def __init__(self, provider: SugestoesProvider, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._provider = provider  # <<-- injeta o provider
        self.setupUi(self)
        self.setWindowTitle("Modificar Dados da Ambulância")

        # Aliases conforme seu .ui
        self.placa = self.lineEdit            
        self.modelo_combo = self.comboBox

        # Models locais (serão alimentados pelo provider)
        self._model_placa = QStringListModel([], self)
        self._model_chassi = QStringListModel([], self)
        self._model_cnes = QStringListModel([], self)
        self._model_denominacao = QStringListModel([], self)

        # >>> Autocomplete nos campos (completares + primeira sincronização)
        self._setup_completers()
        self._provider.suggestions_changed.connect(self._sync_sugestoes_deste_form)
        self._sync_sugestoes_deste_form()

        # -------------------- Conexões dos botões OK/Cancel --------------------
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        try:
            ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
            cancel_btn = self.buttonBox.button(QDialogButtonBox.Cancel)

            if ok_btn is not None:
                ok_btn.clicked.connect(self.on_buttonBox_accepted)
            else:
                print("[Modificar] Aviso: buttonBox não possui botão Ok (verifique o .ui)")

            if cancel_btn is not None:
                cancel_btn.clicked.connect(self.on_buttonBox_rejected)
            else:
                print("[Modificar] Aviso: buttonBox não possui botão Cancel (verifique o .ui)")
        except Exception as e:
            print("[Modificar] Aviso: não consegui conectar diretamente aos botões do buttonBox:", e)

        # Remover destaque de erro assim que alterar algo
        self.placa.textChanged.connect(lambda _: self.placa.setStyleSheet(""))
        self.chassi.textChanged.connect(lambda _: self.chassi.setStyleSheet(""))
        self.cnes.textChanged.connect(lambda _: self.cnes.setStyleSheet(""))
        self.denominacao.textChanged.connect(lambda _: self.denominacao.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.ano.valueChanged.connect(lambda _: self.ano.setStyleSheet(""))
        self.data.dateChanged.connect(lambda _: self.data.setStyleSheet(""))

    # -------------------- AUTOCOMPLETE (primeira opção com provider) --------------------

    def _setup_completers(self):
        def fazocomplete(model: QStringListModel) -> QCompleter:
            comp = QCompleter(model, self)
            comp.setCaseSensitivity(Qt.CaseInsensitive)
            comp.setFilterMode(Qt.MatchContains)  # sugestões que CONTÊM o texto
            comp.setCompletionMode(QCompleter.PopupCompletion)
            return comp

        self.placa.setCompleter(fazocomplete(self._model_placa))
        self.chassi.setCompleter(fazocomplete(self._model_chassi))
        self.cnes.setCompleter(fazocomplete(self._model_cnes))
        self.denominacao.setCompleter(fazocomplete(self._model_denominacao))

        # (Opcional) Autocomplete no ComboBox de modelo — torne-o editável e crie um model dedicado
        # self.modelo_combo.setEditable(True)
        # self._model_modelo = QStringListModel(["Fiat Ducato", "Mercedes Sprinter"], self)
        # self.modelo_combo.setCompleter(fazocomplete(self._model_modelo))

    def _sync_sugestoes_deste_form(self):
        """
        Atualiza os QStringListModel deste form com o estado atual do provider.
        É chamado na criação e sempre que o provider emitir suggestions_changed.
        """
        self._model_placa.setStringList(self._provider.placas())
        self._model_chassi.setStringList(self._provider.chassis())
        self._model_cnes.setStringList(self._provider.cnes())
        self._model_denominacao.setStringList(self._provider.denominacoes())

    # -------------------- OK / CANCELAR --------------------

    def on_buttonBox_accepted(self):
        """Valida, emite o DTO e volta para o Menu (sem fechar o widget)."""
        print("[Modificar] OK clicado")
        self._resetar_estilos()

        campos_invalidos = []

        if not self.placa.text().strip():
            campos_invalidos.append(self.placa)
        if not self.chassi.text().strip():
            campos_invalidos.append(self.chassi)
        if not self.cnes.text().strip():
            campos_invalidos.append(self.cnes)
        if not self.denominacao.text().strip():
            campos_invalidos.append(self.denominacao)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),
            placa=self.placa.text().strip(),
            chassi=self.chassi.text().strip(),
            tipo_aquisicao=self.tipo.currentText(),
            data_aquisicao=self.data.date(),
            ano=self.ano.value(),
            cnes=self.cnes.text().strip(),
            denominacao=self.denominacao.text().strip(),
        )

        # Emite para quem quiser persistir/sincronizar
        self.submitted.emit(dto)
        QMessageBox.information(self, "Sucesso", "Cadastro salvo com sucesso!")
        self.gotomenu.emit()

    def on_buttonBox_rejected(self):
        """Cancelar → voltar para o Menu (sem fechar o widget)."""
        print("[Modificar] Cancelar clicado")
        self._resetar_estilos()
        self.gotomenu.emit()

    # -------------------- Proteção contra fechamento --------------------

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.parent() is not None:
            self.gotomenu.emit()
            event.ignore()  # não fecha se for "filho" de outro widget
        else:
            event.accept()

    # -------------------- Helpers de validação/estilo --------------------

    def _resetar_estilos(self):
        for w in (self.placa, self.chassi, self.cnes, self.denominacao):
            w.setStyleSheet("")
        self.modelo_combo.setStyleSheet("")
        self.ano.setStyleSheet("")
        self.data.setStyleSheet("")

    def _destacar_campos_vazios(self, widgets):
        estilo_line = "QLineEdit { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_combo = "QComboBox { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_spin = "QSpinBox { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_date = "QDateEdit { border: 1px solid #d9534f; border-radius: 6px; }"

        for w in widgets:
            cls = w.metaObject().className()
            if cls == "QLineEdit":
                w.setStyleSheet(estilo_line)
            elif cls == "QComboBox":
                w.setStyleSheet(estilo_combo)
            elif cls == "QSpinBox":
                w.setStyleSheet(estilo_spin)
            elif cls == "QDateEdit":
                w.setStyleSheet(estilo_date)
            else:
                w.setStyleSheet(estilo_line)


# Execução isolada para testar a tela com provider vazio
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     from sugestoes import DTOBase, SugestoesProvider

#     provider = SugestoesProvider()
#     # Exemplo: carga inicial (substituir por leitura real do DAO)
#     # provider.load_from([DTOBase("ABC1D23", "9BW...", "1234567", "Ambulância Tipo A")])

#     w = Modificar(provider)
#     w.show()
#     sys.exit(app.exec())