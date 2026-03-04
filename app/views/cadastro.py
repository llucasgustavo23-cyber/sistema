from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import Signal, QDate, Qt, QStringListModel
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication, QDialogButtonBox, QCompleter
from PySide6.QtGui import QCloseEvent

from ui_cadastro import Ui_cadastro
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


class Cadastro(QWidget, Ui_cadastro):
    gotomenu = Signal()
    submitted = Signal(AmbulanciaDTO)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Ambulâncias")

        # --- Aliases conforme o seu .ui ---
        # lbl_modelo -> "Placa"  => QLineEdit correto para PLACA é self.lineEdit
        # lbl_placa  -> "Modelo" => QComboBox correto para MODELO é self.comboBox
        self.placa_edit = self.lineEdit            # QLineEdit de PLACA
        self.modelo_combo = self.comboBox          # QComboBox de MODELO
        self.chassi_edit = self.chassi             # QLineEdit chassi
        self.tipo_combo = self.tipo                # QComboBox tipo de aquisição
        self.data_edit = self.data                 # QDateEdit
        self.ano_spin = self.ano                   # QSpinBox
        self.cnes_edit = self.cnes                 # QLineEdit cnes
        self.denominacao_edit = self.denominacao   # QLineEdit denominação

        # --- Autocomplete local (sem provider) ---
        self._model_placa = QStringListModel([], self)
        self._model_chassi = QStringListModel([], self)
        self._model_cnes = QStringListModel([], self)
        self._model_denominacao = QStringListModel([], self)

        self._setup_completers()

        # -------------------- Conexões dos botões OK/Cancel --------------------
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        try:
            ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
            cancel_btn = self.buttonBox.button(QDialogButtonBox.Cancel)
            if ok_btn is not None:
                ok_btn.clicked.connect(self.on_buttonBox_accepted)
            else:
                print("[Cadastro] Aviso: buttonBox não possui botão Ok (verifique o .ui)")
            if cancel_btn is not None:
                cancel_btn.clicked.connect(self.on_buttonBox_rejected)
            else:
                print("[Cadastro] Aviso: buttonBox não possui botão Cancel (verifique o .ui)")
        except Exception as e:
            print("[Cadastro] Aviso: não consegui conectar diretamente aos botões do buttonBox:", e)

        # Remover destaque de erro assim que o usuário alterar algo
        self.placa_edit.textChanged.connect(lambda _: self.placa_edit.setStyleSheet(""))
        self.chassi_edit.textChanged.connect(lambda _: self.chassi_edit.setStyleSheet(""))
        self.cnes_edit.textChanged.connect(lambda _: self.cnes_edit.setStyleSheet(""))
        self.denominacao_edit.textChanged.connect(lambda _: self.denominacao_edit.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.ano_spin.valueChanged.connect(lambda _: self.ano_spin.setStyleSheet(""))
        self.data_edit.dateChanged.connect(lambda _: self.data_edit.setStyleSheet(""))

    # -------------------- AUTOCOMPLETE (local) --------------------

    def _setup_completers(self):
        def mk(model: QStringListModel) -> QCompleter:
            c = QCompleter(model, self)
            c.setCaseSensitivity(Qt.CaseInsensitive)
            c.setFilterMode(Qt.MatchContains)
            c.setCompletionMode(QCompleter.PopupCompletion)
            return c

        self.placa_edit.setCompleter(mk(self._model_placa))
        self.chassi_edit.setCompleter(mk(self._model_chassi))
        self.cnes_edit.setCompleter(mk(self._model_cnes))
        self.denominacao_edit.setCompleter(mk(self._model_denominacao))

        # Se quiser autocomplete no combo de MODELO (tornando editável):
        # self.modelo_combo.setEditable(True)
        # self._model_modelo = QStringListModel(["Fiat Ducato", "Mercedes Sprinter"], self)
        # self.modelo_combo.setCompleter(mk(self._model_modelo))

    # ---- Métodos públicos para alimentar as sugestões de fora (ex.: MainWindow) ----
    def atualizar_opcoes_placa(self, lista: list[str]):
        self._model_placa.setStringList(lista or [])

    def atualizar_opcoes_chassi(self, lista: list[str]):
        self._model_chassi.setStringList(lista or [])

    def atualizar_opcoes_cnes(self, lista: list[str]):
        self._model_cnes.setStringList(lista or [])

    def atualizar_opcoes_denominacao(self, lista: list[str]):
        self._model_denominacao.setStringList(lista or [])

    # -------------------- OK / CANCELAR --------------------

    def on_buttonBox_accepted(self):
        """Valida, emite o DTO e volta para o Menu (sem fechar o widget)."""
        self._resetar_estilos()

        campos_invalidos = []
        if not self.placa_edit.text().strip():
            campos_invalidos.append(self.placa_edit)
        if not self.chassi_edit.text().strip():
            campos_invalidos.append(self.chassi_edit)
        if not self.cnes_edit.text().strip():
            campos_invalidos.append(self.cnes_edit)
        if not self.denominacao_edit.text().strip():
            campos_invalidos.append(self.denominacao_edit)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        # Monta DTO (alinhado ao UI)
        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),   
            placa=self.placa_edit.text().strip(),             
            chassi=self.chassi_edit.text().strip(),
            tipo_aquisicao=self.tipo_combo.currentText(),
            data_aquisicao=self.data_edit.date(),
            ano=self.ano_spin.value(),
            cnes=self.cnes_edit.text().strip(),
            denominacao=self.denominacao_edit.text().strip(),
        )

        # Emite para quem quiser persistir/sincronizar
        self.submitted.emit(dto)

        # Feedback opcional
        QMessageBox.information(self, "Sucesso", "Cadastro salvo com sucesso!")

        # Voltar ao menu
        self.gotomenu.emit()

    def on_buttonBox_rejected(self):
        """Cancelar → voltar para o Menu (sem fechar o widget)."""
        self._resetar_estilos()
        self.gotomenu.emit()

    # -------------------- Proteção contra fechamento --------------------

    def closeEvent(self, event: QCloseEvent) -> None:
        """Se este widget estiver dentro do QStackedWidget (tem parent), não fecha; volta ao menu."""
        if self.parent() is not None:
            self.gotomenu.emit()
            event.ignore()
        else:
            event.accept()

    # -------------------- Helpers de validação/estilo --------------------

    def _resetar_estilos(self):
        for w in (self.placa_edit, self.chassi_edit, self.cnes_edit, self.denominacao_edit):
            w.setStyleSheet("")
        self.modelo_combo.setStyleSheet("")
        self.ano_spin.setStyleSheet("")
        self.data_edit.setStyleSheet("")

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