"""Generate the three localized KidLogic Loft landing pages.

The app and privacy pages retain their longer, route-specific copy. The landing
page structure lives here so EN, DE and ES cannot drift as the family shell
evolves.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGS = ("en", "de", "es")
LOCALES = {"en": "en_US", "de": "de_DE", "es": "es_ES"}

T = {
    "en": {
        "title": "KidLogic Loft — Calm Kids Apps, No Ads, No Noise",
        "description": "KidLogic Loft makes calm, ad-free mobile apps for children aged 3–8. Thoughtful puzzle games designed with care for children and parents.",
        "nav": ("Apps", "Principles", "About"), "theme": ("Use dark theme", "Use light theme"),
        "eyebrow": "Playful for children. Reassuring for parents.",
        "hero": "Calm apps for curious children.",
        "intro": "Thoughtful mobile play for ages 3–8, designed to work offline without ads, tracking, subscriptions or in-app purchases.",
        "cta": ("Explore the apps", "How we design"),
        "facts": (("Ages", "3–8"), ("Price", "Free"), ("Play", "Offline"), ("Advertising", "None")),
        "apps_head": ("Our apps", "Small worlds, made with care.", "Clear mechanics for children; clear terms for parents."),
        "live": "On Google Play", "learn": "View app details",
        "octo": "Simple, colourful jigsaw puzzles with large pieces and a friendly octopus. Made for phones and tablets.",
        "coming": "In development", "beaver": "A gentle railway adventure about helping neighbours on the way to a picnic.",
        "diorama": "A quiet interactive diorama where characters come to life with a tap, then settle again.",
        "principles_head": ("Our principles", "Designed for a parent’s peace of mind.", "Play stays inside the product. The promises around it stay plain and specific."),
        "principles": (("Private by default", "No accounts, analytics, behavioural profiles or personal data collection."), ("No commercial pressure", "No ads, in-app purchases, subscriptions, timers or manufactured urgency."), ("Works without a connection", "Core play is available offline, without sign-in or a network connection.")),
        "about_head": ("About", "Independent apps, built in Austria."),
        "about": "KidLogic Loft is the children’s app label of Appmonto Studio. We make focused Android experiences that children can understand on their own and parents can evaluate before handing over a device.",
        "footer": ("Privacy", "Support", "Contact", "Imprint", "An Appmonto Studio brand"),
    },
    "de": {
        "title": "KidLogic Loft — Ruhige Kinder-Apps ohne Werbung und Lärm",
        "description": "KidLogic Loft entwickelt ruhige, werbefreie Apps für Kinder von 3 bis 8 Jahren. Sorgfältig gestaltete Puzzlespiele für Kinder und Eltern.",
        "nav": ("Apps", "Prinzipien", "Über uns"), "theme": ("Dunkles Design verwenden", "Helles Design verwenden"),
        "eyebrow": "Verspielt für Kinder. Beruhigend für Eltern.",
        "hero": "Ruhige Apps für neugierige Kinder.",
        "intro": "Durchdachter mobiler Spielspaß für Kinder von 3 bis 8 Jahren – offline, ohne Werbung, Tracking, Abos oder In-App-Käufe.",
        "cta": ("Apps entdecken", "Unsere Prinzipien"),
        "facts": (("Alter", "3–8"), ("Preis", "Kostenlos"), ("Spielen", "Offline"), ("Werbung", "Keine")),
        "apps_head": ("Unsere Apps", "Kleine Welten, mit Sorgfalt gemacht.", "Klare Spielmechaniken für Kinder und klare Bedingungen für Eltern."),
        "live": "Bei Google Play", "learn": "App ansehen",
        "octo": "Einfache, bunte Puzzles mit großen Teilen und einem freundlichen Oktopus. Für Smartphones und Tablets.",
        "coming": "In Entwicklung", "beaver": "Ein ruhiges Eisenbahnabenteuer über kleine Hilfen auf dem Weg zu einem Picknick.",
        "diorama": "Ein stilles interaktives Diorama: Figuren werden durch Antippen lebendig und kommen danach wieder zur Ruhe.",
        "principles_head": ("Unsere Prinzipien", "Damit Eltern ein gutes Gefühl haben.", "Das Spielerische bleibt im Produkt. Unsere Versprechen bleiben klar und konkret."),
        "principles": (("Privat von Anfang an", "Keine Konten, Analysen, Verhaltensprofile oder Erfassung persönlicher Daten."), ("Kein kommerzieller Druck", "Keine Werbung, In-App-Käufe, Abos, Timer oder künstliche Dringlichkeit."), ("Funktioniert ohne Verbindung", "Das eigentliche Spiel funktioniert offline, ohne Anmeldung und ohne Internet.")),
        "about_head": ("Über uns", "Unabhängige Apps, entwickelt in Österreich."),
        "about": "KidLogic Loft ist die Marke für Kinder-Apps von Appmonto Studio. Wir entwickeln fokussierte Android-Erlebnisse, die Kinder selbst verstehen und Eltern vor der Weitergabe eines Geräts gut einschätzen können.",
        "footer": ("Datenschutz", "Support", "Kontakt", "Impressum", "Eine Marke von Appmonto Studio"),
    },
    "es": {
        "title": "KidLogic Loft — Apps infantiles tranquilas, sin anuncios ni ruido",
        "description": "KidLogic Loft crea apps tranquilas y sin anuncios para niños de 3 a 8 años. Puzles diseñados con cuidado para niños y padres.",
        "nav": ("Apps", "Principios", "Quiénes somos"), "theme": ("Usar tema oscuro", "Usar tema claro"),
        "eyebrow": "Divertidas para los niños. Tranquilas para los padres.",
        "hero": "Apps tranquilas para niños curiosos.",
        "intro": "Juego móvil pensado para niños de 3 a 8 años: funciona sin conexión y no tiene anuncios, seguimiento, suscripciones ni compras dentro de la app.",
        "cta": ("Ver las apps", "Cómo diseñamos"),
        "facts": (("Edades", "3–8"), ("Precio", "Gratis"), ("Juego", "Sin conexión"), ("Publicidad", "Ninguna")),
        "apps_head": ("Nuestras apps", "Pequeños mundos, creados con cuidado.", "Mecánicas claras para los niños y condiciones claras para los padres."),
        "live": "En Google Play", "learn": "Ver la app",
        "octo": "Puzles sencillos y coloridos, con piezas grandes y un pulpo simpático. Para teléfonos y tabletas.",
        "coming": "En desarrollo", "beaver": "Una tranquila aventura en tren sobre ayudar a los vecinos de camino a un pícnic.",
        "diorama": "Un diorama interactivo y tranquilo: los personajes cobran vida con un toque y después vuelven a descansar.",
        "principles_head": ("Nuestros principios", "Diseñadas para la tranquilidad de los padres.", "El juego se queda dentro del producto. Nuestras promesas son claras y concretas."),
        "principles": (("Privacidad desde el principio", "Sin cuentas, analíticas, perfiles de comportamiento ni recopilación de datos personales."), ("Sin presión comercial", "Sin anuncios, compras dentro de la app, suscripciones, temporizadores ni urgencia artificial."), ("Funciona sin conexión", "El juego principal está disponible sin conexión, sin registro y sin internet.")),
        "about_head": ("Quiénes somos", "Apps independientes, creadas en Austria."),
        "about": "KidLogic Loft es la marca de apps infantiles de Appmonto Studio. Creamos experiencias Android enfocadas que los niños pueden entender por sí solos y que los padres pueden valorar antes de entregarles un dispositivo.",
        "footer": ("Privacidad", "Soporte", "Contacto", "Aviso legal", "Una marca de Appmonto Studio"),
    },
}

def route(lang, suffix=""):
    prefix = "" if lang == "en" else f"/{lang}"
    return f"{prefix}/{suffix}".replace("//", "/")

def language_switch(lang):
    return "".join(f'<a href="{route(x)}" hreflang="{x}" lang="{x}"' + (' aria-current="page"' if x == lang else '') + f'>{x.upper()}</a>' for x in LANGS)

def theme_button(t):
    return f'''<button class="theme-toggle" type="button" data-theme-toggle data-label-dark="{escape(t["theme"][0])}" data-label-light="{escape(t["theme"][1])}" aria-label="{escape(t["theme"][0])}" aria-pressed="false"><svg class="theme-toggle__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.66 6.34l1.41-1.41"/></svg><svg class="theme-toggle__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 15.1A8.5 8.5 0 0 1 8.9 4a8.5 8.5 0 1 0 11.1 11.1Z"/></svg></button>'''

def render(lang):
    t = T[lang]
    facts = "".join(f'<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>' for k, v in t["facts"])
    principles = "".join(f'<article class="principle-card"><span class="line-icon" aria-hidden="true"></span><h3>{escape(h)}</h3><p>{escape(p)}</p></article>' for h, p in t["principles"])
    prefix = "" if lang == "en" else f"/{lang}"
    canonical = f"https://kidlogicloft.com{prefix}/"
    return f'''<!DOCTYPE html>
<html lang="{lang}" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script>try{{document.documentElement.dataset.theme=localStorage.getItem('kidlogic-theme')==='dark'?'dark':'light'}}catch(_){{document.documentElement.dataset.theme='light'}}</script>
  <title>{escape(t["title"])}</title>
  <meta name="description" content="{escape(t["description"])}" />
  <meta name="theme-color" content="#FBF7EF" />
  <meta property="og:title" content="{escape(t["title"])}" />
  <meta property="og:description" content="{escape(t["description"])}" />
  <meta property="og:url" content="{canonical}" /><meta property="og:type" content="website" />
  <meta property="og:image" content="https://kidlogicloft.com/apps/happy-octo-puzzle/banner.png" />
  <meta property="og:image:width" content="1024" /><meta property="og:image:height" content="500" />
  <meta property="og:locale" content="{LOCALES[lang]}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" href="/favicon.png" /><link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="en" href="https://kidlogicloft.com/" /><link rel="alternate" hreflang="de" href="https://kidlogicloft.com/de/" /><link rel="alternate" hreflang="es" href="https://kidlogicloft.com/es/" /><link rel="alternate" hreflang="x-default" href="https://kidlogicloft.com/" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"KidLogic Loft","url":"https://kidlogicloft.com","description":"{escape(t["description"])}","email":"hello@kidlogicloft.com","parentOrganization":{{"@type":"Organization","name":"Appmonto Studio","url":"https://appmonto.com"}}}}</script>
  <link rel="stylesheet" href="/assets/site.css" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="container header-inner">
    <a class="brand" href="{route(lang)}" aria-label="KidLogic Loft home"><span class="brand-mark" aria-hidden="true"></span><span>KidLogic Loft</span></a>
    <nav class="primary-nav" aria-label="Primary"><a href="#apps">{escape(t["nav"][0])}</a><a href="#principles">{escape(t["nav"][1])}</a><a href="#about">{escape(t["nav"][2])}</a></nav>
    <div class="header-tools"><nav class="lang-switch" aria-label="Language">{language_switch(lang)}</nav>{theme_button(t)}</div>
  </div></header>
  <main id="main">
    <section class="hero"><div class="container hero-grid"><div class="hero-copy"><p class="eyebrow">{escape(t["eyebrow"])}</p><h1>{escape(t["hero"])}</h1><p class="lead">{escape(t["intro"])}</p><div class="button-row"><a class="button button--primary" href="#apps">{escape(t["cta"][0])}</a><a class="button button--ghost" href="#principles">{escape(t["cta"][1])}</a></div></div><figure class="hero-art"><img src="/apps/happy-octo-puzzle/banner.png" alt="Happy Octo Puzzle underwater artwork" width="1024" height="500" /><figcaption>Happy Octo Puzzle</figcaption></figure></div><div class="container"><dl class="trust-bar">{facts}</dl></div></section>
    <section id="apps"><div class="container"><div class="section-head"><p class="eyebrow">{escape(t["apps_head"][0])}</p><h2>{escape(t["apps_head"][1])}</h2><p class="lead">{escape(t["apps_head"][2])}</p></div><div class="product-grid">
      <a class="product-card product-card--featured" href="{route(lang, 'apps/happy-octo-puzzle/')}"><img class="product-icon" src="/apps/happy-octo-puzzle/icon.png" alt="" width="96" height="96" /><div><span class="status status--live">{escape(t["live"])}</span><h3>Happy Octo Puzzle</h3><p>{escape(t["octo"])}</p><span class="text-link">{escape(t["learn"])} →</span></div></a>
      <article class="product-card"><span class="product-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 18h16M6 18V9l6-4 6 4v9M9 12h6M12 9v6"/></svg></span><span class="status">{escape(t["coming"])}</span><h3>Clever Beaver</h3><p>{escape(t["beaver"])}</p></article>
      <article class="product-card"><span class="product-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 17c3-7 13-7 16 0M7 10c1.5-2 3-3 5-3s3.5 1 5 3M12 7V3"/></svg></span><span class="status">{escape(t["coming"])}</span><h3>Cozy Meadow Farm</h3><p>{escape(t["diorama"])}</p></article>
    </div></div></section>
    <section id="principles" class="section-tint"><div class="container"><div class="section-head"><p class="eyebrow">{escape(t["principles_head"][0])}</p><h2>{escape(t["principles_head"][1])}</h2><p class="lead">{escape(t["principles_head"][2])}</p></div><div class="principles-grid">{principles}</div></div></section>
    <section id="about"><div class="container about-grid"><div class="section-head"><p class="eyebrow">{escape(t["about_head"][0])}</p><h2>{escape(t["about_head"][1])}</h2></div><div class="about-copy"><p>{escape(t["about"])}</p><a class="text-link" href="https://appmonto.com" rel="noopener">Appmonto Studio →</a></div></div></section>
  </main>
  <footer class="site-footer"><div class="container footer-grid"><a class="brand" href="{route(lang)}"><span class="brand-mark" aria-hidden="true"></span><span>KidLogic Loft</span></a><nav class="footer-links" aria-label="Footer"><a href="{route(lang, 'apps/happy-octo-puzzle/')}">Happy Octo Puzzle</a><a href="{route(lang, 'privacy/')}">{escape(t["footer"][0])}</a><a href="mailto:hello@kidlogicloft.com?subject=Support">{escape(t["footer"][1])}</a><a href="https://appmonto.com" rel="noopener">Appmonto Studio</a><a href="https://appmonto.com/legal/" rel="noopener">{escape(t["footer"][3])}</a><a href="mailto:hello@kidlogicloft.com">{escape(t["footer"][2])}</a></nav><small>© <span id="year">2026</span> KidLogic Loft · {escape(t["footer"][4])}</small></div></footer>
  <script src="/assets/site.js" defer></script>
</body></html>'''

for lang in LANGS:
    target = ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")
    target.write_text(render(lang), encoding="utf-8")
