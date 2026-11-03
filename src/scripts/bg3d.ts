import {
  AdditiveBlending,
  BufferAttribute,
  BufferGeometry,
  Clock,
  Color,
  Group,
  IcosahedronGeometry,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  PlaneGeometry,
  Points,
  Scene,
  ShaderMaterial,
  TorusGeometry,
  TorusKnotGeometry,
  Vector2,
  Vector3,
  WebGLRenderer,
} from "three";

const GREEN = new Color(0x7dff5a);
const ORANGE = new Color(0xff9a3d);
const WHITE = new Color(0xffffff);

const pointsVert = /* glsl */ `
  attribute float aSeed;
  attribute vec3 aColor;
  uniform float uTime, uPulse, uSize, uPixel;
  uniform vec3 uMouse;
  varying vec3 vColor;
  varying float vGlow;
  void main() {
    vec3 p = position;
    p.x += sin(uTime * 0.25 + aSeed * 6.283) * 0.6;
    p.y += cos(uTime * 0.2 + aSeed * 9.0) * 0.6;
    p.z += sin(uTime * 0.15 + aSeed * 4.0) * 0.8;
    // repel from the pointer
    vec3 d = p - uMouse;
    float md = length(d.xy);
    p.xy += normalize(d.xy + 1e-4) * smoothstep(4.5, 0.0, md) * 1.8;
    // click shockwave: expanding ring from the pointer
    float ring = abs(length(p.xy - uMouse.xy) - uPulse * 22.0);
    float wave = smoothstep(2.2, 0.0, ring) * (1.0 - uPulse) * step(0.0, uPulse) * step(uPulse, 1.0);
    p.z += wave * 3.0;
    vColor = mix(aColor, vec3(1.0), wave);
    vGlow = 0.55 + wave * 0.9 + smoothstep(4.5, 0.0, md) * 0.6;
    vec4 mv = modelViewMatrix * vec4(p, 1.0);
    gl_PointSize = uSize * uPixel * (1.0 + wave * 1.5) * (30.0 / -mv.z);
    gl_Position = projectionMatrix * mv;
  }
`;
const pointsFrag = /* glsl */ `
  varying vec3 vColor;
  varying float vGlow;
  void main() {
    float r = length(gl_PointCoord - 0.5);
    float a = smoothstep(0.5, 0.0, r);
    gl_FragColor = vec4(vColor * vGlow, a * a);
  }
`;
const coreVert = /* glsl */ `
  varying vec3 vN; varying vec3 vV; varying float vY;
  uniform float uTime;
  void main() {
    vec3 p = position + normal * sin(position.y * 2.0 + uTime * 1.4) * 0.12;
    vec4 mv = modelViewMatrix * vec4(p, 1.0);
    vN = normalize(normalMatrix * normal);
    vV = normalize(-mv.xyz);
    vY = position.y;
    gl_Position = projectionMatrix * mv;
  }
`;
const coreFrag = /* glsl */ `
  varying vec3 vN; varying vec3 vV; varying float vY;
  uniform float uTime, uMix;
  uniform vec3 uA, uB;
  void main() {
    float f = pow(1.0 - max(dot(vN, vV), 0.0), 2.4);
    vec3 c = mix(uA, uB, 0.5 + 0.5 * sin(vY * 0.9 + uTime * 0.8 + uMix * 3.14));
    gl_FragColor = vec4(c * (0.25 + f * 1.6), f * 0.9);
  }
`;


