# modificar.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from datetime import date

from PySide6.QtCore import Signal, QDate, Qt, QStringListModel
from PySide6.QtWidgets import (
    QDialog, QWidget, QMessageBox, QDialogButtonBox, QCompleter, QButtonGroup
)

from ui_modifica import Ui_modifca
from app.database import Database


@dataclass
class AmbulanciaDTO:
    modelo: str
    placa: str
    chassi: str
    tipo_aquisicao: str
    data_aquisicao: QDate
    ano: int
    cnes: str


class Modificar(QDialog, Ui_modifca):
    submitted = Signal(AmbulanciaDTO)

    def __init__(
        self,
        chassi: str = "",
        provider=None,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self._provider = provider
        self._db = Database()
        self._chassi_inicial = chassi.strip()

        self.setupUi(self)
        self.setWindowTitle("Modificar Dados da Ambulância")
        self.setModal(True)

        # Corrige fundo cinza nas labels
        self.card.setStyleSheet(
            "#card {"
            "  background: #ffffff;"
            "  border-radius: 12px;"
            "  padding: 20px;"
            "  border: 1px solid #dddddd;"
            "}"
            "QLabel {"
            "  background: transparent;"
            "  font: 600 10pt 'Segoe UI';"
            "  color: #444;"
            "  margin-bottom: 4px;"
            "}"
            "QLineEdit, QComboBox, QDateEdit, QSpinBox {"
            "  background: #f7f7f7;"
            "  border: 1px solid #cfcfcf;"
            "  border-radius: 6px;"
            "  padding: 8px 10px;"
            "  font: 10pt 'Segoe UI';"
            "}"
        )

        self.card.setStyleSheet(
            "#card {"
            "  background: #ffffff;"
            "  border-radius: 12px;"
            "  padding: 20px;"
            "  border: 1px solid #dddddd;"
            "}"
            "QLabel {"
            "  background: transparent;"
            "  font: 600 10pt 'Segoe UI';"
            "  color: #444;"
            "  margin-bottom: 4px;"
            "}"
            "QRadioButton {"
            "  background: transparent;"
            "  font: 10pt 'Segoe UI';"
            "  color: #444;"
            "}"
            "QRadioButton::indicator {"
            "  width: 16px;"
            "  height: 16px;"
            "  border-radius: 8px;"
            "  border: 2px solid #9ca3af;"
            "  background: #ffffff;"
            "}"
            "QRadioButton::indicator:checked {"
            "  border: 2px solid #4f46e5;"
            "  background: #4f46e5;"
            "}"
            "QRadioButton::indicator:hover {"
            "  border: 2px solid #4f46e5;"
            "}"
            "QLineEdit, QComboBox, QDateEdit, QSpinBox {"
            "  background: #f7f7f7;"
            "  border: 1px solid #cfcfcf;"
            "  border-radius: 6px;"
            "  padding: 8px 10px;"
            "  font: 10pt 'Segoe UI';"
            "}"
        )
        # Aliases do .ui
        self.placa = self.lineEdit
        self.modelo_combo = self.comboBox
        self.cnes_edit = self.cnes

        # Grupo exclusivo radio buttons
        self._grupo_categoria = QButtonGroup(self)
        self._grupo_categoria.setExclusive(True)
        self._grupo_categoria.addButton(self.radioButton_2)  # Oficial
        self._grupo_categoria.addButton(self.radioButton)    # Reserva

        # Models autocomplete
        self._model_placa = QStringListModel([], self)
        self._model_chassi = QStringListModel([], self)
        self._model_cnes = QStringListModel([], self)

        self._setup_completers()
        self._carregar_modelos_do_bd()
        self._carregar_formas_do_bd()
        self._carregar_sugestoes_do_bd()

        if self._provider is not None:
            try:
                self._provider.suggestions_changed.connect(self._sync_sugestoes_do_provider)
                self._sync_sugestoes_do_provider()
            except Exception:
                pass

        # Botões OK/Cancelar
        ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_btn = self.buttonBox.button(QDialogButtonBox.Cancel)
        if ok_btn:
            ok_btn.clicked.connect(self.on_buttonBox_accepted)
        if cancel_btn:
            cancel_btn.clicked.connect(self.on_buttonBox_rejected)

        # Limpa realce ao editar
        self.placa.textChanged.connect(lambda _: self.placa.setStyleSheet(""))
        self.chassi.textChanged.connect(lambda _: self.chassi.setStyleSheet(""))
        self.cnes_edit.textChanged.connect(lambda _: self.cnes_edit.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.ano.valueChanged.connect(lambda _: self.ano.setStyleSheet(""))
        self.data.dateChanged.connect(lambda _: self.data.setStyleSheet(""))

        # Visibilidade CNES
        self.radioButton_2.toggled.connect(self._atualizar_cnes_visibilidade)
        self.radioButton.toggled.connect(self._atualizar_cnes_visibilidade)
        if not (self.radioButton_2.isChecked() or self.radioButton.isChecked()):
            self.radioButton_2.setChecked(True)
        self._atualizar_cnes_visibilidade()

        # Se veio com chassi pré-definido, preenche tudo
        if self._chassi_inicial:
            self.chassi.setText(self._chassi_inicial)
            self._aplicar_filtro_por_chassi()

    # -------------------- Completers --------------------
    def _setup_completers(self):
        def mk(model):
            c = QCompleter(model, self)
            c.setCaseSensitivity(Qt.CaseInsensitive)
            c.setFilterMode(Qt.MatchContains)
            c.setCompletionMode(QCompleter.PopupCompletion)
            return c

        self._comp_placa = mk(self._model_placa)
        self._comp_chassi = mk(self._model_chassi)
        self._comp_cnes = mk(self._model_cnes)

        self.placa.setCompleter(self._comp_placa)
        self.chassi.setCompleter(self._comp_chassi)
        self.cnes_edit.setCompleter(self._comp_cnes)

        try:
            self._comp_chassi.activated[str].connect(lambda _: self._aplicar_filtro_por_chassi())
        except Exception:
            pass
        self.chassi.editingFinished.connect(self._aplicar_filtro_por_chassi)

    # -------------------- Filtro por chassi --------------------
    def _aplicar_filtro_por_chassi(self):
        ch = (self.chassi.text() or "").strip()
        if not ch:
            self._restaurar_sugestoes_globais()
            return

        try:
            rec = self._db.obter_ambulancia_por_chassi(ch)
        except Exception as e:
            print("[Modificar] Erro:", e)
            self._restaurar_sugestoes_globais()
            return

        if not rec:
            self._restaurar_sugestoes_globais()
            return

        self.placa.setText(rec.get("placa") or "")

        try:
            idx = self.modelo_combo.findData(rec.get("id_modelo"))
            if idx >= 0:
                self.modelo_combo.setCurrentIndex(idx)
        except Exception:
            pass

        try:
            idx = self.tipo.findData(rec.get("id_forma_aquisicao"))
            if idx >= 0:
                self.tipo.setCurrentIndex(idx)
        except Exception:
            pass

        try:
            dpy = rec.get("data_aquisicao")
            if dpy:
                self.data.setDate(QDate(dpy.year, dpy.month, dpy.day))
                self.ano.setValue(int(dpy.year))
        except Exception:
            pass

        oficial = bool(rec.get("uso_oficial"))
        self.radioButton_2.setChecked(oficial)
        self.radioButton.setChecked(not oficial)
        self._atualizar_cnes_visibilidade()

        self.cnes_edit.setText(rec.get("cnes") or "" if oficial else "")
        if not oficial:
            self.cnes_edit.clear()

        self._model_placa.setStringList([rec["placa"]] if rec.get("placa") else [])
        self._model_cnes.setStringList([rec["cnes"]] if (oficial and rec.get("cnes")) else [])

    def _restaurar_sugestoes_globais(self):
        try:
            self._model_placa.setStringList(self._db.listar_placas())
            self._model_chassi.setStringList(self._db.listar_chassis())
            self._model_cnes.setStringList(self._db.listar_cnes())
        except Exception as e:
            print("[Modificar] Erro ao restaurar sugestões:", e)

    # -------------------- Carregamentos --------------------
    def _carregar_modelos_do_bd(self):
        self.modelo_combo.clear()
        try:
            for row in self._db.listar_modelos():
                self.modelo_combo.addItem(str(row["nome"]), row["id_modelo"])
        except Exception as e:
            print("[Modificar] Erro modelos:", e)

    def _carregar_formas_do_bd(self):
        try:
            self.tipo.clear()
            for row in self._db.listar_formas_aquisicao():
                self.tipo.addItem(str(row["nome"]), row["id"])
        except Exception as e:
            print("[Modificar] Erro formas:", e)

    def _carregar_sugestoes_do_bd(self):
        try:
            self._model_placa.setStringList(self._db.listar_placas())
            self._model_chassi.setStringList(self._db.listar_chassis())
            self._model_cnes.setStringList(self._db.listar_cnes())
        except Exception as e:
            print("[Modificar] Erro sugestões:", e)

    def _sync_sugestoes_do_provider(self):
        try:
            self._model_placa.setStringList(self._provider.placas() or self._db.listar_placas())
            self._model_chassi.setStringList(self._provider.chassis() or self._db.listar_chassis())
            self._model_cnes.setStringList(self._provider.cnes() or self._db.listar_cnes())
        except Exception:
            self._carregar_sugestoes_do_bd()

    # -------------------- Visibilidade CNES --------------------
    def _atualizar_cnes_visibilidade(self) -> None:
        oficial = self.radioButton_2.isChecked()
        self.lbl_cnes.setVisible(oficial)
        self.cnes_edit.setVisible(oficial)
        self.cnes_edit.setEnabled(oficial)
        if not oficial:
            self.cnes_edit.clear()
            self.cnes_edit.setStyleSheet("")

    # -------------------- OK / Cancelar --------------------
    def on_buttonBox_accepted(self):
        self._resetar_estilos()
        oficial = self.radioButton_2.isChecked()

        campos_invalidos = []
        if not self.placa.text().strip():
            campos_invalidos.append(self.placa)
        if not self.chassi.text().strip():
            campos_invalidos.append(self.chassi)
        if oficial and not self.cnes_edit.text().strip():
            campos_invalidos.append(self.cnes_edit)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),
            placa=self.placa.text().strip(),
            chassi=self.chassi.text().strip(),
            tipo_aquisicao=self.tipo.currentText().strip(),
            data_aquisicao=self.data.date(),
            ano=self.ano.value(),
            cnes=self.cnes_edit.text().strip(),
        )

        d = date(dto.data_aquisicao.year(), dto.data_aquisicao.month(), dto.data_aquisicao.day())
        id_modelo = self.modelo_combo.currentData()
        id_forma = self.tipo.currentData()

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
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro ao salvar", f"Não foi possível atualizar:\n{e}")
            return

        if not ok:
            QMessageBox.warning(self, "Aviso", "Nenhuma linha atualizada. Verifique o chassi informado.")
            return

        self.submitted.emit(dto)
        QMessageBox.information(self, "Sucesso", "Atualização salva com sucesso!")
        self.accept()

    def on_buttonBox_rejected(self):
        self._resetar_estilos()
        self.reject()

    # -------------------- Helpers --------------------
    def _resetar_estilos(self):
        for w in (self.placa, self.chassi, self.cnes_edit):
            w.setStyleSheet("")
        self.modelo_combo.setStyleSheet("")
        self.ano.setStyleSheet("")
        self.data.setStyleSheet("")

    def _destacar_campos_vazios(self, widgets):
        estilos = {
            "QLineEdit": "QLineEdit { border: 1px solid #d9534f; border-radius: 6px; }",
            "QComboBox": "QComboBox { border: 1px solid #d9534f; border-radius: 6px; }",
            "QSpinBox":  "QSpinBox  { border: 1px solid #d9534f; border-radius: 6px; }",
            "QDateEdit": "QDateEdit { border: 1px solid #d9534f; border-radius: 6px; }",
        }
        for w in widgets:
            cls = w.metaObject().className()
            w.setStyleSheet(estilos.get(cls, estilos["QLineEdit"]))