# from PySide6.QtWidgets import (
#     QDialog,
#     QGraphicsDropShadowEffect,
#     QMessageBox,
#     QLabel,
#     QComboBox,
# )
# from PySide6.QtCore import Signal, Slot, Qt
# from .ui_usuario import Ui_usuario


# class usuario(QDialog, Ui_usuario):
    
#     submitted = Signal(str, str, str)
#     gotomenu = Signal()

#     def __init__(self, parent=None) -> None:
#         super().__init__(parent)
#         self.setupUi(self)
#         self.setWindowTitle("Cadastrar usuário")
#         self.setModal(True)  # modal por padrão; remova se quiser não modal

#         # Adiciona seletor de perfil ao form (sem alterar .ui)
#         self._add_role_selector()

#         # Efeito visual suave no card (não altera o .ui)
#         self._apply_shadow()

#         # Conectar eventos/ações
#         self._wire()

#     # ---------------------------------------------------------------------
#     # Conexões
#     # ---------------------------------------------------------------------
#     def _wire(self) -> None:
#         # Botão principal "Cadastrar"
#         self.btnEntrar.clicked.connect(self._on_submit)
#         self.lineEdit_2.returnPressed.connect(self._on_submit)

#         # Garantir que o campo de senha esteja como password (o UI já define, mas reforçamos)
#         try:
#             self.lineEdit_2.setEchoMode(self.lineEdit_2.EchoMode.Password)
#         except Exception:
#             pass

#     # ---------------------------------------------------------------------
#     # Injeta o seletor de perfil no formulário (sem mexer no .ui)
#     # ---------------------------------------------------------------------
#     def _add_role_selector(self) -> None:
#         """
#         Insere uma linha 'Perfil' no formLayout do UI com um QComboBox,
#         mantendo a compatibilidade total com o layout existente.
#         """
#         # Cria os widgets
#         self.lblPerfil = QLabel("Perfil", self.card)
#         self.cmbRole = QComboBox(self.card)
#         # Perfis recomendados
#         self.cmbRole.addItems(["admin", "operador", "visualizador"])
#         # Insere como a próxima linha do form
#         # (sua ordem atual: 0=Usuário, 1=Senha; então essa entra como 2)
#         try:
#             self.formLayout.addRow(self.lblPerfil, self.cmbRole)
#         except Exception as e:
#             print("[usuario] Aviso: não foi possível inserir combo de perfil:", e)

#     # ---------------------------------------------------------------------
#     # Efeitos
#     # ---------------------------------------------------------------------
#     def _apply_shadow(self) -> None:
#         """Sombra suave no card (se disponível)."""
#         try:
#             effect = QGraphicsDropShadowEffect(self.card)
#             effect.setBlurRadius(28)
#             effect.setOffset(0, 8)
#             effect.setColor(Qt.black)
#             self.card.setGraphicsEffect(effect)
#         except Exception as e:
#             print("[usuario] Aviso: não foi possível aplicar sombra ao card:", e)

#     # ---------------------------------------------------------------------
#     # Submissão
#     # ---------------------------------------------------------------------
#     @Slot()
#     def _on_submit(self) -> None:
#         usuario_txt = self.lineEdit.text().strip()
#         senha_txt = self.lineEdit_2.text().strip()
#         role = self.cmbRole.currentText() if hasattr(self, "cmbRole") else "visualizador"

#         # Validação mínima
#         if not usuario_txt:
#             self._feedback_inline("Informe o usuário.")
#             self.lineEdit.setFocus()
#             return
#         if not senha_txt:
#             self._feedback_inline("Informe a senha.")
#             self.lineEdit_2.setFocus()
#             return

#         # Emite para quem abriu tratar (DAO/controle)
#         self.submitted.emit(usuario_txt, senha_txt, role)

#         # Feedback opcional ao usuário
#         self._feedback_inline("Usuário cadastrado com sucesso!", success=True)

#         # Fecha o diálogo automaticamente após cadastrar
#         self.accept()

#         # Se quiser voltar ao menu automaticamente (MainWindow conecta gotomenu -> show_menu)
#         # self.gotomenu.emit()

#     # ---------------------------------------------------------------------
#     # Utilitários
#     # ---------------------------------------------------------------------
#     def _feedback_inline(self, mensagem: str, success: bool = False) -> None:
#         """Mostra feedback no lblSubtitulo (mantém o padrão visual do UI)."""
#         color = "#16a34a" if success else "#ff6b6b"
#         try:
#             self.lblSubtitulo.setText(mensagem)
#             self.lblSubtitulo.setStyleSheet(f"color: {color}; font-weight: 600;")
#         except Exception:
#             pass

#     def get_data(self) -> tuple[str, str, str]:
#         """Retorna (usuario, senha, role) sem validação."""
#         role = self.cmbRole.currentText() if hasattr(self, "cmbRole") else "visualizador"
#         return self.lineEdit.text(), self.lineEdit_2.text(), role

#     def set_data(self, usuario: str = "", senha: str = "", role: str = "visualizador") -> None:
#         """Preenche os campos (útil para edição)."""
#         self.lineEdit.setText(usuario or "")
#         self.lineEdit_2.setText(senha or "")
#         try:
#             idx = self.cmbRole.findText(role)
#             if idx >= 0:
#                 self.cmbRole.setCurrentIndex(idx)
#         except Exception:
#             pass

