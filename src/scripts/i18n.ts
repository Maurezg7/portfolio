export type Lang = "es" | "en";

const messages: Record<Lang, Record<string, string>> = {
  es: {},
  en: {
    "nav.menu": "Menu",
    "nav.home": "HOME",
    "nav.about": "ABOUT ME",
    "nav.skills": "SKILLS",
    "nav.projects": "PROJECTS",
    "nav.contact": "CONTACT",
    "nav.lang": "Language",

    "home.role": "FULL STACK DEVELOPER",
    "home.line":
      "I build the whole product: the API, the interface and the data. Clear code, ready to grow.",
    "home.cta": "About me",

    "about.kicker": "ABOUT_ME",
    "about.title": "FULL STACK DEVELOPER",
    "about.tab.me": "About me",
    "about.tab.back": "Backend",
    "about.tab.front": "Frontend",
    "about.tab.data": "Data",
    "about.me.title":
      "I'm Mauro, a software developer. I study at the Provincial University of Administration, Technology and Trades (UPATECO) and I look for projects where I can really build.",
    "about.me.text":
      "I work on the whole product: APIs with Java, Spring Boot, NestJS and FastAPI, interfaces with Angular, Next.js, Svelte and Astro, and PostgreSQL for the data.",
    "about.back.title": "Java, Spring Boot, NestJS and FastAPI",
    "about.back.text":
      "I design REST APIs with JWT login, validation and error handling. I use DTO and SOLID so the service is easy to keep and extend.",
    "about.front.title": "Angular, Next.js, Svelte and Astro",
    "about.front.text":
      "I build interfaces that are easy to read on a computer and on a phone, connected to REST APIs, with the screen state under control.",
    "about.data.title": "PostgreSQL",
    "about.data.text":
      "I design the database, write queries with joins and subqueries, and connect it from Spring Boot, NestJS and FastAPI.",
    "about.cta": "SKILLS",

    "skills.label": "SKILLS_",
    "skills.languages": "LANGUAGES",
    "skills.backend": "BACKEND",
    "skills.frontend": "FRONTEND",
    "skills.data": "DATA",

    "projects.kicker": "PROJECTS",
    "projects.details": "SEE DETAILS",
    "projects.site": "WEBSITE",
    "projects.repo": "REPOSITORY",
    "projects.back": "PROJECTS",
    "projects.visit": "VISIT SITE",
    "projects.code": "SEE CODE",
    "projects.desc": "DESCRIPTION",
    "projects.features": "FEATURES",
    "projects.team": "TEAM",

    "project.sem.badge": "🏆 2ND PLACE — PUNATECH HACKATHON",
    "project.sem.date": "MAY_2026",
    "project.estelares.badge": "HACKATHON · ARGENTINA CHALLENGE",
    "project.estelares.date": "SEPTEMBER_2026",
    "project.invoice.badge": "HACKATHON · ALEPH",
    "project.invoice.date": "AUGUST_2026",
    "project.meetflow.badge": "SIMULATION · NO COUNTRY",
    "project.meetflow.date": "OCTOBER_2026",
    "project.hermes.date": "MARCH_2026",
    "project.portfolio.date": "MAY_2026",

    "project.estelares.desc":
      "Estelares is a remittance app on the Stellar testnet, made for the Argentina Challenge. You can send money that arrives in seconds, receive it with a QR, collect a pool with your community and create a family box. The key never leaves Freighter: you sign in the wallet.",
    "project.estelares.points":
      "Payments on Horizon testnet, and you always sign in Freighter||Receive money with a QR||Community pool: on-chain vault and a leaderboard read from the contract||Family box with Stellar multisig and deposit and withdraw roles||Reference swap between XLM, USDC and EURC||Django backend for the product modules",

    "project.invoice.desc":
      "INVOICE compares an invoice with its purchase order and explains every difference. All the work stays on your computer. The React and Vite frontend sends the file to an Express backend. That backend reads PDFs or images and compares them with fixed rules and an on-device model using QVAC. Nothing goes to the cloud. Built for the Aleph Hackathon.",
    "project.invoice.points":
      "Upload a PDF or an image and extract the text on your computer with OCR||Compare it with the purchase order on the same machine||On-device model with QVAC, with no API keys and no cost per token||Every difference is explained, and manual review is marked||Session history in the frontend",

    "project.meetflow.desc":
      "MeetFlow is an app to start and join video calls. I built it with a team in the No Country work simulation. The host opens a room, shares the link and approves people waiting to enter. A guest can join without an account. The frontend is Next.js. The API is Express, with Prisma and PostgreSQL. The call uses GetStream, and the waiting room tells the host through Socket.IO.",
    "project.meetflow.points":
      "An instant meeting or a scheduled one, with a code to join||Waiting room: the host approves each person, with an account or as a guest||Several hosts, screen share, chat and reactions||Local recording and one microphone per account||Frontend on Vercel and API on Render, with Prisma on PostgreSQL",

    "project.agrocentinela.desc":
      "Offline-first PWA of weather alerts for farmers in Northwest Argentina, built for the Código Facilito Kiro + AWS Hackathon. It checks frost risk and water stress and gives clear alerts. Offline is the normal case, not a backup: it works with no signal and syncs when the connection comes back.",
    "project.agrocentinela.points":
      "Real offline-first setup: Service Worker + Background Sync + IndexedDB||AI in three layers with a fallback: cloud (Amazon Bedrock), on-device (Prompt API) and a rules engine as the guarantee||8 browser APIs with a real job (Geolocation, getUserMedia, Canvas, Web Push, Network Information and others)||End-to-end Web Push with VAPID||Leaf check from a photo, with a histogram on canvas, processed on the device",

    "project.yieldvault.desc":
      "Autonomous yield farming agent on Casper, built during the Casper Agentic Buildathon. I worked as Smart Contracts Lead. The smart contract is in Rust with the Odra framework, deployed and easy to check on Casper Testnet. It saves the agent's decisions on-chain for audit.",
    "project.yieldvault.points":
      "Rust/Odra contract (v2.7.2), deployed and easy to check on Casper Testnet||On-chain action log (log_action) so the history cannot be changed||execute_swap is the core of the rebalance, and the deposit reads the value with attached_value()||Deploy fixed after an out-of-gas error (gas limit changed from 200 to 500 CSPR)",

    "project.hermes.desc":
      "Hermes is a platform for company management and communication. The backend is Java and Spring Boot, with a safe REST API and JWT login. The Angular frontend uses that API and shows a clear, responsive interface.",
    "project.hermes.points":
      "Login and permissions with JWT||REST API documented with Swagger||Responsive design with SASS/SCSS||Relational database with PostgreSQL||Deployed on Vercel",

    "project.portfolio.desc":
      "Personal portfolio built with Astro. The site shows projects, skills and contact, with native view transitions and a custom dark design.",
    "project.portfolio.points":
      "Static site with Astro||View transitions with the View Transitions API||Custom styles with SASS/SCSS||Responsive design for every screen||Deployed on GitHub Pages",

    "project.sem.desc":
      "SEM Salta is a metered parking system. People pay for parking time online. It uses MercadoPago and has an admin panel for zones, prices and users. Built for the Municipality of Salta and awarded 2nd place at the PunaTech Hackathon.",
    "project.sem.points":
      "MercadoPago integration||Admin panel||Backend with NestJS and PostgreSQL||Frontend with React, Vite and Tailwind||Deployed on Vercel",
    "project.sem.award": "🏆 2ND PLACE — PUNATECH HACKATHON",

    "contact.tag": "CONTACT_",
    "contact.line":
      "Do you have a project in mind, or do you want to talk about a job? I am available.",
    "contact.ready": "OPEN TO WORK",
    "contact.email": "YOUR_EMAIL",
    "contact.message": "MESSAGE",
    "contact.emailPh": "hello@example.com",
    "contact.messagePh": "Tell me your idea...",
    "contact.send": "SEND MESSAGE",
  },
};