const nebulaVert = /* glsl */ `
  varying vec2 vUv;
  void main() { vUv = uv; gl_Position = vec4(position.xy, 0.9999, 1.0); }
`;
const nebulaFrag = /* glsl */ `
  varying vec2 vUv;
  uniform float uTime, uAspect;
  uniform vec2 uMouse;
  float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
  float noise(vec2 p) {
    vec2 i = floor(p), f = fract(p); f = f * f * (3.0 - 2.0 * f);
    return mix(mix(hash(i), hash(i + vec2(1, 0)), f.x), mix(hash(i + vec2(0, 1)), hash(i + vec2(1, 1)), f.x), f.y);
  }
  float fbm(vec2 p) { float v = 0.0, a = 0.5; for (int i = 0; i < 5; i++) { v += a * noise(p); p *= 2.02; a *= 0.5; } return v; }
  void main() {
    vec2 uv = (vUv - 0.5) * vec2(uAspect, 1.0);
    vec2 m = uMouse * 0.15;
    float t = uTime * 0.03;
    float n1 = fbm(uv * 1.6 + vec2(t, -t) + m);
    float n2 = fbm(uv * 2.4 - vec2(t * 1.3, t) - m + n1);
    vec3 green = vec3(0.49, 1.0, 0.35);
    vec3 orange = vec3(1.0, 0.6, 0.24);
    vec3 col = vec3(0.039);
    col += green * pow(n1, 3.2) * 0.34 * smoothstep(0.9, -0.3, uv.y + 0.2);
    col += orange * pow(n2, 3.6) * 0.30 * smoothstep(-0.9, 0.5, uv.x);
    float vig = smoothstep(1.25, 0.25, length(uv));
    col *= 0.35 + 0.65 * vig;
    col += (hash(vUv * 900.0 + uTime) - 0.5) * 0.018; // film grain
    gl_FragColor = vec4(col, 1.0);
  }
`;
const gridVert = /* glsl */ `
  varying vec3 vW;
  void main() { vec4 w = modelMatrix * vec4(position, 1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }
`;
const gridFrag = /* glsl */ `
  varying vec3 vW;
  uniform float uTime;
  uniform vec3 uMouse;
  void main() {
    vec2 g = vec2(vW.x, vW.z + uTime * 1.6);
    vec2 d = abs(fract(g - 0.5) - 0.5) / fwidth(g);
    float line = 1.0 - min(min(d.x, d.y), 1.0);
    vec2 g5 = g / 5.0;
    vec2 d5 = abs(fract(g5 - 0.5) - 0.5) / fwidth(g5);
    float major = 1.0 - min(min(d5.x, d5.y), 1.0);
    float fade = smoothstep(70.0, 6.0, length(vW.xz - vec2(0.0, 8.0)));
    float glow = smoothstep(9.0, 0.0, distance(vW.xz, uMouse.xz));
    vec3 col = vec3(0.49, 1.0, 0.35) * line * 0.45 + vec3(1.0, 0.6, 0.24) * major * 0.9;
    col += vec3(1.0) * glow * line * 0.6;
    gl_FragColor = vec4(col * fade, max(line, major) * fade);
  }
`;

function sceneProfile(path: string) {
  const p = path.replace(/\/$/, "");
  if (p === "/portfolio" || p === "") return { x: 0, y: 0, s: 1.0, mix: 0 };
  if (p.endsWith("/skills")) return { x: 6.5, y: 0, s: 0.75, mix: 1 };
  if (p.endsWith("/aboutme")) return { x: -6.5, y: 0, s: 0.75, mix: 0.5 };
  if (p.endsWith("/contact")) return { x: 6, y: -1, s: 0.8, mix: 0.8 };
  return { x: 7, y: 1, s: 0.65, mix: 0.2 };
}