#     def clear_form(self) -> None:
#         """Limpa os campos e reseta feedback."""
#         self.lineEdit.clear()
#         self.lineEdit_2.clear()
#         try:
#             self.lblSubtitulo.setText("Crie um usuário para continuar")
#             self.lblSubtitulo.setStyleSheet("color: #6b7280;")
#         except Exception:
#             pass

#     # ---------------------------------------------------------------------
#     # Teclas padrão de diálogo (Esc fecha)
#     # ---------------------------------------------------------------------
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.reject()
#             return
#         super().keyPressEvent(event)
        
# from PySide6.QtWidgets import (
#     QDialog,
#     QGraphicsDropShadowEffect,
#     QMessageBox,
#     QLabel,
#     QComboBox,
# )
# from PySide6.QtCore import Signal, Slot, Qt
# from .ui_usuario import Ui_usuario

from PySide6.QtWidgets import (
    QDialog,
    QGraphicsDropShadowEffect,
    QMessageBox,
    QLabel,
    QComboBox,
)
from PySide6.QtCore import Signal, Slot, Qt
from .ui_usuario import Ui_usuario

class usuario(QDialog, Ui_usuario):
    
    submitted = Signal(str, str, str)   # usuario, senha, role
    gotomenu = Signal()
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastrar usuário")
        self.setModal(True)

        # Injeta selector de perfil no form
        self._add_role_selector()

        # Coloca sombra no card
        self._apply_shadow()

        # Liga sinais e eventos
        self._wire()

    # ------------------------------------------------------------------
    # Conexões
    # ------------------------------------------------------------------
    def _wire(self) -> None:
        # Botão cadastrar
        self.btnEntrar.clicked.connect(self._on_submit)

        # Botão cancelar → fecha o diálogo e emite sinal para o menu
        self.btnCancelar.clicked.connect(self.reject)
        self.btnCancelar.clicked.connect(self.gotomenu.emit)

        # Enter no campo senha → cadastrar
        self.lineEdit_2.returnPressed.connect(self._on_submit)

        # Garante que campo senha esteja como password
        try:
            self.lineEdit_2.setEchoMode(self.lineEdit_2.EchoMode.Password)
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Insere o combo "Perfil" dinamicamente
    # ------------------------------------------------------------------
    def _add_role_selector(self) -> None:
        self.lblPerfil = QLabel("Perfil", self.card)
        self.cmbRole = QComboBox(self.card)

        # Perfis disponíveis
        self.cmbRole.addItems(["admin", "operador", "visualizador"])

        # Adiciona no form layout do .ui
        try:
            self.formLayout.addRow(self.lblPerfil, self.cmbRole)
        except Exception as e:
            print("[usuario] Erro ao adicionar perfil:", e)

    # ------------------------------------------------------------------
    # Aplica sombra no card
    # ------------------------------------------------------------------
    def _apply_shadow(self) -> None:
        try:
            effect = QGraphicsDropShadowEffect(self.card)
            effect.setBlurRadius(28)
            effect.setOffset(0, 8)
            effect.setColor(Qt.black)
            self.card.setGraphicsEffect(effect)
        except Exception as e:
            print("[usuario] Erro na sombra:", e)

    # ------------------------------------------------------------------
    # BOTÃO CADASTRAR
    # ------------------------------------------------------------------
    @Slot()
    def _on_submit(self) -> None:
        usuario_txt = self.lineEdit.text().strip()
        senha_txt = self.lineEdit_2.text().strip()
        role = self.cmbRole.currentText()

        # VALIDAÇÃO
        if not usuario_txt:
            self._feedback_inline("Informe o usuário.")
            self.lineEdit.setFocus()
            return

        if not senha_txt:
            self._feedback_inline("Informe a senha.")
            self.lineEdit_2.setFocus()
            return

        self.submitted.emit(usuario_txt, senha_txt, role)

        self._feedback_inline("Usuário cadastrado com sucesso!", success=True)

        # Limpa os campos para novo cadastro
        self.clear_form()
        self.lineEdit.setFocus()

    # ------------------------------------------------------------------
    # Feedback visual
    # ------------------------------------------------------------------
    def _feedback_inline(self, mensagem: str, success: bool = False) -> None:
        color = "#16a34a" if success else "#ff6b6b"
        try:
            self.lblSubtitulo.setText(mensagem)
            self.lblSubtitulo.setStyleSheet(f"color: {color}; font-weight: 600;")
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def get_data(self) -> tuple[str, str, str]:
        return (
            self.lineEdit.text(),
            self.lineEdit_2.text(),
            self.cmbRole.currentText(),
        )

    def set_data(self, usuario: str = "", senha: str = "", role: str = "visualizador") -> None:
        self.lineEdit.setText(usuario)
        self.lineEdit_2.setText(senha)

        idx = self.cmbRole.findText(role)
        if idx >= 0:
            self.cmbRole.setCurrentIndex(idx)

    def clear_form(self) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        try:
            self.lblSubtitulo.setText("Crie um usuário para continuar")
            self.lblSubtitulo.setStyleSheet("color: rgba(255,255,255,0.75);")
        except Exception:
            pass

    # ------------------------------------------------------------------
    # ESC fecha o diálogo e volta ao menu
    # ------------------------------------------------------------------
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.reject()
            self.gotomenu.emit()
            return
        super().keyPressEvent(event)