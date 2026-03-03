from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from ui_teladecadastro import UI_cadastro
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


class Cadastro(QWidget, UI_cadastro):
    gotomenu = Signal()
    submitted = Signal(AmbulanciaDTO)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Ambulância")

        # Conexões dos botões OK/Cancel
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected)

        # Remover destaque de erro assim que o usuário começar a digitar/alterar
        self.modelo.textChanged.connect(lambda _: self.modelo.setStyleSheet(""))
        self.chassi.textChanged.connect(lambda _: self.chassi.setStyleSheet(""))
        self.cnes.textChanged.connect(lambda _: self.cnes.setStyleSheet(""))
        self.denominacao.textChanged.connect(lambda _: self.denominacao.setStyleSheet(""))
        self.ano.textChanged.connect(lambda _: self.ano.setStyleSheet(""))
        # self.placa.textChanged.connect(lambda _: self.placa.setStyleSheet(""))
        # self.tipo_aquisicao.textChanged.connect(lambda _: self.tipo_aquisicao.setStyleSheet(""))
        # self.data_aquisicao.textChanged.connect(lambda _: self.data_aquisicao.setStyleSheet(""))
                # Se quiser limpar também quando mudar o combo (Modelo)
        self.comboBox.currentIndexChanged.connect(lambda _: self.comboBox.setStyleSheet(""))

        # (Opcional) defaults:
        # self.data.setDate(QDate.currentDate())
        # self.data.setCalendarPopup(True)

    def on_buttonBox_accepted(self):
        """Valida, destaca em vermelho e mostra UMA mensagem genérica se houver campos vazios."""
        # Sempre limpa estilos antes de uma nova validação
        self._resetar_estilos()

        # Campos obrigatórios que vamos validar
        campos_invalidos = []

        # ATENÇÃO: self.modelo (QLineEdit) está rotulado como "Placa" no seu UI
        if not self.modelo.text().strip():
            campos_invalidos.append(self.modelo)

        if not self.chassi.text().strip():
            campos_invalidos.append(self.chassi)

        if not self.cnes.text().strip():
            campos_invalidos.append(self.cnes)

        if not self.ano.text().strip():
            campos_invalidos.append(self.ano)

        if not self.denominacao.text().strip():
            campos_invalidos.append(self.denominacao)

        # if not self.tipo_aquisicao.text().strip():
        #     campos_invalidos.append(self.tipo_aquisicao)
        
        # if not self.data_aquisicao.text().strip():
        #     campos_invalidos.append(self.data_aquisicao)

        # Se houver algum vazio: destaca e mostra UMA mensagem
        if campos_invalidos:
            self._destacar_campos_vazios(campos_invalidos)
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha os campos destacados.")
            return

        # Monta o DTO e segue o fluxo normal
        dto = AmbulanciaDTO(
            modelo=self.comboBox.currentText().strip(),   # "Modelo" (combo)
            placa=self.modelo.text().strip(),             # "Placa" (line edit chamado 'modelo')
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
        for w in (self.modelo, self.chassi, self.cnes, self.denominacao):
            w.setStyleSheet("")
        # Caso tenha aplicado estilo no combo:
        self.comboBox.setStyleSheet("")

    def _destacar_campos_vazios(self, widgets):
        """Aplica borda vermelha nos widgets passados."""
        estilo_erro_line = "QLineEdit { border: 1px solid #d9534f; border-radius: 6px; }"
        estilo_erro_combo = "QComboBox { border: 1px solid #d9534f; border-radius: 6px; }"

        for w in widgets:
            # Aplica estilo apropriado conforme o tipo do widget
            if hasattr(w, "setEditable"):  # heurística simples para QComboBox
                w.setStyleSheet(estilo_erro_combo)
            else:
                w.setStyleSheet(estilo_erro_line)

# Exemplo de uso
def on_submitted(dto: AmbulanciaDTO):
    print("Dados salvos:", dto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Cadastro()
    w.submitted.connect(on_submitted)
    w.show()
    sys.exit(app.exec())


