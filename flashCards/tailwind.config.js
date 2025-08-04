/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './**/templates/**/*.html',  // Охватывает все уровни вложенности шаблонов
        './**/*.py',                 // Если вы используете классы в строках Python
    ],
    darkMode: 'class',
    theme: {
        extend: {},
    },
    plugins: [],

}