# Motion graphics y UI

## Qué hace Vaultrum acá

Especifica y verifica la **animación de interfaz**: cómo aparecen, cambian y se van los elementos de una pantalla, y la animación de elementos gráficos —tipografía, formas, interfaz— sincronizada con sonido, que es el motion graphics.

El qué se comunica y en qué estados es de UI/UX. Acá está **cómo se mueve**, y cómo se pide y se verifica. Casi todo salió de la clase del 10 de agosto del owner (`68_Apuntes_de_catedra_Animacion_2D_3D`).

## Lo que hace buena a una interfaz animada

Clara y legible, que guíe la vista del jugador, y coherente con el juego. Cinco preguntas antes de animar una pantalla:

```txt
¿que aparece?  ¿que desaparece?  ¿que se mueve?  ¿que llama la atencion?  ¿que queda quieto?
```

## Las reglas de la clase

```txt
inmediato y animado     todo cambio es inmediato y transiciona en pocos cuadros, siempre
                        con una animacion de por medio
los textos primero      por encima de todo, y pueden entrar por corte directo
escalonado              no todo aparece junto: primer elemento a 0 s, segundo a 0.08,
                        tercero a 0.16. Es jerarquia de la informacion
escala con opacidad     escalar acompanado de opacidad se lee mejor que escalar solo
brillos y fades         para llevar la vista a un lugar del HUD
microanimaciones        +5% de escala, un cambio breve de opacidad, un desplazamiento
                        chico, un temblor de pocos cuadros: alcanza para llamar la atencion
el evento lo dispara    la informacion aparece cuando ocurre: la animacion la dispara un
                        evento (en Unreal, un dispatcher), no un sondeo
no se anima el layout   nunca tamano ni margenes: se anima la transform del render
```

**Tres tiempos de transición**, según lo que pide el momento:

```txt
utilitaria    casi inmediata         abrir el inventario por decima vez
contextual    breve y controlada     pasar de explorar a pelear
dramatica     lenta, si el contexto  un final; genera presion
              lo permite
```

**Dos cadenas que sirven de plantilla:**

```txt
recibir dano   dano -> flash -> barra de vida -> temblor -> sonido
un boton       normal -> sobre -> presionado -> respuesta
               (cada estado cambia escala, color, posicion u opacidad)
```

El ritmo: lento frustra, rápido no se entiende. Depende del contexto y de la estética, no de un número universal.

## Cómo se especifica

Una tabla de pistas, que es lo que la IA entrega y lo que después verifica:

```txt
elemento | propiedad | desde -> hasta | inicio | duracion | curva | evento que la dispara
```

La curva se escribe por lo que hace la velocidad —*llega frenando*, *overshoot leve*— y no por el nombre de un programa (`Curvas e interpolacion`).

## Con qué opera la IA

```txt
en Unreal     ver Unreal para motion graphics
en la web     la especificacion pasa a Programacion, que la implementa en CSS o JS;
              la IA verifica los valores en el codigo
```

## Qué verifica

```txt
se mide     que cada pista de la implementacion coincida con la tabla: inicio, duracion,
            curva; que ninguna anime tamano ni margenes; cuantos elementos se mueven a la
            vez en cada transicion
se juzga    si la vista va adonde tiene que ir
```

## Cómo pedírselo

```txt
"Anima el menu principal de <juego>: logo y botones, entrada contextual, escalonado
 0.08 s, boton con sus cuatro estados. Entregame la tabla de pistas."
```

Es, casi literal, la tarea de la clase.

## Lo que no hace

No decide qué estados tiene una pantalla ni qué se comunica: UI/UX. No implementa la lógica: Programación.
