from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication, QDialogButtonBox
from PySide6.QtGui import QCloseEvent
from ui_telademodificar import Ui_modificar
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

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Modificar Dados da Ambulância")

        # Aliases conforme seu .ui
        self.placa = self.lineEdit           
        self.modelo_combo = self.comboBox     

        # -------------------- Conexões dos botões OK/Cancel --------------------
        # 1) Conexões padrão (funcionam se o buttonBox tiver roles Ok/Cancel)
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        # 2) Opção 1 (garantia): conecta diretamente os botões Ok/Cancel
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

    # -------------------- OK / CANCELAR --------------------

    def on_buttonBox_accepted(self):
        """Valida, emite o DTO e volta para o Menu (sem fechar o widget)."""
        print("[Modificar] OK clicado")
        self._resetar_estilos()

        campos_invalidos = []

        # Valida obrigatórios
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

        # Monta DTO
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


# # Exemplo de uso local
# def on_submitted(dto: AmbulanciaDTO):
#     print("Dados salvos:", dto)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Modificar()
#     w.submitted.connect(on_submitted)
#     w.show()
#     sys.exit(app.exec())
