#!/usr/bin/env python3
"""Genera public/docs/Mauro_Gomez_CV.pdf (formato Harvard / ATS, una página)."""

from pathlib import Path

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "docs" / "Mauro_Gomez_CV.pdf"

SERIF = "/usr/share/fonts/noto/NotoSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/noto/NotoSerif-Bold.ttf"
SANS = "/usr/share/fonts/noto/NotoSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/noto/NotoSans-Bold.ttf"

# Fallback si Noto Bold no está con ese nombre
for bold_try in (
    "/usr/share/fonts/noto/NotoSerif-Bold.ttf",
    "/usr/share/fonts/TTF/NimbusRoman-Bold.ttf",
):
    if Path(bold_try).exists():
        SERIF_BOLD = bold_try
        break
for bold_try in (
    "/usr/share/fonts/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/TTF/crosextra/Carlito-Bold.ttf",
):
    if Path(bold_try).exists():
        SANS_BOLD = bold_try
        break

pdfmetrics.registerFont(TTFont("CVSerif", SERIF))
pdfmetrics.registerFont(TTFont("CVSerifBold", SERIF_BOLD))
pdfmetrics.registerFont(TTFont("CVSans", SANS))
pdfmetrics.registerFont(TTFont("CVSansBold", SANS_BOLD))

INK = HexColor("#1a1a1a")
MUTED = HexColor("#444444")
RULE = HexColor("#222222")


