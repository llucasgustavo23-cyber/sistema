# app/scripts/seed_admin.py
from __future__ import annotations

import argparse
import sys
from getpass import getpass

from app.database import Database


def main():
    ap = argparse.ArgumentParser(
        description="Seed: cria um usuário inicial no banco (senha com PBKDF2)."
    )
    ap.add_argument("--usuario", required=True, help="Login do usuário (ex.: admin)")
    ap.add_argument("--role", choices=["admin", "operador", "visualizador"], default="admin",
                    help="Perfil do usuário (default: admin)")
    ap.add_argument("--password", help="Senha do usuário (se não passar, será solicitada de forma oculta)")
    ap.add_argument("--create-tables", action="store_true",
                    help="(Opcional) Garante colunas necessárias no schema antes de criar o usuário.")
    args = ap.parse_args()

    # Solicitar senha se não informada
    if not args.password:
        p1 = getpass("Defina a senha do usuário: ")
        p2 = getpass("Confirme a senha: ")
        if p1 != p2:
            print("As senhas não coincidem. Abortando.", file=sys.stderr)
            sys.exit(1)
        args.password = p1

    try:
        # Se sua tabela já tem todas as colunas, você pode deixar create-tables de fora
        db = Database(ensure_schema=args.create_tables)
    except Exception as e:
        print(f"[Seed] Falha ao conectar no banco: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        new_id = db.criar_usuario(args.usuario, args.password, args.role)
        print(f"[Seed] Usuário criado com sucesso! id={new_id}, user={args.usuario}, role={args.role}")
        print("IMPORTANTE: guarde a senha com segurança.")
        sys.exit(0)
    except ValueError as ve:
        # Provável usuário já existe
        print(f"[Seed] Não foi possível criar: {ve}", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"[Seed] Erro inesperado ao criar usuário: {e}", file=sys.stderr)
        sys.exit(4)


if __name__ == "__main__":
    main()