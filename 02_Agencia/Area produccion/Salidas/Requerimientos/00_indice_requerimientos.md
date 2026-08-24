## Propósito

Esta carpeta contiene los requerimientos generados por el Área de Producción.

Cada requerimiento debe concretar una parte del timeline asociado.

---

## Formato obligatorio

Cada requerimiento respeta esta estructura:

```txt
Título
Área afectada
Criticidad
Descripción
Subtasks
```

---

## Regla de numeración y nombre de archivo

Un requerimiento hereda el número base del timeline que concreta, y lo subnumera:

```txt
TL-001
  RQ-001.1
  RQ-001.2
  RQ-001.3
```

El archivo se nombra con el código, el separador y el nombre descriptivo:

```txt
RQ-XXX.Y_Nombre_Descriptivo.md
RQ-001.1_Paletas_Controlables.md
```

---

## Requerimientos registrados

### TL-001 — Pong 2 jugadores

- [[RQ-001.6_Setup_Proyecto_Cancha|RQ-001.6 Setup de proyecto y cancha]] — proyecto Unity 2022.3, escena y cancha
- [[RQ-001.1_Paletas_Controlables|RQ-001.1 Paletas controlables]] — dos paletas por teclado (W/S y flechas), acotadas y configurables
- [[RQ-001.2_Pelota_Rebote_Aceleracion|RQ-001.2 Pelota: rebote y aceleración]] — rebote por impacto y aceleración progresiva
- [[RQ-001.3_Score_Victoria|RQ-001.3 Score y victoria]] — marcador y condición de victoria configurable
- [[RQ-001.4_Estados_Menu_Pausa_Reinicio|RQ-001.4 Estados]] — máquina de estados: menú, pausa, fin y reinicio
- [[RQ-001.5_Game_Feel_Feedback|RQ-001.5 Game feel]] — feedback visual y sonoro en rebote, gol y saque

### TL-002 — Pong 3D en Unity 6

- [[RQ-002.1_Setup_Proyecto_Arena3D|RQ-002.1 Setup de proyecto y arena]] — Unity 6000.0.81f1, arena 3D y escena generada por script
- [[RQ-002.2_Paletas_Controlables|RQ-002.2 Paletas controlables]] — dos paletas por teclado, acotadas, entrada tras interfaz
- [[RQ-002.3_Pelota_Rebote_Aceleracion|RQ-002.3 Pelota: rebote y aceleración]] — ángulo por punto de impacto y aceleración acotada
- [[RQ-002.4_Score_Victoria_Reinicio|RQ-002.4 Score, victoria y reinicio]] — marcador, victoria configurable y reinicio sin recargar escena
- [[RQ-002.5_Estados_Menus|RQ-002.5 Estados y menús]] — máquina de estados, menús y menú de opciones
- [[RQ-002.6_Game_Feel_Audio|RQ-002.6 Game feel y audio]] — sacudida, punch, estela, hitstop y audio procedural

### TL-003 — Pong 3D, cadena completa

- [[RQ-003.1_Setup_Proyecto_Arena|RQ-003.1 Setup de proyecto y arena]] — Unity 6, escena mínima y arena 3D legible
- [[RQ-003.2_Paletas_Controlables|RQ-003.2 Paletas controlables]] — rampa de aceleración y peso
- [[RQ-003.3_Pelota_Rebote_Aceleracion|RQ-003.3 Pelota: rebote y aceleración]] — ángulo por punto de impacto, spin de paleta y anti-tunneling
- [[RQ-003.4_Score_Saque_Victoria|RQ-003.4 Score, saque y victoria]] — saque hacia quien recibió el gol, victoria y revancha
- [[RQ-003.5_Estados_Y_Flujo_De_Pantallas|RQ-003.5 Estados y flujo de pantallas]] — máquina de estados sin estados muertos
- [[RQ-003.6_Game_Feel_Y_Audio|RQ-003.6 Game feel y audio]] — juice jerarquizado de impacto, gol y rally; audio procedural
- [[RQ-003.7_Onboarding_Y_Legibilidad|RQ-003.7 Onboarding y legibilidad]] — controles comunicados, lados distinguibles, HUD jerarquizado

---

