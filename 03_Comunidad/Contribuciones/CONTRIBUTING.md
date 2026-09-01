# Cómo contribuir a Vaultrum

Vaultrum acepta contribuciones que mejoren su conocimiento, su claridad y su utilidad.

El objetivo de contribuir es aportar contenido, correcciones o propuestas que ayuden a que Vaultrum sea una herramienta más sólida para trabajar con videojuegos, software, inteligencia artificial, arquitectura, producción, documentación y desarrollo.

---

## Qué tipo de aportes se buscan

Actualmente se buscan tres tipos principales de contribución:

1. Aportes de contenido nuevo.
    
2. Correcciones o mejoras sobre contenido existente.
    
3. Propuestas justificadas para mejorar la estructura del sistema.
    

---

## 1. Aportes de contenido nuevo

Se pueden proponer nuevos contenidos que todavía no existan dentro de Vaultrum y que sean útiles para el sistema.

Ejemplos de contenido válido:

- patrones de diseño;
    
- principios de arquitectura;
    
- estructuras de datos;
    
- algoritmos;
    
- conceptos de optimización;
    
- conceptos de inteligencia artificial;
    
- criterios de producción;
    
- flujos de documentación;
    
- ejemplos aplicados a videojuegos;
    
- buenas prácticas de programación;
    
- sistemas reutilizables;
    
- metodologías de trabajo con IA;
    
- análisis de herramientas o procesos útiles.
    

El contenido nuevo debe tener valor operativo.

No alcanza con que sea información interesante.

Tiene que poder ayudar a pensar, decidir, construir o mejorar un proyecto.

---

## Criterios para aportar contenido nuevo

Antes de proponer contenido nuevo, revisar:

- si el tema ya existe en Vaultrum;
    
- si el aporte mejora o amplía algo real;
    
- si está explicado con claridad;
    
- si puede ser útil para humanos e inteligencias artificiales;
    
- si tiene relación con videojuegos, software, producción, documentación, IA, arquitectura u optimización;
    
- si aporta criterio y no solo información suelta.
    

Un buen aporte de contenido debería responder:

- qué es;
    
- para qué sirve;
    
- qué problema resuelve;
    
- cuándo conviene usarlo;
    
- cuándo no conviene usarlo;
    
- cómo puede aplicarse en videojuegos o software;
    
- qué errores ayuda a evitar.
    

---

## 2. Correcciones o mejoras sobre contenido existente

También se aceptan mejoras sobre documentos que ya existen dentro de Vaultrum.

Ejemplos:

- corregir errores de escritura;
    
- mejorar redacción;
    
- aclarar una definición;
    
- corregir una contradicción;
    
- arreglar links;
    
- mejorar formato Markdown;
    
- ordenar una sección confusa;
    
- agregar un ejemplo útil;
    
- eliminar contenido repetido;
    
- detectar contenido mal ubicado;
    
- mejorar una explicación técnica;
    
- ajustar una nota para que sea más clara para humanos e IA.
    

Estas contribuciones son importantes porque ayudan a que Vaultrum sea más preciso, más mantenible y más fácil de usar.

---

## 3. Propuestas justificadas

También se pueden abrir propuestas para mejorar partes del sistema.

Una propuesta puede ser:

- crear una nueva nota;
    
- mover contenido a otra carpeta;
    
- mejorar una sección existente;
    
- proponer una nueva relación entre notas;
    
- sugerir un nuevo agente;
    
- proponer una mejora en un flujo de trabajo;
    
- detectar un vacío importante en el conocimiento actual;
    
- proponer una mejora sobre VaultrumCore, la Agencia o la Comunidad.
    

Una propuesta no tiene que venir con todo resuelto, pero sí debe estar bien justificada.

---

## Cómo hacer una buena propuesta

Una propuesta debería explicar:

### Problema

Qué falta, qué está mal, qué confunde o qué podría mejorar.

### Ubicación

Dónde impactaría el cambio.

Ejemplos:

- `01_VaultrumCore/02_Contenido VaultrumCore`
    
- `01_VaultrumCore/03_VaultrumAi`
    
- `02_Agencia`
    
- `02_Agencia/Agentes`
    
- `03_Comunidad`
    

### Propuesta

Qué se sugiere crear, corregir o modificar.

### Justificación

Por qué ese cambio sería útil para Vaultrum.

### Riesgo

Qué podría romper, duplicar o confundir.

---

## Formato recomendado para nuevos contenidos

Cuando se aporte una nota nueva, se recomienda usar una estructura simple:

```md
# Nombre del concepto

## Definición

Qué es el concepto.

## Qué problema resuelve

Qué necesidad o problema ayuda a resolver.

## Cómo funciona

Explicación clara del funcionamiento.

## Cómo aplicarlo en videojuegos o software

Ejemplos prácticos de uso.

## Cuándo conviene usarlo

Situaciones donde tiene sentido aplicarlo.

## Cuándo no conviene usarlo

Situaciones donde puede ser innecesario o contraproducente.

## Errores que ayuda a evitar

Problemas comunes que este concepto puede prevenir.
```

---

## Criterio de navegación

Vaultrum usa navegación en cascada.

Antes de agregar links, revisar si realmente ayudan a navegar.

Un índice padre no debería linkear todo lo que existe debajo.

Debe linkear principalmente a sus hijos directos.

Ejemplo:

```txt
VaultrumCore
→ Identidad y principios
→ Contenido VaultrumCore
→ VaultrumAi
```

No debería convertirse en una lista de todas las notas internas.

