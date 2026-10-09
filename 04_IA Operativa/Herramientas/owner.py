#!/usr/bin/env python3
"""Vaultrum - IA Operativa - la passphrase del Modo Owner.

El Modo Owner existe para que el asistente no modifique el sistema sin su dueño.
Pero el dueño depende de la copia: en la tuya, sos vos. Hasta la v1.0 el unico
verificador era owner.json, el del maintainer, y quien clonaba no podia entrar
nunca a Modo Owner en su propia copia -- ni para proponer una mejora.

  python owner.py              crea 04_IA Operativa/owner.local.json con TU passphrase.
                               No se versiona. Si existe, el asistente verifica contra
                               este y no contra owner.json.
  python owner.py --oficial    reescribe owner.json, el verificador que viaja con el
                               repo. Solo para el maintainer.

La passphrase se pide sin eco y nunca se escribe: se guarda salt + hash
(PBKDF2-SHA256, 600.000 iteraciones). Usa una frase de varias palabras: el hash
de owner.json es publico, y una palabra sola cae con un diccionario.
"""
import os, sys, json, getpass, hashlib

ITERACIONES = 600000
MINIMO = 16


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 04_IA Operativa
    oficial = '--oficial' in sys.argv
    destino = os.path.join(base, 'owner.json' if oficial else 'owner.local.json')
    print('Passphrase del Modo Owner -> %s' % destino)
    p1 = getpass.getpass('  frase nueva: ').strip()
    if len(p1) < MINIMO or len(p1.split()) < 3:
        print('  Muy corta: usa una frase de tres palabras o mas, y %d caracteres o mas.' % MINIMO)
        return 1
    if getpass.getpass('  repetila:    ').strip() != p1:
        print('  No coinciden. No se escribio nada.')
        return 1
    salt = os.urandom(16)
    datos = {'algo': 'pbkdf2_sha256', 'iteraciones': ITERACIONES, 'salt': salt.hex(),
             'hash': hashlib.pbkdf2_hmac('sha256', p1.encode(), salt, ITERACIONES).hex()}
    with open(destino, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)
        f.write('\n')
    print('  Listo. Desde ahora el asistente verifica contra %s.' % os.path.basename(destino))
    return 0


if __name__ == '__main__':
    sys.exit(main())
