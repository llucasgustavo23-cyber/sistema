# sugestoes.py
from __future__ import annotations
from typing import Iterable
from dataclasses import dataclass
from PySide6.QtCore import QObject, Signal

@dataclass(frozen=True)
class DTOBase:
    placa: str
    chassi: str
    cnes: str
    denominacao: str

class SugestoesProvider(QObject):
 
    suggestions_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._placas: set[str] = set()
        self._chassis: set[str] = set()
        self._cnes: set[str] = set()
        self._denominacoes: set[str] = set()

    # ---------- Acesso ordenado ----------
    def placas(self) -> list[str]:
        return sorted(self._placas, key=str.lower)

    def chassis(self) -> list[str]:
        return sorted(self._chassis, key=str.lower)

    def cnes(self) -> list[str]:
        return sorted(self._cnes, key=str.lower)

    def denominacoes(self) -> list[str]:
        return sorted(self._denominacoes, key=str.lower)

    # ---------- Carga inicial ou recarga total ----------
    def load_from(self, ambulancias: Iterable[DTOBase]) -> None:
        self._placas.clear(); self._chassis.clear(); self._cnes.clear(); self._denominacoes.clear()
        for a in ambulancias:
            if a.placa: self._placas.add(a.placa)
            if a.chassi: self._chassis.add(a.chassi)
            if a.cnes: self._cnes.add(a.cnes)
            if a.denominacao: self._denominacoes.add(a.denominacao)
        self.suggestions_changed.emit()

    # ---------- Eventos incrementais ----------
    def on_cadastrada(self, a: DTOBase) -> None:
        changed = False
        if a.placa and a.placa not in self._placas:
            self._placas.add(a.placa); changed = True
        if a.chassi and a.chassi not in self._chassis:
            self._chassis.add(a.chassi); changed = True
        if a.cnes and a.cnes not in self._cnes:
            self._cnes.add(a.cnes); changed = True
        if a.denominacao and a.denominacao not in self._denominacoes:
            self._denominacoes.add(a.denominacao); changed = True
        if changed:
            self.suggestions_changed.emit()

    def on_excluida_recarregar(self, ambulancias: Iterable[DTOBase]) -> None:
        """
        Preferível após exclusão: recarregar tudo para não apagar valores ainda usados.
        (Apenas um alias semântico para load_from)
        """
        self.load_from(ambulancias)