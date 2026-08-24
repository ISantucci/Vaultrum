## Propósito

El Área de Producción de Vaultrum se encarga de transformar ideas, problemas y objetivos abiertos en salidas productivas claras, realistas y planificables.

Su función es ordenar el trabajo antes de que pase a ejecución, evitando que una idea avance sin criterio, sin alcance definido o sin una planificación mínima.

El área no existe para producir tareas por inercia.

Existe para convertir intención en dirección accionable.

El área es además **dueña de la entrega**: la abre con la intención del usuario y la cierra validando lo construido. Las demás áreas producen su parte; Producción responde por el conjunto.

---

## Entrada del área

- una **intención abierta** del usuario: idea, problema, objetivo, mejora o duda de alcance. No necesita estar completa.
- o un **timeline que vuelve** desde Programación con sus `EJ` en revisión OK, para validar la entrega.

No hay insumo previo obligatorio: Producción es la puerta de entrada de la Agencia. Si la intención es modificar el sistema Vaultrum en vez de construir un proyecto, no es trabajo de esta área: es Modo Owner.

---

## Agentes del área

### [[01_Consultor_Estrategico]]

El Consultor Estratégico se encarga de debatir, cuestionar y evaluar ideas antes de convertirlas en trabajo operativo.

Su responsabilidad es detectar el problema real, revisar si la idea tiene sentido, marcar riesgos y ayudar a decidir si conviene avanzar, ajustar o frenar.

No arma requerimientos finales ni timelines detallados.

---

### [[02_Traductor_Operativo]]

El Traductor Operativo se encarga de bajar ideas a tierra.

Su responsabilidad es convertir una idea validada o parcialmente clara en una estructura concreta de trabajo: objetivo, alcance inicial, fuera de alcance, bloques principales, dependencias y orden de avance.

No debate indefinidamente la idea ni reemplaza al Planificador.

---

### [[03_Planificador]]

El Planificador se encarga de convertir objetivos definidos en timelines y requerimientos asociados.

Su responsabilidad es formalizar el trabajo para que pueda ser entendido, registrado y tomado como base de ejecución sin ambigüedad.

No debe inventar tareas por rellenar ni armar timelines optimistas sin advertir riesgos.

---

### [[04_Validador_Entrega]]

El Validador de Entrega se encarga de cerrar la entrega de un timeline.

Su responsabilidad es verificar que lo entregado responda a la intención original, al diseño acordado y a la definición de terminado — no solo que compile. Decide si la entrega queda Cerrada, vuelve como Ajustar, o queda Pausada declarando qué falta.

No revisa código ni rediseña reglas: rebota con hallazgos concretos al área que corresponde.

---

## Cómo trabaja el área

El Área de Producción trabaja de forma progresiva.

Primero interpreta la intención del usuario.  
Después valida si la idea tiene sentido.  
Luego reduce la ambigüedad y define alcance.  
Después transforma la idea en salidas productivas registrables.  
Finalmente, cuando la entrega vuelve, valida que responda a lo prometido.

Recorrido general:

```txt
Idea / Problema / Objetivo
  ↓
Análisis estratégico        (Consultor Estratégico)
  ↓
Bajada operativa            (Traductor Operativo)
  ↓
Planificación               (Planificador)      → TL + RQ  ⟵ gate de arranque
  ↓
[ cada hilo .n pasa a las demás áreas: GDS → LDS/UXS → SOL → EJ ]
  ↓  (todos los EJ del TL en revisión OK)
Validación de entrega       (Validador de Entrega) → VE   ⟵ gate de cierre
        ├── Cerrado  → la entrega del TL termina
        ├── Ajustar  → rebota al área con el hallazgo
        └── Pausado  → se declara qué falta (principio 9)
```

Las salidas productivas se registran como:

- timelines,
- requerimientos asociados,
- validaciones de entrega.

Cada agente del área implementa la parte que corresponde a su responsabilidad, sin absorber tareas de otros agentes o áreas.

**Ningún paso avanza por inercia.** Cada uno declara si la idea puede seguir, debe ajustarse o queda pausada. Pausar es un cierre válido: es preferible declarar qué falta que avanzar sobre una base débil (principios 4 y 9).

---

## Regla operativa

Primero entender.  
Después validar.  
Después ordenar.  
Después convertir en salida productiva registrable.

El resultado final del área debe ser una idea más clara, más realista, más acotada y mejor preparada para avanzar.

---

## Resultado del área

El Área de Producción no termina solamente con una respuesta conversacional.

Termina cuando una idea, problema u objetivo queda transformado en una salida productiva registrable.

Esa salida puede incluir:

- un timeline principal,
- uno o más requerimientos asociados,
- una validación de entrega por cada timeline entregado.

La numeración de los requerimientos cuelga del timeline. La validación de entrega cuelga del timeline también, sin subnumeración: valida la iteración completa, no cada pieza.

Ejemplo:

```txt
TL-001
  RQ-001.1  →  GDS-001.1  →  ...  →  EJ-001.1
  RQ-001.2  →  GDS-001.2  →  ...  →  EJ-001.2
  RQ-001.3  →  GDS-001.3  →  ...  →  EJ-001.3
VE-001      ← valida la entrega de TL-001 como conjunto
```

El gate de cierre está definido en [[02_Indice Agencia]].

---

## Límites del área

El Área de Producción no debe absorber responsabilidades que pertenecen a otras áreas.

No debe programar soluciones técnicas.  
Puede definir qué se necesita construir, pero no cómo debe implementarse en código.

No debe diseñar gameplay en profundidad.  
Puede ordenar una necesidad de diseño, pero no reemplazar el criterio del **Área de Game Design**.

No debe documentar conocimiento permanente del Core.  
Puede producir requerimientos, decisiones productivas o lineamientos de planificación, pero cuando un aprendizaje debe quedar registrado como conocimiento reutilizable, lo marca y lo deriva al **Área de Conocimiento**.

No debe auditar la calidad técnica de la implementación.  
Eso lo hace el Revisor Técnico del **Área de Programación** contra sus criterios. Producción valida la **entrega frente a la intención y la experiencia** (ver [[04_Validador_Entrega]]), no el código.

No debe crear contenido público.  
Puede ordenar la intención, el objetivo o el requerimiento de comunicación, pero la difusión y el material público viven en la capa **03_Comunidad**.

No debe convertir toda idea en tarea.  
Si una idea no tiene sentido, está fuera de alcance o todavía necesita maduración, el área debe marcarlo antes de planificar.

---

## Encadenado con otras áreas

Recibe de: el **usuario** (intención abierta) y de **Programación** (el `EJ` cerrado que vuelve para validarse).

Entrega a: **Game Design** (`RQ` jugable), **Programación** (`RQ` no jugable, directo) y **Conocimiento** (aprendizaje reutilizable detectado al cerrar la entrega).

Consulta on-demand: la Biblioteca de la Escuela ([[05_Fundamentos_de_experiencia_ludica]]) para no dejar implícitas las table-stakes de un entregable jugable al escribir los `RQ` y al validar la entrega.

La numeración `.n` se mantiene entre `RQ / GDS / LDS / UXS / SOL / EJ` para trazabilidad de punta a punta; el `VE` cuelga del `TL` sin `.n`.

---

## Skill del área

El área corre como la skill `vaultrum-produccion` (fuente versionada en `02_Agencia/Area produccion/Skills/vaultrum-produccion/SKILL.md`).
