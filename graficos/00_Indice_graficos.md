# Gráficos del sistema

Doce diagramas: uno por cada área de la Agencia, uno por cada torre, y uno del sistema entero. Existen para poder **mirar** Vaultrum en vez de leerlo — y para que una incoherencia se vea antes de que cueste.

Se entra por `00_START_HERE`, que los nombra.

---

## Cómo se usan

De cada diagrama hay dos archivos con el mismo contenido y las mismas coordenadas:

```txt
<nombre>.drawio    editable en draw.io / diagrams.net (y en la extensión de VS Code)
<nombre>.svg       mirable en cualquier lado, sin instalar nada
```

Los dos son **copias generadas**. La fuente es `generar_graficos.py`, en esta misma carpeta: una lista de nodos y aristas por diagrama. Si el sistema cambia, se corrige la especificación y se regenera todo con la misma forma:

```bash
python3 graficos/generar_graficos.py
```

Es la misma regla que las skills: doce diagramas dibujados a mano divergen igual que doce textos que dicen lo mismo. Editar un `.drawio` a mano se pierde en la próxima corrida.

## El lenguaje visual

Es el mismo en los doce, para que se puedan leer en serie.

```txt
insumo        lo que entra al área, y lo produjo otro
rol           un agente o sub-agente: alguien con responsabilidad
artefacto     una salida registrable y numerada
gate          una decisión que puede frenar
instrumento   un script: su salida es la evidencia
externo       algo que vive fuera de esta área
flecha roja   un rebote: vuelve hacia atrás con un hallazgo
flecha punteada  una relación transversal, no un paso de la cadena
```

## Los doce

| Archivo | Qué muestra |
|---|---|
| `agencia-01-produccion` | Los cuatro agentes en cadena, el pivoteo entre áreas y el cierre por `VE`. El Despachante, de costado. |
| `agencia-02-game-design` | `RQ` + mitad A del `UXS` → `GDS`, con el marco común opcional. |
| `agencia-03-level-design` | `GDS` cerrado → `LDS`. Incluye la deuda: `LDS` no tiene contrato. |
| `agencia-04-ui-ux` | Los tres modos, y por qué el `UXS` abre antes que su insumo principal. |
| `agencia-05-programacion` | El loop de cuatro sub-agentes, los dos gates y el reparto de ejecución. |
| `agencia-06-control-de-calidad` | Gate de hilo y gate de entrega. Incluye la deuda: el de hilo nunca corrió. |
| `agencia-07-conocimiento` | Copiloto, Gate y Cosecha, y el merge al Core con aprobación del owner. |
| `agencia-08-arquitectura` | Plano, Emplazamiento y Pasada, y los instrumentos que alimentan el gate de cierre. |
| `torre-01-comunidad` | Disparadores, los tres tiempos del post, y la verificación contra el archivo. |
| `torre-02-ia-operativa` | Los dos presupuestos: entrada (AiCare) y ejecución (Despacho). |
| `torre-03-escuela` | La misión de cuatro roles, la Biblioteca y la frontera con el Core. |
| `sistema-completo` | Las cinco capas, el flujo `TL → VE` y los retornos. |

## Lo que un diagrama no puede decir

Un diagrama muestra la **forma declarada**, no lo que pasó. Tres de estos gráficos incluyen a propósito una caja con una deuda medida — el `LDS` sin contrato, el `QA` de hilo que nunca corrió — porque un mapa que solo dibuja lo que debería pasar es el mapa más caro que hay.

Para lo que sí pasó están los instrumentos, que cuentan en vez de dibujar.
