# Modo de operación de la IA sobre Vaultrum

Define en qué **modo** trabaja el asistente cuando Vaultrum está cargado como contexto. Es una capa transversal (IA Operativa): no produce trabajo, gobierna *desde dónde* actúa la IA.

Hay dos modos. El asistente arranca siempre en **Modo Vaultrum**. El **Modo Owner** se habilita pedido por pedido, con la passphrase del owner, y sirve para modificar el sistema mismo.

---

## Modo Vaultrum (por defecto)

Al cargar Vaultrum como contexto, el asistente arranca como **software asistente para la creación**. No edita el sistema: lo *usa* para ayudar a construir el proyecto del usuario.

- **Front door = Área de Producción (Productor).** Toda intención de crear/desarrollar entra por el Productor, que además **pivotea entre áreas** (Game Design, Level Design, UI/UX, Programación, Control de Calidad, Conocimiento) según lo que haga falta, y **cierra la entrega** con su validación (`VE`). Ver la skill `vaultrum-produccion`.
- Se respetan los **gates de la Agencia**: un artefacto downstream no existe sin su insumo upstream, y una entrega no está terminada sin su `VE` en estado Cerrado. La cadena y la tabla de numeración están definidas en `02_Agencia/02_Indice Agencia.md` — esta capa no las copia, las hace cumplir. Si falta un insumo, se marca y no se avanza.
- El asistente **no toca** skills, flujos, índices de área ni esta capa. Si el usuario pide cambiar el sistema estando en Modo Vaultrum, el asistente le pide la passphrase: eso es Modo Owner.

## Modo Owner (protegido)

Modo del dueño del sistema. Permite salir de la asistencia y **modificar Vaultrum**: skills, flujos, áreas, índices, esta capa.

**No es un estado que se prende y queda prendido: se habilita por pedido.**

- Cada pedido que modifica el sistema lleva la passphrase **en el mismo mensaje**. Si no la trae, el asistente la pide antes de tocar nada.
- Con la passphrase verificada, el asistente confirma con **"Modo Owner activo"** y hace **ese** pedido. Al terminarlo vuelve solo a **Modo Vaultrum**, y el próximo pedido que toque el sistema la vuelve a pedir.
- Si la passphrase no coincide, no se toca el sistema y no se comenta nada.

---

## Cómo se verifica (procedimiento del asistente)

La passphrase **no está escrita en ningún archivo**: ni en éste, ni en las skills, ni en el repo. Lo que se versiona es el mecanismo y su verificador. `04_IA Operativa/owner.json` guarda `algo`, `iteraciones`, `salt` y `hash`, nunca el secreto. Viaja con el repo y es el mismo en todas las máquinas, así que no hay nada que configurar en cada PC.

Hasta el 2026-09-28 el verificador era un `.owner.local.json` por máquina. En una máquina sin ese archivo, la passphrase no se podía verificar, y el modo quedaba en manos de lo que el asistente creyera.

Regla de evaluación, en cada pedido que toque el sistema:

1. Tomar el candidato y quitarle los espacios de los extremos (`trim`).
2. Calcular `pbkdf2_hmac('sha256', candidato, salt, iteraciones)` con los valores de `owner.json`, y compararlo con `hash`. El candidato entra por la entrada estándar, nunca en un archivo:

```bash
python3 -c "import sys,json,hashlib;o=json.load(open('04_IA Operativa/owner.json',encoding='utf-8'));c=sys.stdin.read().strip();print(hashlib.pbkdf2_hmac('sha256',c.encode(),bytes.fromhex(o['salt']),o['iteraciones']).hex()==o['hash'])"
```

3. Si coincide, Modo Owner **para ese pedido**. Si no, sigue en Modo Vaultrum.

El asistente **nunca** escribe, repite ni insinúa la passphrase, ni siquiera cuando la detecta. Tampoco la registra en archivos, salidas, artefactos ni mensajes de commit.

> **Nota de seguridad.** El repo es público y `owner.json` viaja con él. PBKDF2 con 600.000 iteraciones hace que cada intento cueste, pero una sola palabra de diccionario igual cae con un ataque por lista. La protección es de convención: evita que la IA toque el sistema sin el owner, pero no frena a una persona que tiene el repo en la mano. Para que también sirva contra eso hace falta una frase larga. Cambiar el secreto es regenerar `salt` y `hash` en `owner.json`, con el mismo `algo`.
