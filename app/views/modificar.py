from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
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

        # --- Aliases para clareza (opcional): no .ui, 'lineEdit' é a Placa ---
        self.placa = self.lineEdit   # QLineEdit (rótulo "Placa")
        self.modelo_combo = self.comboBox  # QComboBox (rótulo "Modelo")

        # Conexões dos botões OK/Cancel
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        # Remover destaque de erro assim que o usuário começar a digitar/alterar
        self.placa.textChanged.connect(lambda _: self.placa.setStyleSheet(""))
        self.chassi.textChanged.connect(lambda _: self.chassi.setStyleSheet(""))
        self.cnes.textChanged.connect(lambda _: self.cnes.setStyleSheet(""))
        self.denominacao.textChanged.connect(lambda _: self.denominacao.setStyleSheet(""))
        self.modelo_combo.currentIndexChanged.connect(lambda _: self.modelo_combo.setStyleSheet(""))
        self.ano.valueChanged.connect(lambda _: self.ano.setStyleSheet(""))
        self.data.dateChanged.connect(lambda _: self.data.setStyleSheet(""))

        # (Opcional) defaults
        # self.data.setDate(QDate.currentDate())
        # self.data.setCalendarPopup(True)

    def on_buttonBox_accepted(self):
        """Valida, destaca em vermelho e mostra UMA mensagem genérica se houver campos vazios."""
        self._resetar_estilos()

        campos_invalidos = []

        # Campos obrigatórios:
        # - Placa (lineEdit)
        if not self.placa.text().strip():
            campos_invalidos.append(self.placa)

        # - Chassi
        if not self.chassi.text().strip():
            campos_invalidos.append(self.chassi)

        # - CNES
        if not self.cnes.text().strip():
            campos_invalidos.append(self.cnes)

        if not self.denominacao.text().strip():
            campos_invalidos.append(self.denominacao)

        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            campos_invalidos[0].setFocus()
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        # Monta o DTO com o mapeamento correto do seu .ui:
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

        self.submitted.emit(dto)
        QMessageBox.information(self, "Sucesso", "Cadastro salvo com sucesso!")
        self.close()

    def on_buttonBox_rejected(self):
        self.close()

    # ---------- Helpers de validação/estilo ----------

    def _resetar_estilos(self):
        """Remove bordas vermelhas dos campos (volta ao estilo padrão)."""
        for w in (self.placa, self.chassi, self.cnes, self.denominacao):
            w.setStyleSheet("")
        self.modelo_combo.setStyleSheet("")
        self.ano.setStyleSheet("")
        self.data.setStyleSheet("")

    def _destacar_campos_vazios(self, widgets):
        """Aplica borda vermelha nos widgets passados."""
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
                # fallback
                w.setStyleSheet(estilo_line)


# Exemplo de uso
def on_submitted(dto: AmbulanciaDTO):
    print("Dados salvos:", dto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Modificar()
    w.submitted.connect(on_submitted)
    w.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Modificar()
    w.submitted.connect(on_submitted)
    w.show()
    sys.exit(app.exec())       


