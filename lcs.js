const args = process.argv.slice(2);

if (!args.length) {
  console.log("");
  return;
}

// Найдём самое короткое слово для минимизации перебора
const shortest = args.reduce((a, b) => a.length <= b.length ? a : b);
const len = shortest.length;

// Пройдем по длинам подстрок от длинной к короткой
for (let l = len; l > 0; l--) {
  for (let i = 0; i <= len - l; i++) {
    const sub = shortest.slice(i, i + l);

    // Проверяем, что все строки содержат подстроку
    if (args.every(s => s.includes(sub))) {
      console.log(sub);
      process.exit(0); // быстрее, чем return в цикле
    }
  }
}

console.log("");
