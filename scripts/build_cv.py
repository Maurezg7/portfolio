#!/usr/bin/env python3
"""Genera los CV en PDF (ES y EN) en public/docs. Requiere: pip install reportlab."""

import shutil
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "public" / "docs"

INK = HexColor("#111111")
MUTED = HexColor("#444444")
ACCENT = HexColor("#111111")
RULE = HexColor("#888888")

FONT_CANDIDATES = [
    ("/usr/share/fonts/noto/NotoSans-Regular.ttf", "/usr/share/fonts/noto/NotoSans-Bold.ttf"),
    ("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf", "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"),
    ("/usr/share/fonts/liberation/LiberationSans-Regular.ttf", "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]


def register_fonts():
    for regular, bold in FONT_CANDIDATES:
        if Path(regular).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("CV", regular))
            pdfmetrics.registerFont(TTFont("CV-Bold", bold))
            pdfmetrics.registerFontFamily("CV", normal="CV", bold="CV-Bold", italic="CV", boldItalic="CV-Bold")
            return "CV", "CV-Bold"
    return "Helvetica", "Helvetica-Bold"


CONTACT = {
    "phone": "+54 9 387 563 7692",
    "email": "mauroleonelg7@gmail.com",
    "links": [
        ("maurezg7.github.io/portfolio", "https://maurezg7.github.io/portfolio/"),
        ("github.com/Maurezg7", "https://github.com/Maurezg7"),
        ("linkedin.com/in/maurezg7", "https://www.linkedin.com/in/maurezg7/"),
    ],
}

CV = {
    "es": {
        "file": "Mauro_Gomez_CV_Java_ES.pdf",
        "lang": "es-AR",
        "role": "Desarrollador Full Stack Junior (Java, React)",
        "location": "Salta, Argentina (UTC-3)",
        "subject": "CV de Mauro Gomez, desarrollador full stack: Java y React",
        "sections": {
            "profile": "Perfil",
            "skills": "Habilidades técnicas",
            "experience": "Experiencia laboral",
            "projects": "Proyectos",
            "education": "Educación",
            "extra": "Información adicional",
        },
        "profile": (
            "Desarrollo APIs REST con <b>Java y Spring Boot</b> e interfaces con <b>React</b>. "
            "En Hermes implementé la autenticación con JWT y modelé los datos en PostgreSQL. "
            "En SEM Salta desarrollé la interfaz de pago con Mercado Pago en un equipo de tres. "
            "Busco un puesto remoto de desarrollo backend o full stack."
        ),
        "skills": [
            ("Backend", "Java, Spring Boot, Spring Security, Spring Data JPA, Hibernate, Maven, JWT, APIs REST"),
            ("Frontend", "React, TypeScript, JavaScript, HTML5, CSS3, Tailwind CSS, Vite"),
            ("Datos y herramientas", "PostgreSQL, SQL, modelado relacional, Git, GitHub, Docker, Nginx"),
            ("Programación de sistemas", "C"),
            ("Prácticas", "Programación orientada a objetos (POO), MVC, SOLID, DTO, metodologías ágiles"),
            ("En aprendizaje", "JUnit, Mockito, Kafka, Spring Cloud, Kubernetes, AWS, GitHub Actions y Next.js"),
            ("Rust (en aprendizaje)", "Tokio, Axum, Actix Web, SQLx, Serde y Odra"),
        ],
        "experience": [
            {
                "title": "MeetFlow - App de videollamadas",
                "meta": "No Country (simulación laboral) | Octubre 2026",
                "stack": "Next.js, Tailwind CSS, Express, Prisma, PostgreSQL, GetStream, Socket.IO",
                "bullets": [
                    "Desarrollamos en equipo una app para iniciar o programar videollamadas y compartir un código de acceso.",
                    "La sala de espera notifica al anfitrión por Socket.IO para que apruebe cada ingreso. GetStream permite compartir pantalla y conversar por chat.",
                ],
                "links": [
                    ("web-ruddy-mu-22.vercel.app", "https://web-ruddy-mu-22.vercel.app"),
                    ("github.com/No-Country-simulation/S08-26-equipo-5", "https://github.com/No-Country-simulation/S08-26-equipo-5"),
                ],
            },
            {
                "title": "Gestión de Biblioteca - Sistema en Java",
                "meta": "Softtek (prácticas / simulación laboral) | Julio 2025 - Agosto 2025",
                "stack": "Java, MVC",
                "bullets": [
                    "Desarrollamos en equipo un sistema de biblioteca en Java, separando el modelo, la vista y el controlador.",
                ],
                "links": [("github.com/gianalercia/GestionBibliotecaMVC", "https://github.com/gianalercia/GestionBibliotecaMVC")],
            },
        ],
        "projects": [
            {
                "title": "Hermes - Plataforma de mensajería y comunidades",
                "meta": "Proyecto personal | 2026",
                "stack": "Java 21, Spring Boot 3.4, Spring Security, JWT, Spring Data JPA, PostgreSQL, Angular 21, Docker, Nginx",
                "bullets": [
                    "Protegí las rutas de la API con Spring Security y JWT. La verificación por correo usa códigos de seis dígitos que vencen a los cinco minutos.",
                    "Modelé amistades, canales y notificaciones en PostgreSQL y expuse los mensajes mediante una API REST que consulta el cliente Angular.",
                ],
                "links": [("hermes-inky-two.vercel.app", "https://hermes-inky-two.vercel.app/")],
            },
            {
                "title": "SEM Salta - Sistema de estacionamiento medido",
                "meta": "Hackathon PunaTech, segundo puesto | 2026",
                "stack": "React, Vite, Tailwind CSS, NestJS, PostgreSQL, MercadoPago",
                "bullets": [
                    "Desarrollé el frontend en React para que los usuarios pudieran pagar su tiempo de estacionamiento con Mercado Pago.",
                    "Conecté la interfaz de pago con la API REST del sistema durante el hackatón.",
                ],
                "links": [("parki-pay.vercel.app", "https://parki-pay.vercel.app/")],
            },
            {
                "title": "Achique - Bloqueo judicial de streaming pirata en vivo",
                "meta": "Hackathon Argentina Space, primer puesto | 2026",
                "stack": "Python 3, biblioteca estándar, HMAC, SHA-256, Docker",
                "bullets": [
                    "Cada detección genera un expediente con evidencia verificable. Un juez revisa y firma la orden; el bloqueo por IP vence al terminar el partido.",
                    "Un registro público encadena los eventos por hash para que se pueda verificar el historial de cada orden.",
                ],
                "links": [
                    ("achique-g8j6.onrender.com", "https://achique-g8j6.onrender.com"),
                    ("github.com/Maurezg7/achique", "https://github.com/Maurezg7/achique"),
                ],
            },
            {
                "title": "AgroCentinela - PWA de alertas agroclimáticas offline-first",
                "meta": "Hackathon Kiro + AWS (Código Facilito) | 2026",
                "stack": "React 18, Vite, TypeScript, NestJS en AWS Lambda, DynamoDB, AWS SAM, Zod",
                "bullets": [
                    "Desarrollé el proyecto de forma individual: backend, frontend, infraestructura y despliegue.",
                    "PWA offline-first en React y TypeScript (Service Worker, Background Sync, IndexedDB), con notificaciones push y un motor de recomendaciones en capas (Amazon Bedrock con respaldo on-device y reglas).",
                    "Backend serverless con infraestructura como código (AWS SAM) y contratos de datos compartidos con Zod.",
                    "Desplegado en Netlify; probado por jueces y entre 15 y 20 usuarios durante el hackathon.",
                ],
                "links": [
                    ("agrocentinela.netlify.app", "https://agrocentinela.netlify.app/"),
                    ("github.com/Maurezg7/AgroCentinela", "https://github.com/Maurezg7/AgroCentinela"),
                ],
            },
            {
                "title": "Dengue Centinela - Vigilancia comunitaria de dengue",
                "meta": "Hackathon | 2026",
                "stack": "React 19, Express, Prisma",
                "bullets": [
                    "Desarrollé el backend para el registro y la consulta de reportes comunitarios de dengue en Salta.",
                    "Diseñé el modelo de datos y las rutas REST consumidas por el frontend en React 19.",
                ],
                "links": [
                    ("app.dengue-centinela.workers.dev", "https://app.dengue-centinela.workers.dev"),
                ],
            },
            {
                "title": "YieldVault - Smart contract en Rust sobre Casper",
                "meta": "Casper Agentic Buildathon | 2026",
                "stack": "Rust, Odra Framework, Casper Testnet",
                "bullets": [
                    "Como Smart Contracts Lead, desarrollé un smart contract en Rust desplegado en Casper Testnet, con registro on-chain de las acciones del agente para trazabilidad y auditoría.",
                    "Funciones de rebalanceo y depósito; resolví una falla out-of-gas en el despliegue al ajustar el gas de 200 a 500 CSPR.",
                ],
                "links": [("github.com/EstebanNahuelok/casper-yield-agent", "https://github.com/EstebanNahuelok/casper-yield-agent")],
            },
        ],
        "link_label": "Enlaces",
        "education": [
            ("Tecnicatura en Desarrollo de Software", "UPATecO - Universidad Provincial de Administración, Tecnología y Oficios", "2023 - 2025"),
            ("Club Java Master, formación intensiva", "Udemy", "2025"),
            ("Desarrollo Web", "CoderHouse", "2021"),
        ],
        "extra": [
            ("Idiomas", "Español (nativo), Inglés (B1)"),
            ("Otros conocimientos", "Álgebra, Análisis Matemático, Unity, Godot"),
            ("Comunidad", "Participante activo de SaltaDev y de hackatones (Argentina Space, PunaTech, Kiro + AWS, Casper)."),
        ],
    },
    "en": {
        "file": "Mauro_Gomez_CV_Java_EN.pdf",
        "lang": "en",
        "role": "Junior Full Stack Developer (Java, React)",
        "location": "Salta, Argentina (UTC-3)",
        "subject": "Resume of Mauro Gomez, full stack developer: Java and React",
        "sections": {
            "profile": "Summary",
            "skills": "Technical skills",
            "experience": "Work experience",
            "projects": "Projects",
            "education": "Education",
            "extra": "Additional information",
        },
        "profile": (
            "I build REST APIs with <b>Java and Spring Boot</b> and user interfaces with <b>React</b>. "
            "For Hermes, I implemented JWT authentication and designed the PostgreSQL data model. "
            "For SEM Salta, I built the Mercado Pago checkout interface on a team of three. "
            "I am looking for a remote backend or full stack developer role."
        ),
        "skills": [
            ("Backend", "Java, Spring Boot, Spring Security, Spring Data JPA, Hibernate, Maven, JWT, REST APIs"),
            ("Frontend", "React, TypeScript, JavaScript, HTML5, CSS3, Tailwind CSS, Vite"),
            ("Data & tools", "PostgreSQL, SQL, relational modeling, Git, GitHub, Docker, Nginx"),
            ("Systems programming", "C"),
            ("Practices", "Object-oriented programming (OOP), MVC, SOLID, DTO, agile development"),
            ("Currently learning", "JUnit, Mockito, Kafka, Spring Cloud, Kubernetes, AWS, GitHub Actions and Next.js"),
            ("Rust (currently learning)", "Tokio, Axum, Actix Web, SQLx, Serde and Odra"),
        ],
        "experience": [
            {
                "title": "MeetFlow - Video call app",
                "meta": "No Country (work simulation) | October 2026",
                "stack": "Next.js, Tailwind CSS, Express, Prisma, PostgreSQL, GetStream, Socket.IO",
                "bullets": [
                    "Worked on a team to build an app for starting or scheduling video calls and inviting participants with a join code.",
                    "The waiting room notifies the host through Socket.IO for admission approval. GetStream handles screen sharing and chat.",
                ],
                "links": [
                    ("web-ruddy-mu-22.vercel.app", "https://web-ruddy-mu-22.vercel.app"),
                    ("github.com/No-Country-simulation/S08-26-equipo-5", "https://github.com/No-Country-simulation/S08-26-equipo-5"),
                ],
            },
            {
                "title": "Library Management - Java system",
                "meta": "Softtek (internship / work simulation) | July 2025 - August 2025",
                "stack": "Java, MVC",
                "bullets": [
                    "Worked on a team to build a Java library management system with separate model, view and controller layers.",
                ],
                "links": [("github.com/gianalercia/GestionBibliotecaMVC", "https://github.com/gianalercia/GestionBibliotecaMVC")],
            },
        ],
        "projects": [
            {
                "title": "Hermes - Messaging and community platform",
                "meta": "Personal project | 2026",
                "stack": "Java 21, Spring Boot 3.4, Spring Security, JWT, Spring Data JPA, PostgreSQL, Angular 21, Docker, Nginx",
                "bullets": [
                    "Secured API routes with Spring Security and JWT. Email verification uses six-digit codes that expire after five minutes.",
                    "Modeled friendships, channels and notifications in PostgreSQL and exposed messages through a REST API for the Angular client.",
                ],
                "links": [("hermes-inky-two.vercel.app", "https://hermes-inky-two.vercel.app/")],
            },
            {
                "title": "SEM Salta - Metered parking system",
                "meta": "PunaTech Hackathon, 2nd place | 2026",
                "stack": "React, Vite, Tailwind CSS, NestJS, PostgreSQL, MercadoPago",
                "bullets": [
                    "Built the React frontend so drivers could pay for metered parking through Mercado Pago.",
                    "Connected the payment interface to the backend REST API during the hackathon.",
                ],
                "links": [("parki-pay.vercel.app", "https://parki-pay.vercel.app/")],
            },
            {
                "title": "Achique - Live judicial blocking of pirate streaming",
                "meta": "Argentina Space Hackathon, 1st place | 2026",
                "stack": "Python 3, standard library, HMAC, SHA-256, Docker",
                "bullets": [
                    "Each detection creates a case file with verifiable evidence. A judge reviews and signs the order; the IP block expires when the match ends.",
                    "A public, hash-chained log makes each order’s history independently verifiable.",
                ],
                "links": [
                    ("achique-g8j6.onrender.com", "https://achique-g8j6.onrender.com"),
                    ("github.com/Maurezg7/achique", "https://github.com/Maurezg7/achique"),
                ],
            },
            {
                "title": "AgroCentinela - Offline-first agro-climate alerts PWA",
                "meta": "Kiro + AWS Hackathon (Código Facilito) | 2026",
                "stack": "React 18, Vite, TypeScript, NestJS on AWS Lambda, DynamoDB, AWS SAM, Zod",
                "bullets": [
                    "Built the project individually: backend, frontend, infrastructure and deployment.",
                    "Offline-first PWA in React and TypeScript (Service Worker, Background Sync, IndexedDB), with push notifications and a layered recommendation engine (Amazon Bedrock with on-device fallback and rules).",
                    "Serverless backend with infrastructure as code (AWS SAM) and shared data contracts with Zod.",
                    "Deployed on Netlify; tested by judges and about 15 to 20 users during the hackathon.",
                ],
                "links": [
                    ("agrocentinela.netlify.app", "https://agrocentinela.netlify.app/"),
                    ("github.com/Maurezg7/AgroCentinela", "https://github.com/Maurezg7/AgroCentinela"),
                ],
            },
            {
                "title": "Dengue Centinela - Community dengue surveillance",
                "meta": "Hackathon | 2026",
                "stack": "React 19, Express, Prisma",
                "bullets": [
                    "Built the backend for logging and querying community dengue reports in Salta.",
                    "Designed the data model and the REST routes consumed by the React 19 frontend.",
                ],
                "links": [
                    ("app.dengue-centinela.workers.dev", "https://app.dengue-centinela.workers.dev"),
                ],
            },
            {
                "title": "YieldVault - Rust smart contract on Casper",
                "meta": "Casper Agentic Buildathon | 2026",
                "stack": "Rust, Odra Framework, Casper Testnet",
                "bullets": [
                    "As Smart Contracts Lead, built a Rust smart contract deployed on Casper Testnet, with on-chain logging of the agent's actions for traceability and auditing.",
                    "Implemented rebalancing and deposit functions; fixed an out-of-gas deployment failure by raising the deploy gas from 200 to 500 CSPR.",
                ],
                "links": [("github.com/EstebanNahuelok/casper-yield-agent", "https://github.com/EstebanNahuelok/casper-yield-agent")],
            },
        ],
        "link_label": "Links",
        "education": [
            ("Software Development (Tecnicatura program)", "UPATecO - Provincial University of Administration, Technology and Trades", "2023 - 2025"),
            ("Club Java Master, intensive training", "Udemy", "2025"),
            ("Web Development", "CoderHouse", "2021"),
        ],
        "extra": [
            ("Languages", "Spanish (native), English (B1)"),
            ("Other knowledge", "Algebra, Calculus, Unity, Godot"),
            ("Community", "Active member of SaltaDev; hackathons: Argentina Space, PunaTech, Kiro + AWS, Casper."),
        ],
    },
}


def link(label, url):
    return f'<link href="{url}" color="#111111">{label}</link>'


def build(lang, font, bold):
    cv = CV[lang]
    out = DOCS / cv["file"]

    def style(name, **kw):
        base = dict(fontName=font, fontSize=10.2, leading=14.2, textColor=INK)
        base.update(kw)
        return ParagraphStyle(name, **base)

    s_name = style("name", fontName=bold, fontSize=26, leading=29, spaceAfter=2)
    s_role = style("role", fontName=bold, fontSize=12, leading=15, textColor=INK)
    s_contact = style("contact", fontSize=9, leading=12.5, textColor=MUTED)
    s_section = style("section", fontName=bold, fontSize=10.3, leading=13.5, textColor=ACCENT, spaceBefore=10, spaceAfter=2)
    s_body = style("body")
    s_title = style("title", fontSize=10.4, leading=14)
    s_stack = style("stack", fontSize=8.5, leading=11.4, textColor=MUTED, spaceAfter=1.5)
    s_bullet = style("bullet", leftIndent=9, bulletIndent=1, spaceAfter=0.6, bulletFontName=font)
    s_small = style("small", fontSize=8.7, leading=11.8, textColor=MUTED)

    def section(key):
        return [
            Paragraph(cv["sections"][key].upper(), s_section),
            HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=0, spaceAfter=4),
        ]

    def heading(title, meta):
        # Una sola línea de texto: las fechas en una columna aparte se leen fuera de orden.
        return Paragraph(f'<b>{title}</b> <font size="8.6" color="#444444">| {meta}</font>', s_title)

    story = [
        Paragraph("Mauro Gomez", s_name),
        Paragraph(cv["role"], s_role),
        Spacer(1, 2),
        Paragraph(f'{cv["location"]} | {CONTACT["phone"]} | {link(CONTACT["email"], "mailto:" + CONTACT["email"])}', s_contact),
        Paragraph(" | ".join(link(l, u) for l, u in CONTACT["links"]), s_contact),
    ]

    story += section("profile") + [Paragraph(cv["profile"], s_body)]

    story += section("skills")
    for label, value in cv["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s_body))

    for key in ("experience", "projects"):
        story += section(key)
        for p in cv[key]:
            block = [heading(p["title"], p["meta"]), Paragraph(p["stack"], s_stack)]
            block += [Paragraph(b, s_bullet, bulletText="•") for b in p["bullets"]]
            if p["links"]:
                block.append(Paragraph(f'{cv["link_label"]}: ' + " | ".join(link(l, u) for l, u in p["links"]), s_bullet))
            block.append(Spacer(1, 5))
            story.append(KeepTogether(block))

    story += section("education")
    for title, place, when in cv["education"]:
        story.append(KeepTogether([heading(title, when), Paragraph(place, s_small), Spacer(1, 3)]))

    story += section("extra")
    for label, value in cv["extra"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s_body))

    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=13 * mm,
        title="Mauro Gomez - " + cv["role"],
        creator="Mauro Gomez",
        author="Mauro Gomez",
        subject=cv["subject"],
        keywords="Java, Spring Boot, React, TypeScript, PostgreSQL, C, Rust",
        lang=cv["lang"],
    )
    doc.build(story)
    print(f"OK -> {out.relative_to(ROOT)} ({doc.page} pág.)")


if __name__ == "__main__":
    DOCS.mkdir(parents=True, exist_ok=True)
    regular, bold = register_fonts()
    for lang in CV:
        build(lang, regular, bold)
    shutil.copyfile(DOCS / CV["es"]["file"], DOCS / "Mauro_Gomez_CV.pdf")
