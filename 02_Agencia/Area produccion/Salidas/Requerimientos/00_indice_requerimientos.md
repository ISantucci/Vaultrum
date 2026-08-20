## Propósito

Esta carpeta contiene los requerimientos generados por el Área de Producción.

Cada requerimiento debe concretar una parte del timeline asociado.

---

## Formato obligatorio

Cada requerimiento debe respetar esta estructura:

- Título
- Área afectada
- Criticidad
- Descripción
- Subtasks

---

## Regla de numeración

Los requerimientos usan el número base del timeline asociado.

Ejemplo:

TL-001  
RQ-001.1  
RQ-001.2  
RQ-001.3

---

## Patron de archivo

Cada requerimiento debe usar este patron:

RQ-XXX.Y_Nombre_Descriptivo.md

Ejemplo:

RQ-001.1_Paletas_Controlables.md

---

## Requerimientos registrados

Formato de registro:

```
- [[RQ-XXX.Y_Nombre_Descriptivo]] - descripcion breve
```

Registros:

- [[RQ-001.1_Paletas_Controlables]] - Dos paletas por teclado (W/S y flechas), acotadas y configurables
- [[RQ-001.2_Pelota_Rebote_Aceleracion]] - Pelota con rebote por impacto y aceleración progresiva
- [[RQ-001.3_Score_Victoria]] - Marcador y condición de victoria configurable
- [[RQ-001.4_Estados_Menu_Pausa_Reinicio]] - Máquina de estados: menú, pausa, fin y reinicio
- [[RQ-001.5_Game_Feel_Feedback]] - Feedback visual y sonoro en rebote, gol y saque
- [[RQ-001.6_Setup_Proyecto_Cancha]] - Setup de proyecto Unity 2022.3, escena y cancha