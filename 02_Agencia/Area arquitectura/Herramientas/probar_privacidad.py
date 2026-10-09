#!/usr/bin/env python3
"""Pruebas de privacidad.py. Cada caso arma un repo git de juguete en un
directorio temporal, sin tocar el vault.

  python3 probar_privacidad.py
"""
import os, sys, shutil, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import privacidad as P


def repo(archivos, versionar):
    d = tempfile.mkdtemp(prefix='vaultrum_priv_')
    subprocess.run(['git', 'init', '-q', d], check=True)
    for ruta, txt in archivos.items():
        full = os.path.join(d, ruta)
        os.makedirs(os.path.dirname(full) or d, exist_ok=True)
        if txt is None:
            os.makedirs(full, exist_ok=True)
        else:
            open(full, 'w', encoding='utf-8').write(txt)
    for ruta in versionar:
        subprocess.run(['git', '-C', d, 'add', '-f', ruta], check=True)
    return d


def tipos(d):
    fallas, _, _ = P.medir(d)
    shutil.rmtree(d, ignore_errors=True)
    return [f[0] for f in fallas]


CASOS = []
def caso(f):
    CASOS.append(f)
    return f


@caso
def nombrar_un_proyecto_en_el_sistema_falla():
    d = repo({'06_Proyectos/Secreto': None, 'nota.md': 'Como hizo Secreto, el TL...'}, ['nota.md'])
    assert tipos(d) == ['nombra un proyecto privado']

@caso
def la_leccion_sin_el_nombre_pasa():
    d = repo({'06_Proyectos/Secreto': None, 'nota.md': 'Como hizo un proyecto real...'}, ['nota.md'])
    assert tipos(d) == []

@caso
def palabra_entera_y_mayusculas():
    d = repo({'06_Proyectos/Rayo': None,
              'nota.md': 'el rayo variable. RayoDoble no es el proyecto. Rayos tampoco.'}, ['nota.md'])
    assert tipos(d) == []

@caso
def el_falso_positivo_se_declara_en_la_lista_local():
    d = repo({'06_Proyectos/Rayo': None,
              '06_Proyectos/privado.txt': 'nota.md | Rayo | palabra comun\n',
              'nota.md': 'Rayo de sol: una palabra comun en una nota.'}, ['nota.md'])
    assert tipos(d) == []

@caso
def la_excepcion_no_cubre_otro_archivo():
    d = repo({'06_Proyectos/Rayo': None,
              '06_Proyectos/privado.txt': 'nota.md | Rayo | palabra comun\n',
              'otra.md': 'Rayo cerro su VE.'}, ['otra.md'])
    assert tipos(d) == ['nombra un proyecto privado']

@caso
def un_termino_extra_de_la_lista_cuenta():
    d = repo({'06_Proyectos/privado.txt': 'NombreComercial\n',
              'nota.md': 'Evidencia: NombreComercial, BUG-999.'}, ['nota.md'])
    assert tipos(d) == ['nombra un proyecto privado']

@caso
def una_nota_suelta_de_proyectos_tambien_es_privada():
    d = repo({'06_Proyectos/Notas sueltas.md': 'x',
              'nota.md': 'ver Notas sueltas'}, ['nota.md'])
    assert tipos(d) == ['nombra un proyecto privado']

@caso
def un_archivo_de_proyectos_versionado_falla():
    d = repo({'06_Proyectos/Secreto/cuaderno.md': 'x'}, ['06_Proyectos/Secreto/cuaderno.md'])
    assert tipos(d) == ['proyecto versionado']

@caso
def un_artefacto_versionado_falla_aunque_este_afuera():
    d = repo({'02_Agencia/TL-001_Algo.md': 'x', '02_Agencia/RA-001_Regla.md': 'x'},
             ['02_Agencia/TL-001_Algo.md', '02_Agencia/RA-001_Regla.md'])
    assert tipos(d) == ['historial versionado']

@caso
def un_registro_y_un_local_versionados_fallan():
    d = repo({'00_Registro_arq.md': 'x', 'excepciones.local.txt': 'x'},
             ['00_Registro_arq.md', 'excepciones.local.txt'])
    assert sorted(tipos(d)) == ['archivo local versionado', 'historial versionado']

@caso
def el_guion_bajo_de_un_artefacto_es_borde():
    d = repo({'06_Proyectos/Rayo': None,
              'nota.md': 'Evidencia: `SOL-001_Arquitectura_Rayo` y VE-003_Rayo.'}, ['nota.md'])
    assert tipos(d) == ['nombra un proyecto privado', 'nombra un proyecto privado']

@caso
def mide_lo_que_esta_en_stage_y_no_el_disco():
    d = repo({'06_Proyectos/Rayo': None, 'nota.md': 'Como hizo Rayo.'}, ['nota.md'])
    open(os.path.join(d, 'nota.md'), 'w', encoding='utf-8').write('limpio en disco')
    assert tipos(d) == ['nombra un proyecto privado']

@caso
def sin_proyectos_locales_igual_mide_el_paquete():
    d = repo({'nota.md': 'nada privado'}, ['nota.md'])
    assert tipos(d) == []

@caso
def el_indice_de_proyectos_no_es_un_nombre_privado():
    d = repo({'06_Proyectos/00_Proyectos.md': 'x', 'nota.md': 'tus proyectos: 00_Proyectos'}, ['nota.md'])
    assert tipos(d) == []

@caso
def un_binario_no_se_lee_como_texto():
    d = repo({'06_Proyectos/Secreto': None}, [])
    open(os.path.join(d, 'img.png'), 'wb').write(b'\x89PNG\0\0Secreto')
    subprocess.run(['git', '-C', d, 'add', '-f', 'img.png'], check=True)
    assert tipos(d) == []


def main():
    fallas = 0
    for f in CASOS:
        try:
            f()
            print('  ok     %s' % f.__name__)
        except AssertionError as e:
            fallas += 1
            print('  FALLA  %s %s' % (f.__name__, e))
    print('\n%d casos, %d fallas' % (len(CASOS), fallas))
    return 1 if fallas else 0


if __name__ == '__main__':
    sys.exit(main())