let lang: Lang = "es";

export function getLang(): Lang {
  return lang;
}

export function t(key: string): string {
  if (lang === "es") return "";
  return messages.en[key] ?? "";
}

function apply(root: ParentNode = document) {
  root.querySelectorAll<HTMLElement>("[data-i18n]").forEach((el) => {
    const key = el.dataset.i18n;
    if (!key) return;
    const value = t(key);
    if (lang === "en" && value) el.textContent = value;
  });

  root.querySelectorAll<HTMLElement>("[data-i18n-list]").forEach((list) => {
    const key = list.dataset.i18nList;
    if (!key || lang !== "en") return;
    const value = t(key);
    if (!value) return;
    const parts = value.split("||");
    const items = list.querySelectorAll("li");
    parts.forEach((part, index) => {
      if (items[index]) items[index].textContent = part;
    });
  });

  root.querySelectorAll<HTMLElement>("[data-i18n-placeholder]").forEach((el) => {
    const key = el.dataset.i18nPlaceholder;
    if (!key || lang !== "en") return;
    const value = t(key);
    if (value && "placeholder" in el) (el as HTMLInputElement).placeholder = value;
  });

  root.querySelectorAll<HTMLElement>("[data-i18n-aria]").forEach((el) => {
    const key = el.dataset.i18nAria;
    if (!key || lang !== "en") return;
    const value = t(key);
    if (value) el.setAttribute("aria-label", value);
  });

  document.documentElement.lang = lang === "en" ? "en" : "es";
  document.querySelectorAll<HTMLButtonElement>("[data-set-lang]").forEach((button) => {
    button.classList.toggle("is-on", button.dataset.setLang === lang);
    button.setAttribute("aria-pressed", button.dataset.setLang === lang ? "true" : "false");
  });
}

export function setLang(next: Lang) {
  if (next === lang) return;
  lang = next;
  localStorage.setItem("portfolio-lang", next);
  if (next === "es") window.location.reload();
  else apply();
}

export function installGlobals() {
  const runtime = window as Window & {
    __portfolioT?: (key: string) => string;
    __portfolioLang?: () => Lang;
  };
  runtime.__portfolioT = t;
  runtime.__portfolioLang = () => lang;
}

export function initLanguage() {
  installGlobals();
  const saved = localStorage.getItem("portfolio-lang");
  lang = saved === "en" ? "en" : "es";
  apply();

  const runtime = window as Window & {
    __langClick?: (event: Event) => void;
    __setPortfolioLang?: (next: Lang) => void;
  };
  runtime.__setPortfolioLang = setLang;
  if (runtime.__langClick) document.removeEventListener("click", runtime.__langClick);
  runtime.__langClick = (event: Event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;
    const button = target.closest<HTMLButtonElement>("[data-set-lang]");
    if (!button?.dataset.setLang) return;
    const next = button.dataset.setLang === "en" ? "en" : "es";
    runtime.__setPortfolioLang?.(next);
  };
  document.addEventListener("click", runtime.__langClick);
}

export function translateElement(el: HTMLElement, key: string) {
  el.dataset.i18n = key;
  const value = t(key);
  if (lang === "en" && value) el.textContent = value;
}
