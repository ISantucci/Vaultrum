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
- [[RQ-002.1_Setup_Proyecto_Arena3D]] - Setup Unity 6000.0.81f1, arena 3D y escena generada por script
- [[RQ-002.2_Paletas_Controlables]] - Dos paletas por teclado, acotadas, entrada tras interfaz
- [[RQ-002.3_Pelota_Rebote_Aceleracion]] - Pelota con angulo por punto de impacto y aceleracion acotada
- [[RQ-002.4_Score_Victoria_Reinicio]] - Marcador, victoria configurable y reinicio sin recargar escena
- [[RQ-002.5_Estados_Menus]] - Maquina de estados, menus y menu de opciones
- [[RQ-002.6_Game_Feel_Audio]] - Sacudida, punch, estela, hitstop y audio procedural
- [[RQ-003.1_Setup_Proyecto_Arena]] - Setup Unity 6, escena minima y arena 3D legible
- [[RQ-003.2_Paletas_Controlables]] - Dos paletas por teclado con rampa de aceleracion y peso
- [[RQ-003.3_Pelota_Rebote_Aceleracion]] - Angulo por punto de impacto, spin de paleta, anti-tunneling
- [[RQ-003.4_Score_Saque_Victoria]] - Marcador, saque hacia quien recibio el gol, victoria y revancha
- [[RQ-003.5_Estados_Y_Flujo_De_Pantallas]] - Maquina de estados y flujo sin estados muertos
- [[RQ-003.6_Game_Feel_Y_Audio]] - Juice jerarquizado de impacto, gol y rally, audio procedural
- [[RQ-003.7_Onboarding_Y_Legibilidad]] - Controles comunicados, lados distinguibles, HUD jerarquizado
