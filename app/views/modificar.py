# modificar.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from datetime import date

from PySide6.QtCore import Signal, QDate, Qt, QStringListModel
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QDialogButtonBox, QCompleter, QButtonGroup
)
from PySide6.QtGui import QCloseEvent

from ui_modificar import Ui_modificar
from app.database import Database  # <- integração com o banco


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
    gotomodificar = Signal()

    def __init__(self, provider=None, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._provider = provider  
        self._db = Database()

        self.setupUi(self)
        self.setWindowTitle("Modificar Dados da Ambulância")

        # Aliases conforme seu .ui
        self.placa = self.lineEdit          # (QLineEdit) – “Placa”
        self.modelo_combo = self.comboBox   # (QComboBox) – “Modelo”
        # self.tipo (QComboBox) – “Forma de aquisição” já existe no .ui
        # self.chassi (QLineEdit) – existe no .ui
        # self.cnes (QLineEdit), self.lbl_cnes (QLabel)
        # RadioButtons: self.radioButton_2 = "Oficial" | self.radioButton = "Reserva"
        # self.data (QDateEdit), self.ano (QSpinBox), self.denominacao (QLineEdit)

        # --- Grupo de botões para garantir exclusividade ---
        self._grupo_categoria = QButtonGroup(self)
        self._grupo_categoria.setExclusive(True)
        self._grupo_categoria.addButton(self.radioButton_2)  # Oficial
        self._grupo_categoria.addButton(self.radioButton)    # Reserva

        # Models locais para autocompletes
        self._model_placa = QStringListModel([], self)
        self._model_chassi = QStringListModel([], self)
        self._model_cnes = QStringListModel([], self)
        self._model_denominacao = QStringListModel([], self)

        # Autocompletes
        self._setup_completers()

        # Carrega combos e sugestões do BD
        self._carregar_modelos_do_bd()
        self._carregar_formas_do_bd()
        self._carregar_sugestoes_do_bd()

        # Se existir provider externo, sincroniza também
        if self._provider is not None:
            try:
                self._provider.suggestions_changed.connect(self._sync_sugestoes_do_provider)
                self._sync_sugestoes_do_provider()
            except Exception:
                pass

        # -------------------- Conexões dos botões OK/Cancel --------------------
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)
        try:
            ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
            cancel_btn = self.buttonBox.button(QDialogButtonBox.Cancel)
            if ok_btn is not None:
                ok_btn.clicked.connect(self.on_buttonBox_accepted)
            if cancel_btn is not None:
                cancel_btn.clicked.connect(self.on_buttonBox_rejected)
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

        # -------------------- Regras de visibilidade do CNES --------------------
        self.radioButton_2.toggled.connect(self._atualizar_cnes_visibilidade)  
        self.radioButton.toggled.connect(self._atualizar_cnes_visibilidade)    
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

        self.placa.setCompleter(mk(self._model_placa))
        self.chassi.setCompleter(mk(self._model_chassi))
        self.cnes.setCompleter(mk(self._model_cnes))
        self.denominacao.setCompleter(mk(self._model_denominacao))

    # -------------------- Carregamentos do BD --------------------
    def _carregar_modelos_do_bd(self):
        """Preenche combo de modelo com (nome visível, id no userData)."""
        self.modelo_combo.clear()
        try:
            for row in self._db.listar_modelos():
                self.modelo_combo.addItem(str(row["nome"]), row["id_modelo"])
        except Exception as e:
            print("[Modificar] Erro ao carregar modelos:", e)

    def _carregar_formas_do_bd(self):
        """Preenche combo de forma de aquisição (self.tipo) com (nome visível, id no userData)."""
        try:
            self.tipo.clear()
            for row in self._db.listar_formas_aquisicao():
                self.tipo.addItem(str(row["nome"]), row["id"])
        except Exception as e:
            print("[Modificar] Erro ao carregar formas de aquisição:", e)

    def _carregar_sugestoes_do_bd(self):
        """Carrega listas para os autocompletes a partir do banco."""
        try:
            self._model_placa.setStringList(self._db.listar_placas())
            self._model_chassi.setStringList(self._db.listar_chassis())
            self._model_cnes.setStringList(self._db.listar_cnes())
            self._model_denominacao.setStringList(self._db.listar_denominacoes())
        except Exception as e:
            print("[Modificar] Erro ao carregar sugestões do BD:", e)

    def _sync_sugestoes_do_provider(self):
        """Se houver provider externo, sincroniza com ele também (opcional)."""
        try:
            self._model_placa.setStringList(self._provider.placas() or self._db.listar_placas())
            self._model_chassi.setStringList(self._provider.chassis() or self._db.listar_chassis())
            self._model_cnes.setStringList(self._provider.cnes() or self._db.listar_cnes())
            self._model_denominacao.setStringList(self._provider.denominacoes() or self._db.listar_denominacoes())
        except Exception:
            # Se o provider não tiver esses métodos, usamos apenas o BD
            self._carregar_sugestoes_do_bd()

    # -------------------- VISIBILIDADE DO CNES --------------------
    def _atualizar_cnes_visibilidade(self) -> None:
        oficial = self.radioButton_2.isChecked()  
        self.lbl_cnes.setVisible(oficial)
        self.cnes.setVisible(oficial)
        self.cnes.setEnabled(oficial)
        if not oficial:
            self.cnes.clear()
            self.cnes.setStyleSheet("")

    # -------------------- OK / CANCELAR --------------------
    def on_buttonBox_accepted(self):
        """Valida, atualiza no banco e emite o DTO."""
        self._resetar_estilos()

        oficial = self.radioButton_2.isChecked()

        # Validação
        campos_invalidos = []
        if not self.placa.text().strip(): campos_invalidos.append(self.placa)
        if not self.chassi.text().strip(): campos_invalidos.append(self.chassi)
        if not self.denominacao.text().strip(): campos_invalidos.append(self.denominacao)
        if oficial and not self.cnes.text().strip(): campos_invalidos.append(self.cnes)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        # Monta DTO (útil para quem ouvir o sinal submitted)
        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),
            placa=self.placa.text().strip(),
            chassi=self.chassi.text().strip(),
            tipo_aquisicao=self.tipo.currentText().strip(),
            data_aquisicao=self.data.date(),
            ano=self.ano.value(),
            cnes=self.cnes.text().strip(),
            denominacao=self.denominacao.text().strip(),
        )

        # Converte QDate -> date
        d = date(dto.data_aquisicao.year(), dto.data_aquisicao.month(), dto.data_aquisicao.day())

        # Obtém IDs das combos (userData)
        id_modelo = self.modelo_combo.currentData()
        id_forma = self.tipo.currentData()

        # Atualiza no banco localizando pelo CHASSI atual
        try:
            ok = self._db.atualizar_ambulancia_por_chassi(
                chassi_ref=dto.chassi,
                id_modelo=int(id_modelo),
                id_forma_aquisicao=int(id_forma),
                data_aquisicao=d,
                uso_oficial=oficial,
                cnes=(dto.cnes if oficial else None),
                placa=dto.placa,
                novo_chassi=dto.chassi,          
                denominacao=dto.denominacao,     
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro ao salvar", f"Não foi possível atualizar:\n{e}")
            return

        if not ok:
            QMessageBox.warning(self, "Aviso", "Nenhuma linha atualizada. Verifique o chassi informado.")
            return

        # Feedback + sinais
        self.submitted.emit(dto)
        QMessageBox.information(self, "Sucesso", "Atualização salva com sucesso!")
        self._carregar_sugestoes_do_bd()  # atualiza autocompletes após salvar
        self.gotomodificar.emit()

    def on_buttonBox_rejected(self):
        self._resetar_estilos()
        self.gotomenu.emit()

    # -------------------- Proteção contra fechamento --------------------
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.parent() is not None:
            self.gotomenu.emit()
            event.ignore()
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
            if cls == "QLineEdit": w.setStyleSheet(estilo_line)
            elif cls == "QComboBox": w.setStyleSheet(estilo_combo)
            elif cls == "QSpinBox": w.setStyleSheet(estilo_spin)
            elif cls == "QDateEdit": w.setStyleSheet(estilo_date)
            else: w.setStyleSheet(estilo_line)