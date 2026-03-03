# app/views/cadastro.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QApplication, QDialogButtonBox
)
from PySide6.QtGui import QCloseEvent

from ui_teladecadastro import UI_cadastro  # ⬅️ ajuste se o arquivo tiver outro nome
import sys


@dataclass
class AmbulanciaDTO:
    modelo: str          # texto do modelo (pego do comboBox)
    placa: str           # texto da placa (no seu .ui é o QLineEdit 'modelo', ver abaixo)
    chassi: str
    tipo_aquisicao: str
    data_aquisicao: QDate
    ano: int
    cnes: str
    denominacao: str


class Cadastro(QWidget, UI_cadastro):
    gotomenu = Signal()                       # usado pela MainWindow para voltar ao Menu
    submitted = Signal(AmbulanciaDTO)         # opcional: quem quiser ouvir o DTO salvo

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Ambulâncias")

        # --- Aliases conforme o seu .ui ---
        # Atenção: no seu .ui, os rótulos parecem invertidos:
        #   lbl_modelo = "Placa"   → o QLineEdit correspondente chama-se 'modelo'
        #   lbl_placa  = "Modelo"  → o 'comboBox' tem opções 1..5 (vou tratá-lo como "modelo")
        #
        # Para manter compatível com o seu DTO (e com a tela Modificar), farei:
        #   placa        ← self.modelo.text()
        #   modelo_combo ← self.comboBox.currentText()
        self.placa = self.modelo               # QLineEdit (rotulado no .ui como "Placa")
        self.modelo_combo = self.comboBox      # QComboBox (rotulado no .ui como "Modelo")
        self.chassi_edit = self.chassi         # QLineEdit
        self.tipo_combo = self.tipo            # QComboBox
        self.data_edit = self.data             # QDateEdit
        self.ano_spin = self.ano               # QSpinBox
        self.cnes_edit = self.cnes             # QLineEdit
        self.denominacao_edit = self.denominacao  # QLineEdit

        # -------------------- Conexões dos botões OK/Cancel --------------------
        # 1) Padrão: accepted/rejected (funciona se o buttonBox tiver roles Ok/Cancel configurados)
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        # 2) Opção 1 (garantia): conecta diretamente os botões Ok/Cancel
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
        self.placa.textChanged.connect(lambda _: self.placa.setStyleSheet(""))
        self.chassi_edit.textChanged.connect(lambda _: self.chassi_edit.setStyleSheet(""))
        self.cnes_edit.textChanged.connect(lambda _: self.cnes_edit.setStyleSheet(""))
        self.denominacao_edit.textChanged.connect(lambda _: self.denominacao_edit.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.ano_spin.valueChanged.connect(lambda _: self.ano_spin.setStyleSheet(""))
        self.data_edit.dateChanged.connect(lambda _: self.data_edit.setStyleSheet(""))

    # -------------------- OK / CANCELAR --------------------

    def on_buttonBox_accepted(self):
        """Valida, emite o DTO e volta para o Menu (sem fechar o widget)."""
        self._resetar_estilos()

        campos_invalidos = []

        # Valida obrigatórios
        if not self.placa.text().strip():               # placa no seu .ui = QLineEdit 'modelo'
            campos_invalidos.append(self.placa)
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

        # Monta DTO
        dto = AmbulanciaDTO(
            modelo=self.modelo_combo.currentText().strip(),   # do comboBox
            placa=self.placa.text().strip(),                  # do QLineEdit 'modelo' no .ui
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

        # Não fecha a página do stack; apenas peça para voltar ao menu
        self.gotomenu.emit()

    def on_buttonBox_rejected(self):
        """Cancelar → voltar para o Menu (sem fechar o widget)."""
        self._resetar_estilos()
        self.gotomenu.emit()

    # -------------------- Proteção contra fechamento --------------------

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        Se este widget estiver dentro do QStackedWidget (tem parent),
        ignoramos o fechamento e apenas emitimos gotomenu.
        """
        if self.parent() is not None:
            self.gotomenu.emit()
            event.ignore()
        else:
            event.accept()

    # -------------------- Helpers de validação/estilo --------------------

    def _resetar_estilos(self):
        for w in (self.placa, self.chassi_edit, self.cnes_edit, self.denominacao_edit):
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


# # Exemplo local
# def on_submitted(dto: AmbulanciaDTO):
#     print("Dados salvos:", dto)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Cadastro()
#     w.submitted.connect(on_submitted)
#     w.show()
#     sys.exit(app.exec())