La navegación debe ayudar a entender el sistema, no crear una telaraña.

---

## Criterio de ubicación

Cada contenido debe entrar por responsabilidad.

Antes de proponer una nota, carpeta o cambio estructural, revisar:

- qué problema resuelve;
    
- qué responsabilidad cubre;
    
- dónde debería vivir;
    
- si ya existe contenido relacionado;
    
- si puede integrarse en una nota existente;
    
- si realmente necesita una nota nueva.
    

No se debe crear contenido solo por completismo.

---

## Criterio de revisión

Una contribución puede aceptarse si:

- mejora la claridad;
    
- mejora la utilidad;
    
- corrige un error real;
    
- aporta conocimiento aplicable;
    
- respeta la estructura del vault;
    
- mantiene separación de responsabilidades;
    
- evita duplicar contenido;
    
- ayuda a humanos e inteligencias artificiales.
    

Una contribución puede rechazarse o requerir revisión si:

- agrega contenido genérico;
    
- mezcla responsabilidades;
    
- duplica material existente;
    
- no aporta valor operativo;
    
- rompe la navegación;
    
- modifica partes centrales sin justificación;
    
- crea estructura innecesaria;
    
- contradice los principios del proyecto.
    

---

## Dirección del proyecto

Vaultrum es un proyecto abierto con dirección curada.

Las contribuciones externas son bienvenidas, pero deben respetar la identidad, la estructura y el criterio del proyecto.

La aceptación de contribuciones no implica autoridad automática sobre el rumbo de Vaultrum.

Las decisiones finales de integración, estructura y dirección corresponden a la gobernanza del proyecto.

---

## La licencia de lo que aportás

Vaultrum es GPL-3.0 y se queda así. La política de contribución estaba sin escribir hasta el 2026-09-01 — hallazgo de `ARQ-024` — y se escribe **antes** del primer aporte externo a propósito: una política escrita después del primer PR ya no es una política, es una negociación.

> **DCO (Developer Certificate of Origin). No hay cesión de copyright: cada quien conserva el suyo.**

Para aportar, firmá cada commit:

```bash
git commit -s
```

Eso agrega `Signed-off-by: Tu Nombre <tu@email>`, con lo que certificás lo que dice el [DCO 1.1](https://developercertificate.org/): que tenés derecho a aportar ese trabajo y que aceptás que se distribuya bajo la licencia del proyecto.

### Qué implica, dicho claro

Es la mitad que las políticas de contribución suelen callar, así que va explícita:

```txt
Con DCO      cada quien conserva el copyright de lo que escribio. Vaultrum queda
             GPL-3.0 y NO se puede relicenciar despues sin el consentimiento de
             todos los que aportaron.

Con CLA      quien aporta le cede al dueño una licencia amplia, y el dueño puede
             relicenciar el proyecto entero mas adelante -- incluso cerrarlo.
```

**Se eligió DCO a propósito.** La decisión de mantener Vaultrum abierto ya está tomada, y un CLA en un proyecto GPL de un solo autor comunica lo contrario: *me reservo el derecho de cerrar esto*. Pedir una cesión para una opción que no se va a usar es cobrar un costo por nada.

La contrapartida se acepta con los ojos abiertos: **desde el primer aporte externo, relicenciar deja de depender de una sola persona.** No es un efecto secundario — es la garantía que el proyecto le da a quien aporta.

La marca es otra cosa que la licencia: la GPL licencia el código, no el nombre. Ver `03_Comunidad/Gestion/License_Notice.md`.

---

## El gate de cierre va a medir tu cambio

Vaultrum tiene un gate que corre en cada commit y mide cuatro cosas. Un aporte tiene que pasarlo, o declarar por qué no.

```bash
skills.bat            # o skills.sh: sincroniza, instala el gate y verifica el entorno
git commit -s         # el hook corre solo
```

Las cuatro mediciones son `grafo.py` (las seis leyes del grafo), `grafo.py --paquete` (las mismas, sobre lo que se clona), `gemelos.py` (las copias que deben ser idénticas) y `documentacion.py` (la forma del texto). Si alguna frena, el mensaje dice cuál y cómo correr su informe completo.

**Un desvío deliberado se declara, no se esconde.** El camino es el `excepciones.txt` del área que mide, con la razón escrita. `git commit --no-verify` existe y no deja rastro en ningún lado: si lo usás, decilo en el mensaje del commit.

Tres cosas que el gate mide y conviene saber antes de escribir:

- **Las skills no se editan donde se ven.** `.claude/skills/` y `.agents/skills/` son copias generadas; la fuente vive en el área. Editar la copia se pierde en la próxima corrida del instalador.
- **Un área declara, no guarda.** Si tu cambio agrega un archivo, el índice de esa carpeta tiene que nombrarlo.
- **Un número sin instrumento es una estimación.** Si afirmás una medición, decí con qué se midió.

---

## Antes de contribuir

Antes de abrir una contribución, revisar:

- `README.md`;
    
- `00_START_HERE.md`;
    
- `03_Comunidad/Gestion/GOVERNANCE.md`;
    
- `03_Comunidad/Contribuciones/Sistema de contribucion.md`;
    
- la sección del vault donde se quiere aportar.
    

Esto ayuda a evitar duplicaciones, cambios fuera de lugar o propuestas que no respetan el criterio de Vaultrum.

---

## Regla final

Contribuir no es agregar más contenido.

Contribuir es mejorar Vaultrum.

Un aporte vale si mejora el conocimiento, la claridad, la estructura o la utilidad del sistema.