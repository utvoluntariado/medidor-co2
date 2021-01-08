# Medidor CO2

## Tabla de contenidos
1. [Empezando por el principio: ¿porqué un medidor de CO₂?](#empezando)
2. [Manos a la obra: ¿qué necesitamos?](#componentes)
3. [Hardware: Montando el sensor de CO₂](#sensor)
4. [Hardware: Montando la pantalla](#pantalla)
5. [Software: Dándole vida](#software)
6. [Cómo funciona](#funcionamiento)
7. [Posibilidades y ampliaciones](#posibilidades)
8. [Notas para técnicos y profesionales](#notas-para-tecnicos)
9. [Preguntas frecuentes acerca de funcionamiento, uso y calibración](#faq)
10. [Referencias y créditos](#creditos)

### 1. Empezando por el principio: ¿porqué un medidor de CO₂? <a name="empezando"></a>
La pandemia de COVID-19 ha movido a muchos profesionales y expertos a divulgar conocimiento, cada uno en su campo: Acerca del propio virus SARS-CoV-2 o de las herramientas de las que disponemos para combatirlo. Entre éstas últimas está la tecnología de la que disponemos en el siglo XXI.

Gracias al trabajo de científicos como [Jose-Luis Jimenez](https://twitter.com/jljcolorado), y a la labor informativa de personas como [Pablo Fuente](https://twitter.com/PabloFuente), hoy tenemos acceso a muchísima información de corte científico.

Nosotros, los trabajadores del sector tecnológico, tenemos el deber de nutrirnos de dichos conocimientos para crear una gama de herramientas útiles y sencillas de usar para, finalmente, ponerlas a disposición de toda la población.

Pero yendo un paso mas allá, quizá sea el momento de que todos hagamos un pequeño esfuerzo por mejorar nuestras competencias tecnológicas, para así alcanzar un nivel de sincronía adecuado con el año en el que vivimos y la tecnología que nos rodea. 
Solo comprendiendo las herramientas de las que disponemos, conseguiremos usarlas correctamente en nuestro beneficio.

#### 1.1 Pero ¿porqué medir la concentración de CO₂?
En un espacio interior como pueda ser una tienda, un restaurante, o la casa de un amigo, la concentración de CO₂ se eleva en función del número de personas que hay respirando.
Al exhalar CO₂ con la respiración, poco a poco la habitación se va "llenando" de este gas. Si no se ventila, dicha concentración de CO₂ se va acumulando con el paso de los minutos y las horas. 
El trabajo de científicos reputados como [Jose-Luis Jimenez](https://twitter.com/jljcolorado), nos indica que la ventilación y la renovación de aire es vital para evitar la propagación de enfermedades que se transmiten por el aire, como el COVID-19.

Por lo tanto si somos capaces de medir cuánta concentración de CO₂ tenemos en una habitación, dispondremos un indicador certero para saber si debemos ventilar la estancia en función del número de personas que hay dentro de ella, reduciendo así el riesgo de contagio de manera dramática.

Parece complicado, pero en realidad no lo es tanto. Veamos cómo hacer nuestro propio medidor de CO₂
 
### 2. Manos a la obra: ¿qué necesitamos? <a name="componentes"></a>
Sin pensar mucho podemos llegar a la conclusión de que vamos a necesitar: un sensor de CO₂ y algo que nos permita ver la medición. Has acertado el casi la totalidad de los componentes.
Vamos a usar:
- Un sensor de CO₂: Va a ser la pieza encargada de realizar la medición. Concretamente el MH-Z19B.
- Una pantalla muy pequeña: No necesitamos mucho para mostrar un valor, así que usaremos una pantalla de apenas una pulgada.
- Raspberry Pi Zero: Necesitamos un "cerebro" que coordine todo esto. Raspberry es una plaquita que contiene un mini-ordenador. Es de muy bajo coste, fácil de usar y es perfecta para este proyecto.
- Una fuente de alimentación portatil: dado que nuestro "cerebro" se alimenta por USB, podemos usar una batería portátil cualquiera, o una que se pueda integrar con toda la lista anterior.

Ésta es la lista de la compra:
- Raspberry Pi Zero: Esta plaquita nos va a dar el soporte necesario para poder fabricar nuestro medidor de CO₂. Se trata básicamente de un microordenador y está orientada a aficionados de la computación educativa y emprendedores informáticos que desean tener equipos económicos para crear desarrollos y proyectos ambiciosos dentro del campo de la robótica y la automatización.
Para comprarla, tenemos que tener en cuenta lo siguiente:
  * El nombre completo del modelo que necesitamos es Raspberry Pi Zero WH.
  * Tiene que venir con un montón de patillas ya soldadas, como se ve en la foto.
  * No necesitamos un kit con carcasa y todo lo demás. Sólo la placa con las patillas soldadas.
  
Existen muchísimas tiendas donde comprar este pequeño ordenador. Os dejo una lista con algunas de las tiendas en las que suelo comprar:
  * [Tienda KUBII](https://www.kubii.es/raspberry-pi-3-2-b/2076-raspberry-pi-zero-wh-kubii-3272496009394.html)
  * [Tienda Ultra-Lab](http://ultra-lab.net/producto/raspberry-pi-zero-wh/)
  * [Tienda Tienda-Tec](https://www.tiendatec.es/raspberry-pi/gama-raspberry-pi/768-raspberry-pi-zero-wh-0327249600939.html)

Si andáis justos de presupuesto, buscad el mas barato. La placa es la misma independientemente del precio.

Coste medio: 15€

![Raspberry-Pi-Zero_WH](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/RaspberryPiZeroWH-small.png?raw=true)

---

- Tarjeta Micro SD: Una tarjeta SD mínimo de 8Gb en la que instalaremos el software que manejará todo el sistema.

Coste medio: 5€

---

- Sensor de CO₂ MH-Z19B: Hay varios modelos de sensor y tenemos que tener en cuenta varias cosas antes de comprarlo
  * Que venga con las patillas soldadas
  * Que venga con las patillas al aire, sin ningún tipo de conector ni cable
  
Particularmente lo he comprado [en esta tienda de electrónica](https://electronperdido.com/shop/sensores/calidad-aire/mh-z19-sensor-co2-ndir-5000ppm/) pero podéis buscarlo o pedirlo en tiendas de confianza. No tengo ninguna filiación con la tienda enlazada, por supuesto.

Ésta es la pieza mas cara de nuestro medidor de CO₂. No conviene escatimar en este componente.

Coste medio: 35€

![Sensor-co2-correcto](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/SensorCO2-correcto.png?raw=true)

---

- Mini pantalla: Aquí las opciones son muchas y muy variadas. Particularmente 

---

- (OPCIONAL) Batería

---

- Cableado

---

Coste total sin batería: 60€

### 3. Hardware: Montando el sensor de CO₂ <a name="sensor"></a>

### 4. Hardware: Montando la pantalla <a name="pantalla"></a>

### 5. Software: Dándole vida <a name="software"></a>

### 6. Cómo funciona <a name="funcionamiento"></a>

### 7. Posibilidades y ampliaciones <a name="posibilidades"></a>

### 8. Notas para técnicos y profesionales <a name="notas-para-tecnicos"></a>

### 9. Preguntas frecuentes acerca de funcionamiento, uso y calibración <a name="faq"></a>

### 10. Referencias y créditos <a name="creditos"></a>
