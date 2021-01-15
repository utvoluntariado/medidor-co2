# Medidor de CO₂ económico y fácil de hacer
En este repositorio se exponen unas instrucciones sencillas para que cualquier persona pueda construir, por un precio muy reducido, un medidor de CO₂. Éste medidor podrá ser usado como medidor portátil o fijo, y además proveerá una red WiFi desde la que poder consultar la medición del sensor en tiempo real.

De gran utilidad en locales abiertos al público, tales como tiendas, bares o restaurantes. Para que de un modo económico puedan ofrecer a sus clientes una forma de comprobar la correcta ventilación del espacio.

Consulta el tutorial para construir tu medidor de CO₂ en la [wiki de este repositorio](https://github.com/utvoluntariado/medidor-co2/wiki).

## 1. Preguntas frecuentes acerca de funcionamiento, uso y calibración
* Antes de realizar cualquier operación sobre el medidor, quítale la corriente.
* El sensor viene calibrado con un valor de referencia de 400ppm.
* Durante el encendido, es normal observar lecturas de 500ppm en descenso hasta 400ppm antes de comenzar a registrar lecturas reales. Dale unos segundos al sensor para que tome buenas lecturas.
* La red WiFi que el medidor crea para poder consultar la lectura desde un terminal móvil aparecerá como _red insegura_. El motivo es que carece de contraseña de acceso, para facilitar el uso. Recuerda no permanecer mucho tiempo conectado a ella, y desconectarte para continuar usando tu terminal móvil con normalidad.
* El sistema tiene integrados los siguientes códigos de alerta (color de la medición y lectura en los terminales móviles):
  - **VERDE**: Valores por debajo de 700ppm. Calidad del aire dentro de los rangos de seguridad.
  - **AMARILLO**: Valores entre 700ppm y 1400ppm. Se está comenzando a superar el rango de seguridad. Se recomienda ventilación.
  - **ROJO**: Valores superiores a 1400ppm. Se requiere ventilación inmediata.
* Es muy recomendable buscar un sitio adecuado para colocar el medidor.
* Si ha dejado de funcionar, trata de volver a "quemar" la imagen en la tarjeta SD.

## 2. Referencias y créditos
El software de terceros que se ha usado para crear este medidor es el siguiente:
* [Raspberry Pi OS Lite](https://www.raspberrypi.org/software/operating-systems/)
* [mh-z19 0.6.3](https://github.com/UedaTakeyuki/mh-z19) (@UedaTakeyuki)
* [asciimatics](https://github.com/peterbrittain/asciimatics) (@peterbrittain)
* [nodogsplash](https://github.com/nodogsplash/nodogsplash) (@nodogsplash)
* [hostapd](https://en.wikipedia.org/wiki/Hostapd)
* [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq)

La idea original, la imagen del sistema preparada, el script que consulta la medición del sensor, así como la web que se muestra en el portal cautivo han sido creados por Jorge J. Ramos (@jorgej-ramos) y puestos a disposición de la Unidad Tecnológica de Voluntariado en este repositorio.