export function initBackground(canvas: HTMLCanvasElement) {
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const renderer = new WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: "high-performance" });
  renderer.setClearColor(0x000000, 0);
  const scene = new Scene();
  const camera = new PerspectiveCamera(60, 1, 0.1, 100);
  camera.position.z = 14;

  const tiny = () => Math.min(innerWidth, innerHeight) < 500;
  const count = tiny() ? 700 : 2600;

  // ---- particles (custom shader: drift, pointer repel, click shockwave)
  const pos = new Float32Array(count * 3);
  const col = new Float32Array(count * 3);
  const seed = new Float32Array(count);
  const palette = [GREEN, GREEN, ORANGE, WHITE];
  for (let i = 0; i < count; i++) {
    pos[i * 3] = (Math.random() - 0.5) * 44;
    pos[i * 3 + 1] = (Math.random() - 0.5) * 30;
    pos[i * 3 + 2] = (Math.random() - 0.5) * 30;
    const c = palette[Math.floor(Math.random() * palette.length)];
    col.set([c.r, c.g, c.b], i * 3);
    seed[i] = Math.random();
  }
  const pg = new BufferGeometry();
  pg.setAttribute("position", new BufferAttribute(pos, 3));
  pg.setAttribute("aColor", new BufferAttribute(col, 3));
  pg.setAttribute("aSeed", new BufferAttribute(seed, 1));
  const pointsMat = new ShaderMaterial({
    vertexShader: pointsVert,
    fragmentShader: pointsFrag,
    transparent: true,
    depthWrite: false,
    blending: AdditiveBlending,
    uniforms: {
      uTime: { value: 0 },
      uPulse: { value: -1 },
      uSize: { value: 1.6 },
      uPixel: { value: 1 },
      uMouse: { value: new Vector3(999, 999, 0) },
    },
  });
  const points = new Points(pg, pointsMat);
  scene.add(points);

  // ---- hero object: glowing fresnel core + wire knot + orbit rings
  const group = new Group();
  const coreMat = new ShaderMaterial({
    vertexShader: coreVert,
    fragmentShader: coreFrag,
    transparent: true,
    depthWrite: false,
    blending: AdditiveBlending,
    uniforms: { uTime: { value: 0 }, uMix: { value: 0 }, uA: { value: GREEN }, uB: { value: ORANGE } },
  });
  const core = new Mesh(new IcosahedronGeometry(2.1, tiny() ? 3 : 5), coreMat);
  const knot = new Mesh(
    new TorusKnotGeometry(3.1, 0.35, tiny() ? 90 : 220, 10),
    new MeshBasicMaterial({ color: GREEN, wireframe: true, transparent: true, opacity: 0.2, blending: AdditiveBlending }),
  );
  const rings: Mesh[] = [0, 1, 2].map((i) => {
    const m = new Mesh(
      new TorusGeometry(4.2 + i * 0.7, 0.012, 8, 160),
      new MeshBasicMaterial({ color: i === 1 ? ORANGE : WHITE, transparent: true, opacity: 0.35, blending: AdditiveBlending }),
    );
    m.rotation.set(Math.random() * 3, Math.random() * 3, 0);
    return m;
  });
  group.add(core, knot, ...rings);
  scene.add(group);

  // ---- deep-space nebula backdrop (fullscreen, always behind everything)
  const nebulaMat = new ShaderMaterial({
    vertexShader: nebulaVert,
    fragmentShader: nebulaFrag,
    depthTest: false,
    depthWrite: false,
    uniforms: { uTime: { value: 0 }, uAspect: { value: 1 }, uMouse: { value: new Vector2() } },
  });
  const nebula = new Mesh(new PlaneGeometry(2, 2), nebulaMat);
  nebula.frustumCulled = false;
  nebula.renderOrder = -10;
  scene.add(nebula);

  // ---- infinite neon grid floor (perspective depth)
  const gridMat = new ShaderMaterial({
    vertexShader: gridVert,
    fragmentShader: gridFrag,
    transparent: true,
    depthWrite: false,
    blending: AdditiveBlending,
    uniforms: { uTime: { value: 0 }, uMouse: { value: new Vector3(999, 0, 999) } },
  });
  const grid = new Mesh(new PlaneGeometry(160, 160), gridMat);
  grid.rotation.x = -Math.PI / 2;
  grid.position.y = -7;
  grid.renderOrder = -5;
  scene.add(grid);

  // ---- interaction
  const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  const world = new Vector3();
  const ndc = new Vector3();
  const updateWorld = () => {
    ndc.set(mouse.tx, -mouse.ty, 0.5).unproject(camera);
    const dir = ndc.sub(camera.position).normalize();
    const dist = -camera.position.z / dir.z;
    world.copy(camera.position).addScaledVector(dir, dist);
    pointsMat.uniforms.uMouse.value.copy(world);
  };
  addEventListener("pointermove", (e) => {
    mouse.tx = (e.clientX / innerWidth - 0.5) * 2;
    mouse.ty = (e.clientY / innerHeight - 0.5) * 2;
  });
  let pulseStart = -10;
  addEventListener("pointerdown", (e) => {
    mouse.tx = (e.clientX / innerWidth - 0.5) * 2;
    mouse.ty = (e.clientY / innerHeight - 0.5) * 2;
    updateWorld();
    pulseStart = clock.getElapsedTime();
  });
  let scrollY = 0;
  addEventListener("scroll", () => (scrollY = window.scrollY || 0), { passive: true });

  // ---- route-aware composition (object moves aside so text stays readable)
  const target = { x: 0, y: 0, s: 1, mix: 0 };
  const apply = () => {
    const pr = sceneProfile(location.pathname);
    if (innerWidth < 900) Object.assign(target, { x: 0, y: 3.5, s: pr.s * 0.55, mix: pr.mix });
    else Object.assign(target, pr);
  };
  apply();
  document.addEventListener("astro:page-load", apply);

  const resize = () => {
    const w = innerWidth, h = innerHeight;
    const pr = Math.min(devicePixelRatio, 2);
    renderer.setPixelRatio(pr);
    pointsMat.uniforms.uPixel.value = pr;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    nebulaMat.uniforms.uAspect.value = w / h;
    camera.position.z = w / h < 0.8 ? 20 : 14;
    camera.updateProjectionMatrix();
    apply();
  };
  const clock = new Clock();
  resize();
  addEventListener("resize", resize);

  let mix = 0;
  let raf = 0;
  const frame = () => {
    const t = clock.getElapsedTime();
    mouse.x += (mouse.tx - mouse.x) * 0.06;
    mouse.y += (mouse.ty - mouse.y) * 0.06;
    updateWorld();

    pointsMat.uniforms.uTime.value = t;
    pointsMat.uniforms.uPulse.value = (t - pulseStart) / 1.6;
    coreMat.uniforms.uTime.value = t;
    nebulaMat.uniforms.uTime.value = t;
    nebulaMat.uniforms.uMouse.value.set(mouse.x, -mouse.y);
    gridMat.uniforms.uTime.value = t;
    gridMat.uniforms.uMouse.value.set(world.x * 2.2, 0, 14 - (mouse.y + 1) * 14);

    group.position.x += (target.x - group.position.x) * 0.04;
    group.position.y += (target.y - group.position.y) * 0.04;
    const s = group.scale.x + (target.s - group.scale.x) * 0.04;
    group.scale.setScalar(s);
    mix += (target.mix - mix) * 0.04;
    coreMat.uniforms.uMix.value = mix;

    core.rotation.y = t * 0.2;
    knot.rotation.set(t * 0.12 + mouse.y * 0.5, t * 0.17 + mouse.x * 0.5, 0);
    rings.forEach((r, i) => {
      r.rotation.x += 0.002 * (i + 1);
      r.rotation.y += 0.0015 * (3 - i);
    });
    points.rotation.y = t * 0.02 + mouse.x * 0.25;
    camera.position.y = -scrollY * 0.004 + mouse.y * -0.8;
    camera.position.x = mouse.x * 0.8;
    camera.lookAt(0, 0, 0);

    renderer.render(scene, camera);
    if (!reduced) raf = requestAnimationFrame(frame);
  };
  frame();

  document.addEventListener("visibilitychange", () => {
    cancelAnimationFrame(raf);
    if (!document.hidden && !reduced) frame();
  });
}