def wrap(c, text, font, size, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if c.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_section(c, y, title, left, right):
    c.setFont("CVSansBold", 9.2)
    c.setFillColor(INK)
    c.drawString(left, y, title.upper())
    y -= 2.2 * mm
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(left, y, right, y)
    return y - 3.6 * mm


def draw_bullets(c, y, items, left, width, size=8.4, leading=3.15 * mm):
    for item in items:
        lines = wrap(c, item, "CVSans", size, width - 4 * mm)
        for i, line in enumerate(lines):
            if y < 14 * mm:
                return y
            if i == 0:
                c.setFont("CVSans", size)
                c.setFillColor(INK)
                c.drawString(left, y, "•")
                c.drawString(left + 3.2 * mm, y, line)
            else:
                c.drawString(left + 3.2 * mm, y, line)
            y -= leading
        y -= 0.4 * mm
    return y


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4)
    W, H = A4
    left = 16 * mm
    right = W - 16 * mm
    width = right - left
    y = H - 16 * mm

    # Nombre
    c.setFillColor(INK)
    c.setFont("CVSerifBold", 20)
    c.drawCentredString(W / 2, y, "MAURO GOMEZ")
    y -= 6 * mm

    c.setFont("CVSans", 9.5)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, "Desarrollador Full Stack")
    y -= 4.2 * mm

    contact = (
        "Salta, Argentina  |  +54 9 3875 637692  |  mauroleonelg7@gmail.com"
    )
    c.setFont("CVSans", 7.8)
    c.drawCentredString(W / 2, y, contact)
    y -= 3.4 * mm
    links = (
        "github.com/Maurezg7  |  linkedin.com/in/maurezg7  |  "
        "instagram.com/isdeiko  |  maurezg7.github.io/portfolio"
    )
    c.drawCentredString(W / 2, y, links)
    y -= 6 * mm

    # Perfil (corto, tono humano)
    y = draw_section(c, y, "Perfil", left, right)
    profile = (
        "Estudio Desarrollo de Software en UPATECO (Salta). Armo el producto "
        "completo: API, interfaz y datos. Trabajo sobre todo con Java, Spring Boot, "
        "NestJS, FastAPI, Angular, Next.js y PostgreSQL. Busco un equipo donde "
        "pueda seguir construyendo en producción."
    )
    for line in wrap(c, profile, "CVSans", 8.6, width):
        c.setFont("CVSans", 8.6)
        c.setFillColor(INK)
        c.drawString(left, y, line)
        y -= 3.4 * mm
    y -= 2.2 * mm

    # Educación
    y = draw_section(c, y, "Educación", left, right)
    c.setFont("CVSansBold", 9)
    c.setFillColor(INK)
    c.drawString(left, y, "Tecnicatura en Desarrollo de Software")
    c.setFont("CVSans", 8.5)
    c.drawRightString(right, y, "2023 – actualidad")
    y -= 3.3 * mm
    c.setFont("CVSans", 8.3)
    c.setFillColor(MUTED)
    c.drawString(left, y, "UPATECO — Universidad Provincial de Administración, Tecnología y Oficios")
    y -= 3.5 * mm
    c.setFont("CVSansBold", 9)
    c.setFillColor(INK)
    c.drawString(left, y, "Club Java Master")
    c.setFont("CVSans", 8.5)
    c.drawRightString(right, y, "2025")
    y -= 3.3 * mm
    c.setFont("CVSans", 8.3)
    c.setFillColor(MUTED)
    c.drawString(left, y, "Udemy — formación intensiva en Java y Spring")
    y -= 3.5 * mm
    c.setFont("CVSansBold", 9)
    c.setFillColor(INK)
    c.drawString(left, y, "Desarrollo Web")
    c.setFont("CVSans", 8.5)
    c.drawRightString(right, y, "2021")
    y -= 3.3 * mm
    c.setFont("CVSans", 8.3)
    c.setFillColor(MUTED)
    c.drawString(left, y, "CoderHouse")
    y -= 5 * mm

    # Proyectos
    y = draw_section(c, y, "Proyectos", left, right)

    projects = [
        {
            "title": "MeetFlow",
            "meta": "Simulación laboral No Country  |  Oct 2026",
            "bullets": [
                "App de videollamadas en equipo: salas, sala de espera e invitados sin cuenta.",
                "Next.js + Express + Prisma + PostgreSQL; llamadas con GetStream y Socket.IO.",
                "Sitio: web-ruddy-mu-22.vercel.app — github.com/No-Country-simulation/S08-26-equipo-5",
            ],
        },
        {
            "title": "SEM Salta",
            "meta": "Hackathon PunaTech — 2.º puesto  |  May 2026",
            "bullets": [
                "Estacionamiento medido digital para la Municipalidad de Salta, con pagos MercadoPago.",
                "NestJS, React, Vite, Tailwind y PostgreSQL. Equipo de tres.",
                "Sitio: parki-pay.vercel.app",
            ],
        },
        {
            "title": "Estelares",
            "meta": "Hackathon Argentina Challenge  |  Sep 2026",
            "bullets": [
                "Remesas sobre Stellar testnet: envío, QR, pool comunitario y caja familiar con Freighter.",
                "React, Vite, Tailwind y Django. Sitio: frontend-estellares.vercel.app",
            ],
        },
        {
            "title": "INVOICE",
            "meta": "Hackathon Aleph  |  Ago 2026",
            "bullets": [
                "Compara factura y orden de compra en la máquina local (OCR + reglas + QVAC on-device).",
                "React, Vite, TypeScript y Express. Repo: github.com/leitolml1/invoice",
            ],
        },
        {
            "title": "AgroCentinela",
            "meta": "Hackathon Kiro + AWS  |  2026",
            "bullets": [
                "PWA offline-first de alertas de helada y estrés hídrico para productores del NOA.",
                "React, NestJS en AWS Lambda, DynamoDB. Sitio: agrocentinela.netlify.app",
            ],
        },
        {
            "title": "YieldVault",
            "meta": "Casper Agentic Buildathon — Smart Contracts Lead  |  2026",
            "bullets": [
                "Contrato en Rust/Odra en Casper Testnet; log on-chain de las decisiones del agente.",
            ],
        },
        {
            "title": "Hermes",
            "meta": "Proyecto personal  |  Mar 2026",
            "bullets": [
                "Plataforma de gestión y comunicación: Spring Boot + JWT, Angular y PostgreSQL.",
                "Sitio: hermes-inky-two.vercel.app",
            ],
        },
    ]

    for p in projects:
        if y < 28 * mm:
            break
        c.setFont("CVSansBold", 9)
        c.setFillColor(INK)
        c.drawString(left, y, p["title"])
        y -= 3.1 * mm
        c.setFont("CVSans", 7.8)
        c.setFillColor(MUTED)
        c.drawString(left, y, p["meta"])
        y -= 3.2 * mm
        y = draw_bullets(c, y, p["bullets"], left, width, size=8.1, leading=3.0 * mm)
        y -= 1.4 * mm

    # Skills
    y = draw_section(c, y, "Habilidades", left, right)
    skills = [
        ("Lenguajes", "Java, TypeScript, Python, C, C++, Rust"),
        ("Backend", "Spring Boot, NestJS, FastAPI, Express, JWT, Prisma"),
        ("Frontend", "Angular, Next.js, Svelte, Astro, React, Tailwind, SCSS"),
        ("Datos", "PostgreSQL"),
        ("Otros", "Git, Docker, Vercel, Render, GetStream, Stellar"),
    ]
    for label, value in skills:
        c.setFont("CVSansBold", 8.2)
        c.setFillColor(INK)
        label_t = f"{label}: "
        c.drawString(left, y, label_t)
        x = left + c.stringWidth(label_t, "CVSansBold", 8.2)
        c.setFont("CVSans", 8.2)
        c.setFillColor(MUTED)
        for line in wrap(c, value, "CVSans", 8.2, width - (x - left)):
            c.drawString(x, y, line)
            y -= 3.1 * mm
            x = left + 2 * mm
        y += 0.3 * mm
    y -= 1.5 * mm

    # Extra
    y = draw_section(c, y, "Idiomas y más", left, right)
    extras = [
        "Español nativo. Inglés en progreso (cerca de B1).",
        "Participo en SaltaDev y en hackathons cuando puedo.",
    ]
    y = draw_bullets(c, y, extras, left, width, size=8.2, leading=3.1 * mm)

    c.showPage()
    c.save()
    print(f"OK -> {OUT}")


if __name__ == "__main__":
    build()
