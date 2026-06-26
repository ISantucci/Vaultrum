# MOCs y Navegación Guiada

## Propósito

Los MOCs (Maps of Content) son puntos de entrada a secciones de Vaultrum.

La navegación debe ser un árbol guiado, no una telaraña.

---

## MOCs

El Arquitecto de conocimiento debe cuidar que los MOCs funcionen como puntos de entrada.

Un MOC debe:

- orientar,
- agrupar,
- explicar brevemente,
- linkear documentos centrales,
- evitar telarañas,
- mostrar el recorrido recomendado.

Un MOC NO debe:

- repetir todo el contenido,
- linkear cada palabra,
- crear rutas confusas,
- prometer documentos que no existen,
- volverse más importante que las notas reales.

---

## Árbol Guiado

Vaultrum debe priorizar una navegación de árbol guiado con puentes justificados.

```txt
Start Here
→ índice de sección
→ documentos centrales
→ documentos específicos
→ links puntuales por dependencia real
```

No se busca una telaraña de links.

Se busca una estructura que una IA y una persona puedan recorrer sin perderse.

---

## Criterio de Links

Un link debe ayudar a navegar.

No debe marcar simplemente que una palabra es importante.

Si un concepto se menciona pero no es una ruta necesaria, puede quedar como texto plano.

### Links que Orientan (SON BUENOS)

- De un índice a documentos principales
- De un proveedor a sus consumidores
- De un documento a documentos relacionados por necesidad real
- De un algoritmo a aplicaciones

### Links que Decoran (NO USAR)

- Cada aparición de una palabra importante
- Conceptos genéricos (Unity, clase, manager, patrón)
- Enlaces múltiples al mismo documento
- Links que no mejoran navegación

---

## Links Innecesarios

Cuando una nota tiene demasiados wikilinks, el Arquitecto debe revisar si esos links orientan o decoran.

**Criterio**:

```txt
Un link debe ayudar a navegar.
No debe marcar simplemente que una palabra es importante.
```

Si un concepto se menciona pero no es una ruta necesaria, puede quedar como texto plano.

---

## Links Faltantes

Cuando una nota importante queda aislada, el Arquitecto debe revisar si necesita un link desde un MOC, índice o documento central.

No debe agregar links por cantidad.

Debe agregar links dónde mejoren navegación real.

---

## Estructura de Árbol

```txt
00_START_HERE
│
├─ 01_SOLID
│   └─ Índice SOLID
│       └─ Principios específicos
│
├─ 02_Patrones de diseño
│   └─ Índice Patrones
│       └─ Patrones específicos
│
└─ 11_Agentes
    └─ Índice Agentes
        └─ Agentes específicos
            └─ Documentación del Agente
```

Cada nivel tiene UN punto de entrada claro.

Cada punto de entrada muestra las opciones siguientes.

---

## Regla Final

```txt
Un MOC bien diseñado ahorra clicks.
No hace falta saberlo todo para encontrarlo.
```
