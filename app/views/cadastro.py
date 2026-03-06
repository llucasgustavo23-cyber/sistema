# cadastro.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from datetime import date

from PySide6.QtCore import Signal, QDate, Qt, QStringListModel
from PySide6.QtWidgets import QWidget, QMessageBox, QDialogButtonBox, QCompleter
from PySide6.QtGui import QCloseEvent

from ui_cadastro import Ui_cadastro
from app.database import Database

@dataclass
class AmbulanciaDTO:
    modelo: str
    placa: str
    chassi: str
    forma_aquisicao: str
    data_aquisicao: QDate
    oficial: bool
    cnes: str
    denominacao: str

class Cadastro(QWidget, Ui_cadastro):
    gotomenu = Signal()
    submitted = Signal(AmbulanciaDTO)
    gotocadastro = Signal()
    gotoambulancai = Signal()

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Ambulâncias")

        # DB
        self._db = Database()

        # Aliases conforme o seu .ui:
        self.placa_edit = self.lineEdit
        self.modelo_combo = self.comboBox
        self.chassi_edit = self.chassi
        self.forma_combo = self.tipo            # for_aquisicao.tipo
        self.data_edit = self.data
        self.cnes_edit = self.cnes
        self.denominacao_edit = self.denominacao

        # Autocomplete local
        self._model_placa = QStringListModel([], self)
        self._model_chassi = QStringListModel([], self)
        self._model_cnes = QStringListModel([], self)
        self._model_denominacao = QStringListModel([], self)
        self._setup_completers()

        # Botões OK/Cancelar
        # Botões OK/Cancelar (SOMENTE UMA VEZ, sem duplicação!)
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)
        # Tira realce de erro ao digitar
        self.placa_edit.textChanged.connect(lambda _: self.placa_edit.setStyleSheet(""))
        self.chassi_edit.textChanged.connect(lambda _: self.chassi_edit.setStyleSheet(""))
        self.cnes_edit.textChanged.connect(lambda _: self.cnes_edit.setStyleSheet(""))
        self.denominacao_edit.textChanged.connect(lambda _: self.denominacao_edit.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.data_edit.dateChanged.connect(lambda _: self.data_edit.setStyleSheet(""))

        # Radio buttons: radioButton_2 = Oficial, radioButton = Reserva
        self.radioButton_2.toggled.connect(self._atualizar_cnes_visibilidade)  # Oficial
        self.radioButton.toggled.connect(self._atualizar_cnes_visibilidade)    # Reserva
        if not (self.radioButton_2.isChecked() or self.radioButton.isChecked()):
            self.radioButton_2.setChecked(True)
        self._atualizar_cnes_visibilidade()

    # -------------------- Completers --------------------
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

    def _atualizar_cnes_visibilidade(self) -> None:
        oficial = self.radioButton_2.isChecked()
        self.lbl_cnes.setVisible(oficial)
        self.cnes.setVisible(oficial)
        self.cnes.setEnabled(oficial)
        if not oficial:
            self.cnes.clear()
            self.cnes.setStyleSheet("")

    # -------------------- OK / Cancelar --------------------
    def on_buttonBox_accepted(self):
        self._resetar_estilos()
        oficial = self.radioButton_2.isChecked()

        # Validações (conforme você definiu)
        campos_invalidos = []
        if not self.placa_edit.text().strip(): campos_invalidos.append(self.placa_edit)
        if not self.chassi_edit.text().strip(): campos_invalidos.append(self.chassi_edit)
        if not self.denominacao_edit.text().strip(): campos_invalidos.append(self.denominacao_edit)
        if oficial and not self.cnes_edit.text().strip(): campos_invalidos.append(self.cnes_edit)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),
            placa=self.placa_edit.text().strip(),
            chassi=self.chassi_edit.text().strip(),
            forma_aquisicao=self.forma_combo.currentText().strip(),
            data_aquisicao=self.data_edit.date(),
            oficial=oficial,
            cnes=self.cnes_edit.text().strip(),
            denominacao=self.denominacao_edit.text().strip(),
        )

        # Converte QDate -> date
        d = date(dto.data_aquisicao.year(), dto.data_aquisicao.month(), dto.data_aquisicao.day())

        # Salva no banco (alinhado ao seu schema)
        try:
            new_id = self._db.cadastrar_ambulancia(
                modelo_texto=dto.modelo,
                placa=dto.placa,
                chassi=dto.chassi,
                forma_aquisicao_texto=dto.forma_aquisicao,
                data_aquisicao=d,
                uso_oficial=dto.oficial,
                cnes=(dto.cnes if dto.oficial else None),
                denominacao=dto.denominacao,  # só será usada se a coluna existir
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro ao salvar", f"Ocorreu um erro ao salvar o cadastro:\n{e}")
            return

        self.submitted.emit(dto)
        QMessageBox.information(self, "Sucesso", f"Cadastro salvo com sucesso! (ID {new_id})")
        self._limpar_form()
        self.gotocadastro.emit()

    def on_buttonBox_rejected(self):
        self._resetar_estilos()
        self.gotomenu.emit()

    # -------------------- Fechamento --------------------
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.parent() is not None:
            self.gotomenu.emit()
            event.ignore()
        else:
            event.accept()

    # -------------------- Helpers UI --------------------
    def _resetar_estilos(self):
        for w in (self.placa_edit, self.chassi_edit, self.cnes_edit, self.denominacao_edit):
            w.setStyleSheet("")
        self.modelo_combo.setStyleSheet("")
        self.data_edit.setStyleSheet("")

    def _destacar_campos_vazios(self, widgets):
        estilo_line = "QLineEdit { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_combo = "QComboBox { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_date = "QDateEdit { border: 1px solid #d9534f; border-radius: 6px; }"
        for w in widgets:
            cls = w.metaObject().className()
            if cls == "QLineEdit": w.setStyleSheet(estilo_line)
            elif cls == "QComboBox": w.setStyleSheet(estilo_combo)
            elif cls == "QDateEdit": w.setStyleSheet(estilo_date)
            else: w.setStyleSheet(estilo_line)

    def _limpar_form(self):
        self.placa_edit.clear()
        self.chassi_edit.clear()
        self.denominacao_edit.clear()
        self.cnes_edit.clear()
        # mantém seleção atual dos combos e data