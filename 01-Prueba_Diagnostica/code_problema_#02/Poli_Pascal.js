// ============================
//  Poli_Pascal.js
//  Descripción:
//  Genera los coeficientes del polinomio (x+1)^n usando el Triángulo de Pascal.
//  Evalúa f(x) = (x+1)^n paso a paso y mide el tiempo de ejecución.
//  Guarda los resultados en resultados_js.txt
// ============================

const fs = require("fs");
const path = require("path");
const prompt = require("prompt-sync")({ sigint: true });

// Función para Generar los coeficientes del Triángulo de Pascal
function generarCoeficientes(n) {
  const pascal = [];
  for (let i = 0; i <= n; i++) {
    pascal[i] = new Array(i + 1).fill(1);
    for (let j = 1; j < i; j++) {
      pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
    }
  }
  return pascal[n];
}

// Función para Mostrar el polinomio generado
function mostrarPolinomio(coef) {
  const n = coef.length - 1;
  const partes = [];
  coef.forEach((c, i) => {
    const exp = n - i;
    if (exp > 1) partes.push(`${c !== 1 ? c : ""}x^${exp}`);
    else if (exp === 1) partes.push(`${c !== 1 ? c : ""}x`);
    else partes.push(`${c}`);
  });
  return partes.join(" + ");
}

// Función para Evaluar el polinomio paso a paso
function evaluarPolinomio(coef, x) {
  const n = coef.length - 1;
  const pasos = [];
  let total = 0;
  coef.forEach((c, i) => {
    const exp = n - i;
    const valor = c * Math.pow(x, exp);
    pasos.push(`${c}*(x^${exp}) = ${valor}`);
    total += valor;
  });
  return { pasos, total };
}

// PROGRAMA PRINCIPAL
function main() {
  console.log("===============================");
  console.log("  POLINOMIO DE PASCAL (x+1)^n ");
  console.log("===============================");

  const n = parseInt(prompt("Ingrese el valor de n: "));
  const x = parseFloat(prompt("Ingrese el valor de x: "));

  if (isNaN(n) || isNaN(x)) {
    console.log("✗ Entrada inválida. Use números válidos.");
    return;
  }

  const inicio = process.hrtime.bigint(); // Inicio en nanosegundos

  const coef = generarCoeficientes(n);
  const polinomio = mostrarPolinomio(coef);
  const { pasos, total } = evaluarPolinomio(coef, x);

  const fin = process.hrtime.bigint(); // Fin en nanosegundos
  const duracion = Number(fin - inicio) / 1e9; // Convertir a segundos con decimales

  // Mostrar resultados en consola
  console.log(`\nCoeficientes: [${coef.join(", ")}]`);
  console.log(`(x+1)^${n} = ${polinomio}`);
  console.log("\nCálculo paso a paso:");
  pasos.forEach(p => console.log(" ", p));
  console.log(`\nResultado final: f(${x}) = ${total}`);
  console.log(`\n🕔 Tiempo de ejecución: ${duracion.toFixed(6)} segundos`);

  // Guardar resultados en archivo
  const rutaArchivo = path.join(__dirname, "resultados_js.txt");
  let contenido = `\n--- Resultados para n=${n}, x=${x} ---\n`;
  contenido += `Coeficientes: [${coef.join(", ")}]\n`;
  contenido += `Polinomio: (x+1)^${n} = ${polinomio}\n`;
  contenido += `Cálculo paso a paso:\n`;
  pasos.forEach(p => (contenido += `  ${p}\n`));
  contenido += `Resultado final: f(${x}) = ${total}\n`;
  contenido += `Tiempo de ejecución: ${duracion.toFixed(6)} segundos\n`;
  contenido += "----------------------------------------\n";

  fs.appendFileSync(rutaArchivo, contenido, "utf-8");
  console.log("\n🗸 Resultados guardados en 'resultados_js.txt'");
}

main();