from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "python-coding",
        "image": "sofia_coding.png",
        "author": "Sofía Caro",
        "date": date(2025, 9, 1),
        "title": "Programando con Python",
        "excerpt": "Explorando las maravillas del desarrollo web con Python y Django. Muy recomendado para quienes desean aprender más sobre este poderoso lenguaje.",
        "content": """
          Cuando me siento frente al teclado a programar en Python, ronroneo de gusto porque todo parece sencillo. Con pocas teclas logro que la pantalla me obedezca, y eso me hace sentir poderosa, como cuando atrapo un insecto que vuela cerca. Python me da esa sensación de ligereza: no necesito maullar demasiado para que las cosas funcionen, y eso me encanta.
          
          Aun así, confieso que me molesta que los bloques no tengan llaves {}. ¿Cómo esperan que yo, una gatita curiosa, me sienta segura si todo depende de unos espacios invisibles? A veces, un tabulador mal puesto me hace bufar y golpear las patas contra el teclado. Es como cuando alguien me cambia el lugar de mi cama: de repente nada encaja y me siento perdida.
          
          Pero al final, siempre termino disfrutando la experiencia. Python me deja resolver problemas rápido y después tengo más tiempo para acicalarme o dormir al sol. Aunque extraño ver las llaves como en otros lenguajes, he aprendido a convivir con la indentación, como quien acepta que la caja de cartón está chueca pero igual es perfecta para dormir. Al final, programar en Python me hace sentir ágil, libre y lista para seguir explorando.
        """
    },
    {
        "slug": "javascript-coding",
        "image": "maximiliano_coding.png",
        "author": "Maximiliano Caro",
        "date": date(2025, 8, 25),
        "title": "¡Javascript es genial!",
        "excerpt": "¡Javascript es un lenguaje de programación increíble! En este artículo, exploraremos sus características más destacadas y por qué deberías aprenderlo.",
        "content": """
          Cuando programo en JavaScript siento que todo fluye como cuando me estiro sobre el teclado. Amo la libertad que me da este lenguaje, la forma en que puedo construir cosas increíbles en poco tiempo y ver resultados casi de inmediato en la pantalla. Cada proyecto me emociona, como si fuera una nueva caja en la que puedo meterme a jugar y explorar.
          
          Sin embargo, no todo es un ronroneo tranquilo. Lo que más me hace sufrir es el momento de depurar: los errores aparecen como fantasmas que se esconden en rincones oscuros, y me paso horas persiguiéndolos sin atraparlos. Además, las diferencias entre navegadores me sacan maullidos de frustración. Lo que funciona en uno parece desmoronarse en otro, como si cada navegador tuviera su propia personalidad caprichosa.
          
          Aun así, no cambiaría a JavaScript por nada. Es mi lenguaje favorito y me hace sentir creativo, como si cada línea de código fuera un salto elegante sobre un mueble nuevo. Aunque me quejo del debug y de los navegadores, siempre regreso con entusiasmo a mis proyectos, porque sé que al final me darán la satisfacción de ver algo vivo y brillante en la pantalla. Para mí, JavaScript es como un juguete infinito que nunca se agota.
        """
    },
    {
        "slug": "kotlin-coding",
        "image": "demian_coding.png",
        "author": "Demian Caro",
        "date": date(2025, 7, 9),
        "title": "Kotlin: Un Lenguaje Moderno",
        "excerpt": "Kotlin es un lenguaje de programación moderno y conciso que se ejecuta en la JVM. En este artículo, exploraremos sus características más destacadas.",
        "content": """
          Cuando programo en Kotlin siento que todo es suave, limpio y moderno, como cuando encuentro un rincón soleado y me acomodo sin esfuerzo. Me encanta lo expresivo que es el lenguaje y lo poco que necesito escribir para lograr grandes cosas. Con Jetpack Compose me siento aún más libre, porque crear interfaces se vuelve como jugar con cajas de cartón: solo acomodo las piezas y de pronto tengo algo divertido y funcional.
          
          Pero en mis maullidos más sinceros, tengo que confesar que a veces extraño a Java. Siento que Java es más orgánico, más cercano a mis instintos felinos, como rascar un mueble de madera sólida. Kotlin me fascina, pero hay momentos en que tanta abstracción me hace arquear la espalda con dudas. Es como si me dieran una comida gourmet deliciosa, pero yo aún recordara con cariño la croqueta sencilla que me ha alimentado siempre.
          
          Aun así, Kotlin es mi lugar favorito para ronronear. Me da velocidad, seguridad y una manera elegante de expresar mis ideas sin tantos rodeos. Y aunque miro a Java con nostalgia, sé que Kotlin me ofrece la calidez de un regazo moderno, donde puedo estirarme a gusto y programar con confianza. Para mí, escribir en Kotlin es como cazar con precisión: rápido, elegante y profundamente satisfactorio.
        """,
    },
    {
        "slug": "c-coding",
        "image": "wero_coding.png",
        "author": "Wero Caro",
        "date": date(2025, 6, 10),
        "title": "C: Un Lenguaje Clásico",
        "excerpt": "C es un lenguaje de programación de propósito general que ha influido en muchos otros lenguajes. En este artículo, exploraremos sus características más destacadas.",
        "content": """
            Cuando pienso en programación, siempre vuelvo a mis días con el lenguaje C. Aprendí con Borland y para mí fue como entrenar desde cachorro con disciplina: entender la memoria, los punteros y la lógica pura. Ese lenguaje me enseñó a respetar la base de todo, a no dar nada por sentado y a saber exactamente qué hace cada instrucción. Cada vez que escribo en C siento que estoy construyendo con ladrillos sólidos, sin adornos innecesarios.
            
            Claro, reconozco que a veces vivir solo en C es como correr siempre con una correa muy ajustada. Los nuevos lenguajes modernos ofrecen herramientas que aceleran el desarrollo, librerías listas para usar y sintaxis más amigables. Mientras yo sigo contando ciclos y optimizando cada byte, veo cómo otros llegan a soluciones más rápido, y no puedo negar que eso tiene su encanto. Es como ver a cachorros jóvenes que aprenden trucos con facilidad gracias a juguetes nuevos.
            
            Aun así, me gusta pensar que mi experiencia en C me coloca en otro nivel. Es un lenguaje que me formó, que me enseñó a pensar en lo fundamental y a enfrentar problemas de raíz. Y aunque ahora reconozco que lenguajes como Python, JavaScript o Kotlin ayudan a ir más rápido, yo sigo ladrando orgulloso de mis orígenes en C. Al final, sé que todo lo que ellos hacen se apoya en los cimientos que yo aprendí a dominar.
        """
    }
]

def get_date(post):
  return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })